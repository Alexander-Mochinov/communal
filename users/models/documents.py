from django.db import models

class UserDocuments(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
    )
    path_to_file = models.FileField()
    name = models.CharField(max_length=255)
