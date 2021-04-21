from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Document(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="User", null=True
    )
    date_created = models.DateTimeField(
        "Date Created", auto_now=True, null=False, blank=False
    )
    text = models.CharField("Document Text", max_length=100_000)