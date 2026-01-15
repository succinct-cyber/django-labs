from django.shortcuts import render

def home(request):
    return render(request, 'christmas/home.html')


def about(request):
    return render(request, "christmas/about.html")

def christmas_view(request):
    context = {
        "title": "Christmas",
        "subtitle": "A quiet build, a calm season.",
    }
    return render(request, "base.html", context)

def christmas_view(request):
    return render(request, "base.html", {
        "page_title": "Christmas",
        "page_note": "A quiet build. No rush.",
    })

def christmas_home(request):
    return render(request, 'christmas/christmas.html', {
        'title': 'Christmas App',
        'subtitle': 'Slow down. Breathe. Build',
    })



