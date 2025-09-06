import uuid
import os
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

def ficha_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{slugify(instance.name)}-{uuid.uuid4().hex}.{ext}"
    return os.path.join('items', str(instance.pk or 'temp'), filename)

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ImageField(
        upload_to=None, 
        height_field=None, 
        width_field=None, 
        max_length=None
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})
