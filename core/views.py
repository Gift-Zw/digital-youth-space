from django.shortcuts import render
from .models import User, EducationalArticle, BlogItem, BlogComment, ImageCollection, GalleryPicture
from .forms import CommentForm


# Create your views here.


def home_view(request):
    context = {
        'home_nav': 'active',
    }
    return render(request, 'home.html', context)


def blog_view(request):
    context = {
        'blog_nav': 'active',
        'blog_items': BlogItem.objects.all()
    }
    return render(request, 'blog.html', context)


def blog_detail_view(request, id):
    blog_item = BlogItem.objects.filter(id=id).first()
    comments = BlogComment.objects.filter(blog=blog_item)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print('we in')
            comment = BlogComment.objects.create(
                blog=blog_item,
                comment=form.data['comment'],
                posted_by=request.user
            )
            comment.save()
    context = {
        'blog_nav': 'active',
        'blog_item': blog_item,
        'comments': comments,
        'form': CommentForm()
    }
    return render(request, 'blog_detail.html', context)


def articles_view(request):
    context = {
        'articles_nav': 'active',
        'educational_articles': EducationalArticle.objects.all(),
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
        'collections': ImageCollection.objects.all()
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
