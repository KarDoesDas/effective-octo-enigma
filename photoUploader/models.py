from django.db import models
from django.conf import settings
import uuid

# Create your models here.
def photos_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/preke/<uuid>_<filename>
    return 'photos/{0}_{1}'.format(str(uuid.uuid4()), filename)

class Photo(models.Model):
    date = models.DateTimeField(verbose_name="Date", auto_now=False, auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    photo_file = models.FileField(verbose_name="Photo File", upload_to=photos_path)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self):
        return f"{self.user}"