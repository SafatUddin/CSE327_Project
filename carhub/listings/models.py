from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    # 1. DROPDOWN OPTIONS
    # These lists limit what users can select, preventing typos.
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]
    
    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]
    
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Used', 'Used'),
    ]

    # 2. BASIC INFO
    # ForeignKey links this car to a specific User (the seller).
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) 
    price = models.IntegerField()
    
    # 3. CAR SPECS
    year = models.IntegerField()
    mileage = models.IntegerField()
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='Used')
    
    # 4. FEATURES CHECKLIST
    # We use Booleans (True/False) for features. This makes them easy to filter.
    features_backup_camera = models.BooleanField(default=False, verbose_name="Backup Camera")
    features_bluetooth = models.BooleanField(default=False, verbose_name="Bluetooth")
    features_cruise_control = models.BooleanField(default=False, verbose_name="Cruise Control")
    features_gps = models.BooleanField(default=False, verbose_name="GPS / Navigation")
    features_sunroof = models.BooleanField(default=False, verbose_name="Sunroof")
    
    # 5. DESCRIPTION & IMAGES
    description = models.TextField()
    # 'upload_to' organizes photos by date (e.g., photos/2025/03/15/)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    # 6. ADMIN STUFF
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title