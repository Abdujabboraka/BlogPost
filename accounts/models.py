from django.db import models
from django.contrib.auth.models import User

positions = {
    'admin': 'Admin',
    'teacher': 'Teacher',
    'student': 'Student',
    'user': 'User',
}

country_codes = {
    'Uzb': '+998',
    'US': '+1',
    'IN': '+91',
}

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    position = models.CharField(max_length=10, choices=[(k, v) for k, v in positions.items()], default='user')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    address = models.CharField(max_length=250)
    country_code = models.CharField(max_length=10, choices=[(k, v) for k, v in country_codes.items()], default='Uzb')
    phone = models.IntegerField()

    def save(self, *args, **kwargs):
        # Create user only if it doesn’t exist yet
        if not self.user:
            user = User.objects.create_user(
                username=self.email.split('@')[0],  # simple username
                email=self.email,
                first_name=self.first_name,
                last_name=self.last_name,
                password='default123'  # you can replace this
            )
            self.user = user
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
