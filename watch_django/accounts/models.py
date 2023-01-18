from __future__ import unicode_literals
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('user name'), max_length=50, blank=True, unique=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=False)
    avatar = models.ImageField(upload_to='static/images/avatars/', null=True, blank=True, default='static/images/avatars/none_avatar.png')
    is_staff = models.BooleanField('active', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)




# class Status_work(models.Model):
#     STATUS = (
#         ("watch", _("I will watch")),
#         ("looking", _("I'm looking")),
#         ("Viewed", _("Viewed")),
#         ("Favourite", _("Favourite")),
#     )
#
#     id = models.AutoField(primary_key=True)
#     id_user = models.ManyToManyField(User)
#     id_cinema = models.ManyToManyField(Manga)
#     status = models.CharField(max_length=32, choices=STATUS, default=None)
#
#     def __str__(self):
#         return self.status

# class Comment(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.TextField()
