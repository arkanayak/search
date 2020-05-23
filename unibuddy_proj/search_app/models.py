from django.db import models

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    count_words = models.IntegerField(default = 0)

class Word(models.Model):
    w = models.CharField(max_length=100, primary_key=True, db_index=True)

class Freq(models.Model):
    word = models.ManyToManyField(Word, related_name='freqw')
    book = models.ManyToManyField(Book, related_name='freqb')
    count =  models.IntegerField(default = 0)

