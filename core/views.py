from django.shortcuts import render


# Create your views here.


def home_view(request):
    context = {
        'home_nav': 'active',
    }
    return render(request, 'home.html', context)


def blog_view(request):
    context = {
        'blog_nav': 'active',
    }
    return render(request, 'blog.html', context)


def articles_view(request):
    context = {
        'articles_nav': 'active',
    }
    return render(request, 'articles.html', context)


def feed_view(request):
    context = {
        'feed_nav': 'active',
    }
    return render(request, 'feed.html', context)


def gallery_view(request):
    context = {
        'gallery_nav': 'active',
    }
    return render(request, 'gallery.html', context)


def about_view(request):
    context = {
        'about_nav': 'active',
    }
    return render(request, 'about.html', context)


def contact_view(request):
    context = {
        'contact_nav': 'active',
    }
    return render(request, 'contact.html', context)
