from django import template
from django.urls import reverse, resolve
from django.utils.html import escape
from django.utils.safestring import mark_safe

from ..models import MenuItem

register = template.Library()


def _get_menu_items(menu_name):
    """
    Get menu items for the given menu name.
    """
    return MenuItem.objects.filter(menu_name=menu_name)


def _is_active_menu_item(request_path, url):
    """
    Check if the URL is active (i.e. is the current request path).
    """
    if not url:
        return False

    try:
        url_name = resolve(url).url_name
        return request_path == reverse(url_name)
    except:
        return False


def _render_menu_items(menu_items, request_path):
    """
    Recursively render menu items and their children as a nested list.
    """
    if not menu_items:
        return ''

    menu_items_html = []
    for menu_item in menu_items:
        is_active = _is_active_menu_item(request_path, menu_item.url)

        menu_item_html = '<li class="{}">'.format('active' if is_active else '')

        if menu_item.url:
            menu_item_html += '<a href="{}">{}</a>'.format(escape(menu_item.url), escape(menu_item.title))
        else:
            menu_item_html += '<span>{}</span>'.format(escape(menu_item.title))

        children_html = _render_menu_items(menu_item.children.all(), request_path)
        if children_html:
            menu_item_html += '<ul>{}</ul>'.format(children_html)

        menu_item_html += '</li>'
        menu_items_html.append(menu_item_html)

    return ''.join(menu_items_html)


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
    Render a menu with the given menu name.
    """
    request = context.get('request')
    request_path = request.path if request else ''

    menu_items = _get_menu_items(menu_name)
    menu_items_html = _render_menu_items(menu_items, request_path)

    return mark_safe('<ul>{}</ul>'.format(menu_items_html))
