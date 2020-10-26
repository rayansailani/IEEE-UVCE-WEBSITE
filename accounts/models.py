from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, membership_no, is_sig_head, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Email")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            membership_no=membership_no,
            is_sig_head=is_sig_head
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, is_sig_head, membership_no, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            membership_no=membership_no,
            is_sig_head=is_sig_head
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_sig_head = models.BooleanField(default=False)
    membership_no = models.CharField(null=True,
                                     blank=True, default=" ", max_length=8)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'membership_no', 'is_sig_head']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

        # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

        # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
