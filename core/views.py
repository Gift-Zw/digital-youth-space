from django.shortcuts import render, redirect
from .models import User, EducationalArticle, BlogItem, BlogComment, ImageCollection, GalleryPicture, ContactMessage
from .forms import CommentForm

from django.core.mail import send_mail
from django.contrib import messages
from .models import ContactMessage


# Create your views here.


def home_view(request):
    context = {
        'home_nav': 'active',
    }
    return render(request, 'home.html', context)


def browse_view(request):
    context = {
        'browse_nav': 'active',
    }
    return render(request, 'browse.html', context)


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


def article_detail_view(request, id):
    article_item = EducationalArticle.objects.filter(id=id).first()

    context = {
        'articles_nav': 'active',
        'article': article_item

    }
    return render(request, 'article_detail.html', context)


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

    if request.method == "POST":
        message_name = request.POST.get('name')
        message_email = request.POST.get('email')
        message_subject = request.POST.get('subject')
        message_body = request.POST.get('message')

        ContactMessage.objects.create(
            name=message_name,
            email=message_email,
            subject=message_subject,
            message=message_body
        )

        return redirect('contact_success.html')


    else:
        return render(request, 'contact.html', context)


def contact_success_view(request):
    return render(request, 'contact_success.html')
