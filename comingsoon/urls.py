from django.urls import path
from . import views

app_name = 'comingsoon'

urlpatterns = [
    path('', views.home, name='home'),
    path('pdfs/', views.pdf_list, name='pdf_list'),
    path('pdfs/<int:pdf_id>/', views.serve_pdf, name='serve_pdf'),
]


