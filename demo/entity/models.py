from django.db import models


class Entity(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_images(self):
        return Images.objects.values_list('image', flat=True).filter(
            entity=self)


class Images(models.Model):
    entity = models.ForeignKey(Entity)
    image = models.ImageField(upload_to='images')
