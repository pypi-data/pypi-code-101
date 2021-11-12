from __future__ import annotations

from django.db import models
from django.db.models import Q


class Directory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    dns_name = models.CharField('Domain name',
                                max_length=100, null=True, blank=True)
    short_name = models.CharField('Domain name (pre-Windows 2000)',
                                  max_length=100, null=True, blank=True)
    dn = models.CharField(max_length=100)
    dc = models.GenericIPAddressField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    ldaps = models.BooleanField(default=False)

    def __str__(self):
        return self.dn

    class Meta:
        # verbose_name = 'Directory'
        verbose_name_plural = 'directories'

    @staticmethod
    def find_directory(name: str) -> Directory:
        return Directory.objects.get(
            Q(dns_name__iexact=name) |
            Q(name__iexact=name) |
            Q(short_name__iexact=name)
        )
