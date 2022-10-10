from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    content = models.TextField(max_length=500, blank=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Messages'
        ordering = ['-created_on']

    def __str__(self):
        return self.name
