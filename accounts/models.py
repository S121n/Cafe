from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


######################################
# pain_mostafa
######################################
class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone_number, **extra_fields):
        if not phone_number:
            raise ValueError('Mobile number is required.')
        user = self.model(username=username, phone_number=phone_number, **extra_fields)
        user.set_password(phone_number)  # mobile number as password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('role', 'manager')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.create_user(username, phone_number, **extra_fields)
        user.set_password(password)  # superuser password
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('employee', 'Employee'),
        ('manager', 'Manager'),
    )

    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'  # login by phone number
    REQUIRED_FIELDS = ['username']  # for creat superuser

    def __str__(self):
        return f"{self.username} ({self.phone_number})"
