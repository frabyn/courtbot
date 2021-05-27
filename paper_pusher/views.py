from tempfile import NamedTemporaryFile

from django.http import FileResponse
from django.views.generic.list import ListView

from mailmerge import MailMerge

from case_manager.models import Case
from paper_pusher.models import CourtForm


def generate_form(request, case_pk, form_pk):
    template = CourtForm.objects.get(pk=form_pk)
    case_data = Case.objects.get(pk=case_pk)
    fields = {
        "court": case_data.court,
        "case": case_data.cause_number,
        "def_name": case_data.defendant_name,
    }
    finished_name = fields["case"] + "-" + "affidavit" + ".docx"

    with MailMerge(template.upload) as document:
        document.merge(**fields)
        file = NamedTemporaryFile()
        document.write(file.name)
        response = FileResponse(file, as_attachment=True, filename=finished_name)
        return response


class BlankFormList(ListView):

    model = CourtForm


def download_blank(request, form_pk):
    template = CourtForm.objects.get(pk=form_pk)
    response = FileResponse(template.upload, as_attachment=True)
    return response
