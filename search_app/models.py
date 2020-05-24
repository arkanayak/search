from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    words_count = models.IntegerField(default=0)
    summary = models.TextField(blank=True, null=True)


class Word(models.Model):
    text = models.CharField(max_length=100, primary_key=True, db_index=True)


class FreqIndex(models.Model):
    word = models.ManyToManyField(Word, related_name='freqw')
    book = models.ManyToManyField(Book, related_name='freqb')
    count_words = models.IntegerField(default=0)
