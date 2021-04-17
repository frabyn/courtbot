from django.db import models


class CourtForm(models.Model):
    upload = models.FileField(upload_to='court_forms/')
    form_number = models.CharField(
        max_length=3, blank=True, verbose_name='CCL Form Number')
    name = models.CharField(max_length=40, verbose_name='Form')

    forms = models.Manager()

    class Meta:
        verbose_name = 'Court Form'
