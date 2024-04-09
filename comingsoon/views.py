from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import get_object_or_404, HttpResponse
from .models import PDF

def home(request):
    context = {}
    template = 'comingsoon/home.html'
    return render(request, template, context)

def pdf_list(request):
    pdfs = PDF.objects.all()
    return render(request, 'comingsoon/pdf_list.html', {'pdfs': pdfs})

def serve_pdf(request, pdf_id):
    pdf = get_object_or_404(PDF, id=pdf_id)
    # Optionally, you can add permission checks here to ensure the user has access to the PDF
    with open(pdf.pdf_file.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=' + pdf.pdf_file.name
        return response