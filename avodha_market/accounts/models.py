
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class SiteSettings(models.Model):
    disable_registration = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError("Only one site settings object is allowed.")

        super(SiteSettings, self).save(*args, **kwargs)

    def __str__(self):
        return f"Site Settings"

    class Meta:
        verbose_name_plural = "Site Settings"
