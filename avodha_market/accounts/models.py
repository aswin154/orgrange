from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class SiteSettings(models.Model):
    name = models.CharField(max_length=100, default="Site Settings")
    allow_registration = models.BooleanField("Allow Registration", default=False)
    allow_user_products = models.BooleanField("Allow User Upload", default=False)

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError("Only one site settings object is allowed.")

        super(SiteSettings, self).save(*args, **kwargs)

    def __str__(self):
        return f"Site Settings"

    class Meta:
        verbose_name_plural = "Site Settings"
