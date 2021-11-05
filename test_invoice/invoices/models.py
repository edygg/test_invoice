from django.db import models


class Invoice(models.Model):
    REFERS_TO_CHOICES = (
        ('PERSONA_NATURAL', 'Persona Natural'),
        ('PERSONA_JURIDICA', 'Persona Juridica'),
    )

    client_name = models.CharField(max_length=150)
    client_address = models.TextField()
    refers_to = models.CharField(max_length=100, choices=REFERS_TO_CHOICES)

    class Meta:
        ordering = ["client_name"]
