# from email.policy import default
# from enum import unique
# from importlib.metadata import requires
# from random import choice
#
# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
#
#
# # Create your models here.
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, first_name, last_name, username, email, password=None):
#
#         if not email:
#             raise ValueError('User must have an email address')
#
#         if not username:
#             raise ValueError('User must have an username')
#
#         user = self.model(
#
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name
#
#         )
#
#         user.set_password(password)
#
#         user.save(using=self.db)
#         return user
#
#     def create_superuser(self, first_name, last_name, username, email, password=None):
#         user = self.create_user(
#
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name
#
#         )
#         user.is_admin = True
#         user.is_active = True
#         user.is_staff = True
#         user.superadmin = True
#         user.save(using=self._db)
#         return user
#
#
#
# class User(AbstractUser):
#
#     RESTAURANT = 1
#     CUSTOMER = 1
#     ROLE_EMOICE = (
#         (RESTAURANT, 'Restraunt'),
#         (CUSTOMER,'Customer'),
#
#     )
#
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     username = models.CharField(max_length=50,unique=True)
#     email = models.EmailField(unique=True,max_length=100)
#     role = models.PositiveSmallIntegerField(choices = ROLE_EMOICE,blank = True, null=True)
#
#
# # required fields
#
#     data_joined = models.DateTimeField(auto_now=True,blank=True, null=True)
#     last_login = models.DateTimeField(auto_now=True,blank=True, null=True)
#     created_data = models.DateTimeField(auto_now=True,blank=True, null=True)
#     modified_data = models.DateTimeField(auto_now=True,blank=True, null=True)
#     is_admin = models.BooleanField(default=False,blank=True, null=True)
#     is_staff = models.BooleanField(default=False,blank=True, null=True)
#     is_active = models.BooleanField(default=False,blank=True, null=True)
#     is_superadmin = models.BooleanField(default=False,blank=True, null=True)
#
#
#
#
# USERNAME = FIELD = 'emaill'
# REQUIRED_FILDES =  ['username','first_name','lastname ']
# objects = UserManager()
# def __str__(self):
#     return self.emaill
#
#
# def has_pers(self,perm,obj=None):
#     return self.is_admin
#
#
# def has_module_perm(self,applabel):
#     return True


from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    RESTAURANT = 1
    CUSTOMER = 2  # Исправил дублирующийся идентификатор
    ROLE_CHOICES = (
        (RESTAURANT, 'Restaurant'),
        (CUSTOMER, 'Customer'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, max_length=100)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Исправил название и установил автоустановку
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    # created_at = models.DateTimeField(null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_admin = models.BooleanField(default=False, blank=True, null=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)  # Обычно пользователь активен по умолчанию
    is_superadmin = models.BooleanField(default=False, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Исправил ошибку "emaill"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True