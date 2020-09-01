from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    """
    Model representing a film genre .
    """
    name = models.CharField(max_length=200, help_text="Enter a film genre (e.g. Horror, Comedy etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Film(models.Model):
    """
    Model representing a film (but not a specific copy of a film).
    """
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the film")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this film")
    avatar = models.CharField(max_length=100, default="default.png", help_text="Enter name of image of your film")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_img_path(self):
        """
        Returns the path of film image for preview.
        """
        return '/static/img/' + self.avatar
    
    def get_short_summary(self):
        """
        Returns the short summary of film for preview.
        """
        return (self.summary[:75]) + '...' if len(self.summary) > 75 else self.summary

    def get_absolute_url(self):
        """
        Returns the url to access a particular film instance.
        """
        return reverse('film-detail', args=[str(self.id)])

class FilmInstance(models.Model):
    """
    Model representing a specific copy of a film (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular film across whole library")
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    session_time = models.DateField(null=False, blank=False)

    LOAN_STATUS = (
        ('s', 'Sold'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=25, choices=LOAN_STATUS, blank=True, default='m', help_text='Film availability')

    class Meta:
        ordering = ["session_time"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (Availability: %s) %s (%s)' % (self.film, self.status, self.id ,self.film.title)

class Director(models.Model):
    """
    Model representing an director.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    photo = models.CharField(max_length=100, default="default.png", help_text="Enter name of image of your director")

    def get_img_path(self):
        """
        Returns the path of film image for preview.
        """
        return '/static/img/directors/' + self.photo

    def get_absolute_url(self):
        """
        Returns the url to access a particular director instance.
        """
        return reverse('director-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)            