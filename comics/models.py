# -*- coding: utf-8 -*-
from django.db import models

#from search.models import SearchManager


class Artist(models.Model):
    """
    Ein Model des Künstlers mit Name, Beruf, Biografie, Photo und Website.
    """

    name = models.CharField(max_length=40, unique=True)
    profession = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='artistphoto')
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    """
    Ein Model einer Genre mit Name.
    """

    name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.name


class Publisher(models.Model):
    """
    Ein Model des Verlags mit Name, Information, Logo und Website.
    """

    name = models.CharField(max_length=40, unique=True)
    info = models.TextField(blank=True)
    logo = models.ImageField(blank=True, upload_to='logo')
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.name


class Kind(models.Model):
    """
    Ein Model eines Typs mit Name.
    """

    name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """
    Ein Model des Artikels mit Titel, Typ, Text, Autor,
    5 Bildfelder und Quelle-Link.
    """

    title = models.CharField(max_length=60)
    kind = models.ForeignKey(Kind)
    text = models.TextField(blank=True)
    writer = models.ManyToManyField(Artist)
  
    pic1 = models.ImageField(blank=True, upload_to='articlephoto')
    pic2 = models.ImageField(blank=True, upload_to='articlephoto')
    pic3 = models.ImageField(blank=True, upload_to='articlephoto')
    pic4 = models.ImageField(blank=True, upload_to='articlephoto')
    pic5 = models.ImageField(blank=True, upload_to='articlephoto')
    
    source = models.URLField(blank=True)

    def __unicode__(self):
        return self.title


class Comics(models.Model):
    """
    Ein Model des Comics mit Name, Genre, 
    Information, Autor, Künstler, Datum, Verlag, Artikel, 5 Bildfelder 
    und Website-Link.
    """

    name = models.CharField(max_length=60, unique=True)
    genre = models.ManyToManyField(Genre, blank=True)
    info = models.TextField(blank=True)
    
    writer = models.ManyToManyField(Artist, related_name='wr+')
    artist = models.ManyToManyField(Artist, related_name='ar+')
    letterer = models.ManyToManyField(Artist, blank=True, related_name='let+')
    colorist = models.ManyToManyField(Artist, blank=True, related_name='col+')
    inker = models.ManyToManyField(Artist, blank=True, related_name='ink+')
    penciller = models.ManyToManyField(Artist, blank=True, related_name='pen+')
    editor = models.ManyToManyField(Artist, blank=True, related_name='ed+')

    pub_date = models.DateField()
    publisher = models.ForeignKey(Publisher)
    article = models.ManyToManyField(Article, blank=True)
  
    pic1 = models.ImageField(blank=True, upload_to='comicsphoto')
    pic2 = models.ImageField(blank=True, upload_to='comicsphoto')
    pic3 = models.ImageField(blank=True, upload_to='comicsphoto')
    pic4 = models.ImageField(blank=True, upload_to='comicsphoto')
    pic5 = models.ImageField(blank=True, upload_to='comicsphoto')
    
    link = models.URLField(blank=True)

    #objects = SearchManager()

    def __unicode__(self):
        return self.name


