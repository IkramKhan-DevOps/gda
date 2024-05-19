from django.db import models


class Contact(models.Model):
    SUBJECT_CHOICE = [
        ('restaurants', 'Restaurants'),
        ('tenders', 'Tenders'),
        ('technical', 'Technical'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICE)
    message = models.TextField()

    def __str__(self):
        return self.name
