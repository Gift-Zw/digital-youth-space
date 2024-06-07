from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .admin import UserCreationForm
from .models import User, EducationalArticle, BlogItem, BlogComment, ImageCollection, GalleryPicture, ContactMessage
from .forms import CommentForm

from django.core.mail import send_mail
from django.contrib import messages
from .models import ContactMessage


# Create your views here.


def home_view(request):
    context = {
        'home_nav': 'active',
        'blog_posts': BlogItem.objects.all()[:3]
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


def articles_view(request, category):
    context = {
        'articles_nav': 'active',
        'educational_articles': EducationalArticle.objects.all() if (
                    category == "All") else EducationalArticle.objects.filter(category=category),
        'career': EducationalArticle.objects.filter(category='Career Development').count(),
        'personal': EducationalArticle.objects.filter(category='Personal Growth and Development').count(),
        'leadership': EducationalArticle.objects.filter(category='Leadership & Entrepreneurship').count(),
        'financial': EducationalArticle.objects.filter(category='Financial Literacy').count(),
        'social': EducationalArticle.objects.filter(category='Social Impact').count(),
        'health': EducationalArticle.objects.filter(category='Health and Wellness').count(),
        'technology': EducationalArticle.objects.filter(category='Technology & Innovation').count(),
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


def images_view(request, id):
    collection = ImageCollection.objects.filter(id=id).first()
    context = {
        'images': GalleryPicture.objects.filter(collection=collection),
        'gallery_nav': 'active',
        'title': collection.title
    }
    return render(request, 'images.html', context)


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


def logout_view(request):
    logout(request)
    return redirect('home')


class UserRegistrationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'register_user.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = User.objects.get(email=email)
        user.is_staff = False
        user.save()
        login(self.request, user)
        return redirect('home')


class RegularUserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user_login.html'
    redirect_authenticated_user = True
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy('home')
