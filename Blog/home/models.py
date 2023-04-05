from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.utils.text import slugify
import uuid
# email verfication start here
from django.db.models.signals import post_save
from django.dispatch import receiver
from home.helpers import send_account_activation_email


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    profile_img = models.ImageField( upload_to='profile')
    
#  email verification continues here 
@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance, email_token = email_token)
            email = instance.email
            send_account_activation_email(email, email_token)
    except Exception as e:
        print(e)

    





class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)


  

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while BlogModel.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug


    def save(self , *args , **kwargs):
        if not self.slug:
           self.slug = self._get_unique_slug()
        super().save(*args , **kwargs)


    def __str__(self) -> str:
        return self.title