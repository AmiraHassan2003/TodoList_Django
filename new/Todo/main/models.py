from django.db import models

class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now = True)

# Create your models here.
