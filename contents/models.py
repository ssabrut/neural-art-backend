from django.db import models

# Create your models here.
class Content(models.Model):
  image = models.FileField(upload_to='images/contents')
  uploaded_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'contents'
    verbose_name = 'Content'
    verbose_name_plural = 'Contents'