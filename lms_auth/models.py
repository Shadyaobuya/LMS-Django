# Create your models here.

from django.db import models
from lms_auth.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import Group, Permission


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("student", "Student"),
        ("admin", "Admin"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    username = models.CharField(
        max_length=150,
        help_text="Required. 150 characters or fewer. Letters, digits, and spaces only.",
        null=True,
        blank=True,
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    objects = CustomUserManager()

    def is_student(self):
        return self.role == "student"

    def is_admin(self):
        return self.role == "admin"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.email}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["username"], name="unique-username-field")
        ]
        permissions = (
            ("is_student", "Can view student app"),
            ("is_admin", "Can view admin app"),  # Updated to match role names
        )


class ModificationTrackingModel(models.Model):
    created_by = models.CharField(
        null=True,
        blank=True,
        help_text="User who created record",
        max_length=30,
        db_comment="User who created record",
    )
    modified_by = models.CharField(
        null=True,
        blank=True,
        help_text="User who modified record",
        max_length=30,
        db_comment="User who modified record",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Time record was created",
        max_length=30,
        null=True,
        db_comment="Time record was created",
    )

    modified_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Time record was modified",
        max_length=30,
        null=True,
        db_comment="Time record was modified",
    )

    class Meta:
        abstract = True


class Gender(models.TextChoices):
    FEMALE = "Female"
    MALE = "Male"
    UNKNOWN = "Unknown"
