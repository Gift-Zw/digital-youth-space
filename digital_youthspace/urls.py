"""
URL configuration for digital_youthspace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from core import views
from digital_youthspace import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="home"),
    path('blog/', views.blog_view, name="blog"),
    path('feed/', views.feed_view, name="feed"),
    path('educational-articles/<str:category>/', views.articles_view, name="articles"),
    path('gallery', views.gallery_view, name="gallery"),
    path('about/', views.about_view, name="about"),
    path('browse/', views.browse_view, name="browse"),
    path('contact/', views.contact_view, name="contact"),
    path('blog-detail/<int:id>/', views.blog_detail_view, name="blog-detail"),
    path('edu/<int:id>/', views.article_detail_view, name="article-detail"),
    path('contact/success/', views.contact_success_view, name='contact_success'),
    path('gallery-images/<int:id>/', views.images_view, name="images"),
    path('logout/', views.logout_view, name="logout"),
    path('log-in/', views.RegularUserLoginView.as_view(), name="user-login"),
    path('register/', views.UserRegistrationView.as_view(), name="user-register"),

]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
