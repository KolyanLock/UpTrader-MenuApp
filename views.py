from django.shortcuts import render


def example_view(request):
    context = {
        'request': request,
    }
    return render(request, 'example.html', context)

