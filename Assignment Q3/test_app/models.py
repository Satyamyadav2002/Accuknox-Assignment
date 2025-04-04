from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    is_processed = models.BooleanField(default=False)

@receiver(post_save, sender=TestModel)
def process_test_model(sender, instance, created, **kwargs):
    # This signal handler will raise an exception
    if created:
        # This will cause a rollback if in the same transaction
        raise Exception("Signal handler exception") 