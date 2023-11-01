from django.db import models

# Create your models here.
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    tech_skills = models.CharField(max_length=100)  # You can use a CharField for storing skills.

    def __str__(self):
        return self.name
