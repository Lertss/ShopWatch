from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from io import BytesIO
from PIL import Image
from django.core.files import File


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name '), max_length=50)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    counts = models.CharField("Country", max_length=200)

    def __str__(self):
        return self.counts


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    genr = models.CharField("Genre", max_length=100)

    def __str__(self):
        return self.genr


class Tegs(models.Model):
    id = models.AutoField(primary_key=True)
    teg = models.CharField("Teg", max_length=100)

    def __str__(self):
        return self.teg


class Categorys(models.Model):
    CHOICES = (
        ('Manga', 'Manga'),
        ('Manhua', 'Manhua'),
        ('Manhwa', 'Manhwa'),
        ('Comics', 'Comics'),
        ('Other', 'Other'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, choices=CHOICES, unique=True)
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def __str__(self):
        return self.title


class Manga(models.Model):
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE, related_name='category')
    id = models.AutoField(primary_key=True)
    name_manga = models.CharField(_('name_manga'), max_length=100, blank=False)
    name_original = models.CharField(_('name_original'), max_length=100, blank=True)
    author = models.ManyToManyField(Author, related_name='actors')
    time_prod = models.DateTimeField('time of production', default=datetime.today())
    counts = models.ManyToManyField(Country, related_name='country')
    tegs = models.ManyToManyField(Tegs, related_name='tegs')
    genre = models.ManyToManyField(Genre, related_name='genre')
    review = models.TextField(max_length=500)
    avatar = models.ImageField(upload_to='static/images/avatars/',
                               default='default/none_avatar.png/',
                               blank=True)
    thumbnail = models.ImageField(upload_to='media/products/miniava', blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name_manga

    def get_avatar(self):
        if self.avatar:
            return 'http://127.0.0.1:8000' + self.avatar.url
        return ''

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.avatar:
                self.thumbnail = self.make_thumbnail(self.avatar)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, avatar):
        img = Image.open(avatar)
        img = img.resize((100, 150))

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=avatar.name)
        return thumbnail


class Glawa(models.Model):
    id = models.AutoField(primary_key=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='glaws')
    num = models.FloatField(blank=False)
    title = models.CharField(max_length=50, null=True, blank=True)
    time_prod = models.DateTimeField('time of production', default=datetime.today())
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ["-num"]

    def get_absolute_url(self):
        return f'/{self.manga.slug}/{self.slug}/'

    def data_g(self):
        return self.time_prod.strftime("%m/%d/%Y")

    def __str__(self):
        return self.title


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='static/images/gallery/')
    glawa = models.ForeignKey(Glawa, on_delete=models.CASCADE, related_name='galleries')

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
