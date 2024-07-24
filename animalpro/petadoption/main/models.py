from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    temperament = models.CharField(max_length=100)
    medical_history = models.TextField()
    image = models.ImageField(upload_to='pet_images/')

class AdoptionApplication(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=50, choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')))
