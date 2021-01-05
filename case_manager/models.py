from django.db import models


class Case(models.Model):
    court = models.CharField(max_length=3)
    defendant_name = models.CharField(max_length=30, blank=False)
    cause_number = models.CharField(max_length=7, primary_key=True)
    days_old = models.CharField(max_length=15)
    total_settings = models.CharField(max_length=3, blank=True)
    defendant_status = models.CharField(max_length=10)
    bail = models.CharField(max_length=10)
    bond_type = models.CharField(max_length=1, blank=True)
    next_setting_type = models.CharField(max_length=4, blank=False)
    defense_lawyer = models.CharField(max_length=30, blank=True)
    next_setting = models.DateField()
    charge = models.CharField(max_length=30, blank=False)
    felony_pending = models.BooleanField(blank=True, null=True)
    last_updated = models.DateField(auto_now=True)
    
    def next_appearance_required(self):
        required_appearances = ['JTRL', 'PTMO', 'ARRG']
        if self.next_setting_type in required_appearances:
            return True
        else:
            return False

class DataFile(models.Model):
    # Save raw data uploads for auditing
    # Added benefit of smaller files
    zipfile = models.FileField(upload_to='data-files/')
