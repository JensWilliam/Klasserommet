from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} Profile"



class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200) # Navn på rommet
    description = models.TextField(null=True, blank=True) # Beskrivelse av rommet
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) # Når rommet ble oppdatert
    created = models.DateTimeField(auto_now_add=True) # Når rommet ble opprettet


    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
 
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Brukeren som sendte meldingen
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # Rommet meldingen ble sendt i
    body = models.TextField() # Innholdet i meldingen
    updated = models.DateTimeField(auto_now=True) # Når meldingen ble oppdatert
    created = models.DateTimeField(auto_now_add=True) # Når meldingen ble opprettet

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]