from django.test import TestCase
from datetime import date, timedelta

from .models import Case

tomorrow = date.today() + timedelta(days=1)


class CaseCreationTestCase(TestCase):

    def setUp(self):
        Case.objects.create(cause_number='1234567',
                            court='1',
                            next_setting=tomorrow,
                            next_setting_type='ARRG')

    def test_cause_number_exists(self):
        case = Case.objects.get(cause_number='1234567')
        self.assertEqual(case.cause_number, '1234567')
        self.assertEqual(case.court, '1')
        self.assertEqual(case.next_setting, tomorrow)
        self.assertEqual(case.next_setting_type, 'ARRG')
