from django.db import models

# Create your models here.

from datetime import date
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User #Blog author or commenter



def attachment_path(instance, filename):
    return "animal/" + str(instance.animal.id) + "/attachments/" + filename

""" Metoda vrací cestu k uploadovanému plakátu. """

def poster_path(instance, filename):
    return "animals/" + str(instance.id)  + filename


class Type(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Type of animal", help_text='Enter a type of animal (e.g. Savec)')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name







class Animal(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Name of animal")
    poster = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Poster")
    type = models.ManyToManyField(Type, help_text='Select a type for this animal')

    # Metadata
    class Meta:
        ordering = ["name"]

    # Methods
    def __str__(self):
        """Součástí textové reprezentace filmu bude jeho název, rok uvedení a hodnocení"""
        return f"{self.name}, year: {str(self.poster)}, rate: {str(self.type)}"

    def get_absolute_url(self):
        """Metoda vrací URL stránky, na které se vypisují podrobné informace o filmu"""
        return reverse('film-detail', args=[str(self.id)])



class Attachment(models.Model):
    # Fields
    # Povinný titulek přílohy - text do délky 200 znaků
    title = models.CharField(max_length=200, verbose_name="Title")
    # Časový údaj o poslední aktualizaci přílohy - automaticky se ukládá aktuální čas
    last_update = models.DateTimeField(auto_now=True)
    # Pole pro upload souboru
    # Parametr upload_to zajistí uložení souboru do složky specifikované v návratové hodnotě metody attachment_path
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")

    # Konstanta, v níž jsou ve formě n-tic (tuples) předdefinovány různé typy příloh
    TYPE_OF_ATTACHMENT = (
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('text', 'Text'),
        ('video', 'Video'),
        ('other', 'Other'),
    )

    # Pole s definovanými předvolbami pro uložení typu přílohy
    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True, default='image',
                            help_text='Select allowed attachment type', verbose_name="Attachment type")
    # Cizí klíč, který zajišťuje propojení přílohy s daným filmem (vztah N:1)
    # Parametr on_delete slouží k zajištění tzv. referenční integrity - v případě odstranění filmu
    # budou odstraněny i všechny jeho přílohy (models.CASCADE)
    film = models.ForeignKey(Animal, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        # Primární seřazeno podle poslední aktualizace souborů, sekundárně podle typu přílohy
        ordering = ["-last_update", "type"]

    # Methods
    def __str__(self):
        """ Textová reprezentace objektu """
        return f"{self.title}, ({self.type})"