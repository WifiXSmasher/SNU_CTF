from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Subscription(models.Model):

    subscription_choice = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = _("Subscription")
        verbose_name_plural = _("Subscriptions")

    def __str__(self):
        return f"user :{self.user.username} is {"Subscribed" if self.subscription_choice else "UnSubscribed"}"
    

    def get_notification_email(self):
        """Get the email address to send notifications to"""
        return self.user.email

    #to check if the user is subscribed
    def is_subscribed(self):
        return self.subscription_choice
    
    @classmethod
    def get_or_create_for_user(cls, user):
        """utility method to get or create subscription for a user"""
        
        subscription, created = cls.objects.get_or_create(
            user=user,
            defaults={'subscription_choice': False}
        )
        return subscription, created
