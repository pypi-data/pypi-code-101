from django.db import models


class ExampleModel(models.Model):
    first_name = models.CharField("Name", max_length=255)
