from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    """Table of countries containing books."""
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        """For the special properties of table"""
        verbose_name_plural = "Countries"

class Address(models.Model):
    """Table for the address of author"""
    street = models.CharField(max_length=100,)
    pincode = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}"
    
    class Meta:
        """To add special features for address table"""
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    """Table for collecting authors name"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField("Address", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    """Create a table model named Book"""
    title = models.CharField(max_length=250)
    ranking = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True,
                               related_name="books")
    published_country = models.ManyToManyField("Country", null=True,related_name="books")
    is_famous = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        """provide a url for particular model"""
        return reverse("book_detail",args=[self.slug])
    
    def save(self,*args,**kwargs):
        """overwrite the model with slug value"""
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        """FOrmatting data that table will return"""
        return f"{self.title} ({self.ranking})"
