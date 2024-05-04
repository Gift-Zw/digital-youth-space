from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

ARTICLE_CATEGORIES = [
    ('Career Development', 'Career Development'),
    ('Personal Growth and Development', 'Personal Growth and Development'),
    ('Leadership & Entrepreneurship', 'Leadership & Entrepreneurship'),
    ('Financial Literacy', 'Financial Literacy'),
    ('Social Impact', 'Social Impact'),
    ('Health and Wellness', 'Health and Wellness'),
    ('Technology & Innovation', 'Technology & Innovation')
]


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name


class EducationalArticle(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, choices=ARTICLE_CATEGORIES)
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='articles')
    short_description = models.CharField(max_length=600)
    content = models.TextField(max_length=10000)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogItem(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='articles')
    short_description = models.CharField(max_length=600)
    content = models.TextField(max_length=10000)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    blog = models.ForeignKey(BlogItem, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1200)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog.title


class ImageCollection(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='collections')
    description = models.CharField(max_length=1200)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GalleryPicture(models.Model):
    collection = models.ForeignKey(ImageCollection, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.collection.title
