from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    CATEGORY = (
        ('Apple', 'APPLE'),
        ('Samsung', 'Samsung'),
        ('Huawei', 'Huawei'),
        ('Xiaomi', 'Xiaomi'),
        ('Oppo', 'Oppo'),
        ('Vivo', 'Vivo'),
        ('Realme', 'Realme'),
        ('Oneplus', 'Oneplus'),
        ('Google', 'Google'),
        ('Nokia', 'Nokia'),
        ('Sony', 'Sony'),
        ('LG', 'LG'),
        ('HTC', 'HTC'),
        ('Motorola', 'Motorola'),
        ('Lenovo', 'Lenovo'),
        ('Asus', 'Asus'),
        ('ZTE', 'ZTE'),
        ('Alcatel', 'Alcatel'),
        ('Tecno', 'Tecno'),
        ('Infinix', 'Infinix'),
        ('Itel', 'Itel'),
        ('Gionee', 'Gionee'),
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    category = models.CharField(max_length=15, choices=CATEGORY, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField()
    colour = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    sim = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    features = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            num = 1
            if Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)