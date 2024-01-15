from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def resume(request):
    print(os.listdir())
    with open('./pages/FM_RESUME.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=FM_RESUME.pdf'
        return response