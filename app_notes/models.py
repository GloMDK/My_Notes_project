from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='app_notes/images/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.title
