from django.db import models


class Resume(models.Model):
    file = models.FileField(upload_to='static/resume')
    date_added = models.DateTimeField(auto_now_add=True)
    