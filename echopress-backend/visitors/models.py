from django.db import models

# Create your models here.
class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visitor {self.ip_address} at {self.visit_time}"
