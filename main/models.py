from django.db import models
from django.utils import timezone


# Create your models here.
class UserProfile(models.Model):
    uid = models.CharField(max_length=20, primary_key=True)
    fb_name = models.CharField(max_length=10000, default="")

    is_in_queue = models.BooleanField(default=False)
    is_in_chat = models.BooleanField(default=False)

    is_graduated = models.BooleanField(default=False)
    is_male = models.BooleanField(default=True)
    looking_for_choices = [
        ('m', 'Nam'),
        ('f', 'Nữ'),
        ('a', 'Bất kỳ'),
    ]

    gender_wanted = models.CharField(max_length=1,
                                     choices=looking_for_choices,
                                     default='a')
    # graduation_wanted = models.BooleanField(default=True)


class Chat(models.Model):
    sender = models.ForeignKey(UserProfile,
                               on_delete=models.CASCADE,
                               related_name='chats_as_user1')
    receiver = models.ForeignKey(UserProfile,
                                 on_delete=models.CASCADE,
                                 related_name='chats_as_user2')
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
