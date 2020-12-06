from django.db import models
from PIL import Image

# Create your models here.
class projects(models.Model):
    p_title = models.CharField(max_length=150, blank=False)
    p_image = models.ImageField(default='default-image.png', upload_to='projects')
    location = models.CharField(max_length=100, blank=False)

    def save(self, *args, **kwargs):
        super(projects, self).save(*args, **kwargs)

        img = Image.open(self.p_image.path)

        if img.height > 300 or img.width >300:
            output_size =(img.height, img.width)
            img.thumbnail(output_size)
            img.save(self.p_image.path)