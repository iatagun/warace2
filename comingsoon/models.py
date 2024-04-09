from django.db import models

from datetime import datetime, timedelta
from datetime import date

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)

class PDF(models.Model):
    title = models.CharField(
        max_length=200,  # Adjust max length as needed
        verbose_name='Title for PDFs',
        help_text='Enter an title for the associated PDF file.',
        blank=True,  # Depending on your requirements, you may want to allow this field to be optional
    )
    pdf_file = models.FileField(upload_to='comingsoon/media/pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    pdf_explanation = models.CharField(
        max_length=200,  # Adjust max length as needed
        verbose_name='Explanation for PDFs',
        help_text='Enter an explanation for the associated PDF file.',
        blank=True,  # Depending on your requirements, you may want to allow this field to be optional
    )

    def __str__(self):
        return self.title