from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class TechCategory(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)
    class Meta:
        verbose_name_plural = "Tech Categories"
    def __str__(self):
        return f"{self.name}"

class Tech(models.Model):
    title = models.CharField (max_length= 100, default="")
    description = models.TextField ()
    category = models.ForeignKey(TechCategory, on_delete=models.CASCADE,related_name='tech_items')
    slug = models.SlugField (
        default="",
        null= False
    )
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url (self):
        return reverse("tech-detail", args=[self.slug])
    def __str__(self):
        return f"{self.title}"
