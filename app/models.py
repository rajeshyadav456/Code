from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
# # Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)

@receiver(post_save, sender=Post)
def send_notification_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Post Created'
        message = f'Your post "{instance.title}" has been successfully created.'
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.author.email]
        send_mail(subject, message, from_email, to_email)