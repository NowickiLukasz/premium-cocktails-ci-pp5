from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(max_length=100, blank=False)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.email
