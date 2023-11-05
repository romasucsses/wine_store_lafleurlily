from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone

from orders.models import Checkout
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError('The Email must to have')

        if not username:
            username = email

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, username, **extra_fields)

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, username, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=355)
    name = models.CharField(max_length=155, null=True)
    last_name = models.CharField(max_length=155, null=True)
    display_name = models.CharField(max_length=255, default=username)
    orders = models.ForeignKey(Checkout, on_delete=models.PROTECT, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255)
    street_address_1 = models.TextField()
    street_address_2 = models.TextField(null=True)
    city = models.CharField(max_length=155)
    state = models.CharField(max_length=155)
    zip_code = models.CharField(max_length=155)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    account = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



# class HistoryOrders(models.Model):
#     account = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
#     order = models.ForeignKey(Checkout, on_delete=models.PROTECT, null=True)
