from django.conf import settings
import json
from search_app.models import *


def process():
    stop_words = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
                  "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself",
                  "she", "her", "hers", "herself", "it", "its", "itself", "they", "them",
                  "their", "theirs", "themselves", "what", "which", "who", "whom", "this",
                  "that", "these", "those", "am", "is", "are", "was", "were", "be", "been",
                  "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a",
                  "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into",
                  "through", "during", "before", "after", "above", "below", "to", "from",
                  "up", "down", "in", "out", "on", "off", "over", "under", "again", "further",
                  "then", "once", "here", "there", "when", "where", "why", "how", "all", "any",
                  "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor",
                  "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can",
                  "will", "just", "don", "should", "now"}

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    mapping_file = settings.BASE_DIR + '/search_app/input/data.json'
    f = open(mapping_file, 'r')
    data = (json.load(f, encoding="utf-8"))

    summaries = data['summaries']
    for i in range(len(summaries)):
        raw_summary = summaries[i]['summary']
        summary = raw_summary.lower()

        for punc in punctuations:
            """ clean data: replace punctuations """
            summary = summary.replace(punc, "")

        book = Book(id=i, words_count=0, summary=raw_summary)
        book.save()

        words_list = summary.split(" ")
        stop_words_count = 0
        word_dict = {}
        for word in words_list:
            if word in stop_words:
                """ clean data: omit stop words"""
                stop_words_count += 1
                continue
            else:
                try:
                    word_obj = Word.objects.get(text=word)
                    word_dict[word] = word_dict[word] + 1
                except:
                    word_dict[word] = 1
                    word_obj = Word(text=word)
                    word_obj.save()

        book.words_count = len(words_list) - stop_words_count
        book.save()

        for word, freq in word_dict.items():
            """ create mapping b/w Freq object and Book and Word objects"""
            freq = FreqIndex(count_words=freq)
            freq.save()
            freq.word.add(Word.objects.get(text=word))
            freq.book.add(Book.objects.get(id=i))

        i += 1

    return "success"
