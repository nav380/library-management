from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_customer', False)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    # Role flags
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    # Additional user fields
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return self.username

    def clean(self):
        super().clean()

        # Ensure only one role flag is True at a time
        roles = [self.is_staff,  self.is_customer]
        if sum(roles) > 1:
            raise ValidationError("Only one of is_staff, is_superuser, or is_customer can be True.")
        
    def save(self, *args, **kwargs):
        # Validate constraints before saving
        self.full_clean()  # This calls the `clean()` method
        super().save(*args, **kwargs)


class userurlpermisson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    permission = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.url} - {self.permission}"
    