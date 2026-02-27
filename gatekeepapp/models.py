from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('resident', 'Resident'),
        ('guard', 'Guard'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
    

class Apartment(models.Model):
    building_name = models.CharField(max_length=100)
    flat_number = models.CharField(max_length=10)

    resident = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'resident'}
    )

    def __str__(self):
        return f"{self.building_name} - {self.flat_number}"
    

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    id_proof_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
    

class Visit(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)

    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role': 'resident'}
    )

    entry_granted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='guard_entries',
        limit_choices_to={'role': 'guard'}
    )

    status = models.CharField(
        max_length=20,
        choices=(
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('denied', 'Denied'),
            ('checked_out', 'Checked Out'),
        ),
        default='pending'
    )

    def __str__(self):
        return f"{self.visitor.name} → {self.apartment}"
    

