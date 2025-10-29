from django.db import models
from django.contrib.auth.models import User

positions = {
    'admin': 'Admin',
    'teacher': 'Teacher',
    'student': 'Student',
    'user': 'User',
}

country_codes = {
    '+93': 'Afghanistan',
    '+355': 'Albania',
    '+213': 'Algeria',
    '+54': 'Argentina',
    '+374': 'Armenia',
    '+61': 'Australia',
    '+43': 'Austria',
    '+994': 'Azerbaijan',
    '+880': 'Bangladesh',
    '+375': 'Belarus',
    '+32': 'Belgium',
    '+55': 'Brazil',
    '+359': 'Bulgaria',
    '+1': 'United States / Canada',  # Both share +1
    '+86': 'China',
    '+420': 'Czech Republic',
    '+45': 'Denmark',
    '+20': 'Egypt',
    '+358': 'Finland',
    '+33': 'France',
    '+49': 'Germany',
    '+30': 'Greece',
    '+36': 'Hungary',
    '+91': 'India',
    '+62': 'Indonesia',
    '+98': 'Iran',
    '+964': 'Iraq',
    '+353': 'Ireland',
    '+39': 'Italy',
    '+81': 'Japan',
    '+7': 'Russia / Kazakhstan',  # Shared
    '+996': 'Kyrgyzstan',
    '+82': 'South Korea',
    '+60': 'Malaysia',
    '+52': 'Mexico',
    '+31': 'Netherlands',
    '+47': 'Norway',
    '+92': 'Pakistan',
    '+63': 'Philippines',
    '+48': 'Poland',
    '+351': 'Portugal',
    '+974': 'Qatar',
    '+40': 'Romania',
    '+966': 'Saudi Arabia',
    '+65': 'Singapore',
    '+27': 'South Africa',
    '+34': 'Spain',
    '+46': 'Sweden',
    '+41': 'Switzerland',
    '+90': 'Turkey',
    '+993': 'Turkmenistan',
    '+380': 'Ukraine',
    '+971': 'United Arab Emirates',
    '+44': 'United Kingdom',
    '+998': 'Uzbekistan'
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
