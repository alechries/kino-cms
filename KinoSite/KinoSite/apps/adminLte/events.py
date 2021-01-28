import os
import uuid
from django.db import models
from django.dispatch import receiver
from . import services


@receiver(models.signals.post_delete, sender=models.Model)
def delete_file_on_delete(instance, *args, **kwargs):
    for file in instance.file_list():
        if file:
            services.delete_file_with_instance(file.path)