from django.db import models

class Csat_filtred_phones(models.Model):
    phone = models.CharField(max_length=15, null=False)
    created_by = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    creation_reason = models.TextField(max_length=255, null=False, blank=False, default='')
    is_deactivated = models.BooleanField(default=False, blank=True)
    deactivated_by = models.CharField(max_length=30, null=True, default=None, blank=True)
    deactivated_at = models.DateTimeField(null=True, default=None, blank=True)
    deactivation_reason = models.TextField(max_length=255, null=True, blank=True, default='')