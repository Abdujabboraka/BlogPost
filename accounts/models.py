from django.db import models
from django.contrib.auth.models import User

positions = {
    'admin': 'Admin',
    'teacher': 'Teacher',
    'student': 'Student',
    'user': 'User',
}

country_codes = {
    'Afghanistan': '+93',
    'Albania': '+355',
    'Algeria': '+213',
    'Argentina': '+54',
    'Armenia': '+374',
    'Australia': '+61',
    'Austria': '+43',
    'Azerbaijan': '+994',
    'Bangladesh': '+880',
    'Belarus': '+375',
    'Belgium': '+32',
    'Brazil': '+55',
    'Bulgaria': '+359',
    'Canada': '+1',
    'China': '+86',
    'Czech Republic': '+420',
    'Denmark': '+45',
    'Egypt': '+20',
    'Finland': '+358',
    'France': '+33',
    'Germany': '+49',
    'Greece': '+30',
    'Hungary': '+36',
    'India': '+91',
    'Indonesia': '+62',
    'Iran': '+98',
    'Iraq': '+964',
    'Ireland': '+353',
    'Italy': '+39',
    'Japan': '+81',
    'Kazakhstan': '+7',
    'Kyrgyzstan': '+996',
    'South Korea': '+82',
    'Malaysia': '+60',
    'Mexico': '+52',
    'Netherlands': '+31',
    'Norway': '+47',
    'Pakistan': '+92',
    'Philippines': '+63',
    'Poland': '+48',
    'Portugal': '+351',
    'Qatar': '+974',
    'Romania': '+40',
    'Russia': '+7',
    'Saudi Arabia': '+966',
    'Singapore': '+65',
    'South Africa': '+27',
    'Spain': '+34',
    'Sweden': '+46',
    'Switzerland': '+41',
    'Turkey': '+90',
    'Turkmenistan': '+993',
    'Ukraine': '+380',
    'United Arab Emirates': '+971',
    'United Kingdom': '+44',
    'United States': '+1',
    'Uzbekistan': '+998'
}


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    position = models.CharField(max_length=10, choices=[(k, v) for k, v in positions.items()], default='user')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=250)
    country_code = models.CharField(max_length=20, choices=[(k, v) for k, v in country_codes.items()], default='Uzb')
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
