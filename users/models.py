from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
import cloudinary.uploader
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, default="I love learning,it is a source of inspiration", blank=True)
    image = cloudinary.models.CloudinaryField('profile_pics')


    def save_profile(self):
        self.save()


    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # img = cloudinary.open(self.image.url)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.cloudinary.url)