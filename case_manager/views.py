import csv

from django.shortcuts import render, get_list_or_404
from django.views.generic import DetailView
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from datetime import datetime, date, timedelta
from io import TextIOWrapper

from paper_pusher.models import CourtForm
from .forms import UploadFileForm, UploadDataFile, CaseSearchForm
from .models import Case, DataFile


def index(request):
    return render(request, 'case_manager/index.html')


def csv_to_model_obj(csvfile, model):
    csvfile = TextIOWrapper(csvfile, encoding='utf-8-sig')
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    # After reading ahead in the file, reset to beginning
    csvfile.seek(0)

    reader = csv.DictReader(csvfile, dialect=dialect)

    for row in reader:
        row['cm_ss_cda'] = datetime.strptime(row['cm_ss_cda'], '%m/%d/%Y')
        row['felony_pending_flag'] = bool(row['felony_pending_flag'])
        cm_cas = row['cm_cas']
        new_data = {
            'next_setting': row['cm_ss_cda'],
            'court': row['Textbox26'],
            'defendant_name': row['defname'],
            'defendant_status': row['textbox14'],
            'bail': row['Textbox35'],
            'bond_type': row['BondType'],
            'days_old': row['textbox13'],
            'total_settings': row['num_of_settings'],
            'defense_lawyer': row['atyname'],
            'next_setting_type': row['cm_ss_rea'],
            'charge': row['offense_description'],
            'felony_pending': row['felony_pending_flag'],
        }
        obj, created = Case.objects.update_or_create(
            cause_number=cm_cas, defaults=new_data)


# @login_required
def upload_court_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_to_model_obj(form.cleaned_data['file'], Case)
            messages.success(request, "File uploaded")
    else:
        form = UploadFileForm()

    return render(
        request, 'case_manager/upload.html', context={
            'form': form,
        })


def upload_data(request):
    if request.method == 'POST':
        form = UploadDataFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "File uploaded")
    else:
        form = UploadDataFile()
    
    recent_data_files = DataFile.objects.all()[:5]

    return render(
        request, 'case_manager/upload.html', 
        context={'form': form, 
        'recent_data_files': recent_data_files
        })

def case_search(request):
    if request.method == 'POST':
        form = CaseSearchForm(request.POST, request.FILES)
        if form.is_valid():
            defendant_name = str(form.cleaned_data['defendant_name']).upper()
            results = Case.objects.filter(
                defendant_name__startswith=defendant_name)[:25]
            return render(
                request,
                'case_manager/search.html',
                context={'results': results,
                         'form': form})
    else:
        form = CaseSearchForm()
        return render(
            request,
            'case_manager/search.html',
            context={'form': form,
                     'start': True})


class CaseDetail(DetailView):

    model = Case

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the available forms
        context['form_list'] = CourtForm.objects.all()
        return context


def docket(request):
    today_cases = get_list_or_404(Case, next_setting=date.today(), court='008')
    return render(
        request,
        'case_manager/search.html',
        context={'results': today_cases})
