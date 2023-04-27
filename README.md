# UpTrader-MenuApp

This is a Django app that implements a tree menu with the following features:
- The menu is implemented through a template tag.
- All items above the selected item are expanded. The first level of nesting below the selected item is also expanded.
- The menu is stored in a database.
- It can be edited in Django's standard admin panel.
- The active menu item is determined based on the URL of the current page.
- There can be multiple menus on a single page, which are identified by name.
- Clicking on a menu item takes you to the URL specified in it. The URL can be specified explicitly or through a named URL.
- Rendering each menu requires exactly one database query.

To install this app, you can add 'menu_app' to your INSTALLED_APPS and include its URLs in your project's urls.py file.

This app requires Django and the standard Python library. To install the necessary dependencies, you can run:

```bash
pip install -r https://raw.githubusercontent.com/KolyanLock/UpTrader-MenuApp/main/requirements.txt
```
To use the menu tag in your templates, you can include the following code:
```django
{% load menu_tags %}

{% draw_menu 'main_menu' %}

```
You can change the name 'main_menu' to match the name of the menu you want to render.

<div style="text-align: right;">
Author: Nikolay T.<br>
Telegram: <a href="https://t.me/KolyanLock">@KolyanLock</a>
</div>