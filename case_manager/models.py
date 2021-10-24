from pyexpat import model
from re import T
from django.db import models
from datetime import date


# The Case model reflects data available via the
# "CCL Master Export" file at http://jdwprod/

# Notable shortcomings here: No attorney SPN field


class Case(models.Model):

    cases = models.Manager()

    setting_types = (
        ("JTRL", "Jury Trial"),
        ("PTMO", "Pre-trial Motions"),
        ("PTCR", "Pre-trial Conference"),
        ("ARRG", "Arraignment"),
        ("NTRL", "Non-trial Setting"),
        ("FELP", "Felony Pending"),
        ("DISM", "Dismissal Pending"),
        ("DPIH", "DWI PTI Application Pending"),
        ("PTIH", "PTI Application Pending"),
        ("DISP", "Disposition Conference"),
        ("NTRL", "Non-trial Conference"),
    )

    court = models.CharField(max_length=3)
    defendant_name = models.CharField(max_length=30, blank=False)
    cause_number = models.CharField(max_length=7, primary_key=True)
    days_old = models.CharField(max_length=15)
    total_settings = models.CharField(max_length=3, blank=True)
    defendant_status = models.CharField(max_length=10)
    bail = models.CharField(max_length=10)
    bond_type = models.CharField(max_length=1, blank=True)
    next_setting_type = models.CharField(
        max_length=4, blank=False, choices=setting_types
    )
    defense_lawyer = models.CharField(max_length=30, blank=True)
    next_setting = models.DateField()
    charge = models.CharField(max_length=30, blank=False)
    felony_pending = models.BooleanField(blank=True, null=True)
    last_updated = models.DateField(auto_now=True)

    def next_appearance_defendant(self):
        defendant_appearances = ["JTRL", "CTRL", "ARRG"]
        if self.next_setting_type in defendant_appearances:
            return True
        else:
            return False

    def next_appearance_attorney(self):
        attorney_appearances = ["DISP", "PTCR"]
        if self.next_setting_type in attorney_appearances:
            return True
        # If the defendant has to appear, so does the lawyer
        elif self.next_appearance_defendant() is True:
            return True
        else:
            return False

    def checkin_eligible(self):
        today = date.today()
        if self.next_setting == today:
            return True
        else:
            return False


class DataFile(models.Model):
    # Save raw data uploads for auditing
    # Added benefit of smaller files
    zipfile = models.FileField(upload_to="data-files/")

    files = models.Manager()


class CheckIn(models.Model):

    checkins = models.Manager()

    case = models.ForeignKey("Case", on_delete=models.CASCADE)

    roles = (
        ("Defendant"),
        ("Defense Attorney"),
        ("Prosecutor"),
    )

    ready_for_trial = models.BooleanField(blank=True, null=True)
    discovery_complete = models.BooleanField(blank=True, null=True)

    # Defendant Check-in Information
    #
    # As designed, the defendant is the only one to say whether they are in court
    # Assumed here is that attorneys will check in with court staff
    defendant_in_court = models.BooleanField(blank=True, null=True)
    defendant_rep_name = models.CharField(max_length=30, blank=True, null=True)
    defendant_phone = models.CharField(max_length=10, blank=True, null=True)

    # Defense Attorney Check-in Information
    defense_atty_phone = models.CharField(max_length=10, blank=True, null=True)
    defense_atty_sub_name = models.CharField(max_length=30, blank=True, null=True)
