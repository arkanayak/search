import math
from django.conf import settings
import json
import requests
from search_app.models import *


def search(search_term, k):
    total_books = Book.objects.all().count()
    search_term_list = search_term.strip().lower().split()

    res_book_dict = {}
    for term in search_term_list:
        freq_obj = Freq.objects.filter(word__w=term)
        for item in freq_obj:
            word_occ_book = item.count

            books = item.book.all()
            book_id = books[0].book_id
            """ get total words in the book summary """
            total_words_book = books[0].count_words

            """ calculate tf-idf value for a word against a book summary """
            tf_idf = (word_occ_book / total_words_book) * math.log((total_books / (freq_obj.count() + 1)), 10)

            """ Relevance of match is calculated based on summation of calculated tf-idf value for each book id """
            if not res_book_dict.get(book_id, None):
                res_book_dict[book_id] = tf_idf
            else:
                res_book_dict[book_id] += tf_idf

    """ sort the dictionary (key: book_id) based on values (tf-idf) """
    results = sorted(res_book_dict.items(), key=lambda kv: (-1 * kv[1]))
    old_res = results[:k]

    final_res = []
    for item in old_res:
        """ append summary to the result list """
        book_id = item[0]
        mapping_file = settings.BASE_DIR + '/search_app/input/data.json'
        f = open(mapping_file, 'r')
        data = (json.load(f, encoding="utf-8"))

        summaries = data['summaries']
        summary = summaries[book_id]
        final_res.append(summary)
    return final_res


def get_author_api(book_id):
    """ returns the author for a book_id"""
    url = settings.BOOK_API
    data = {"book_id": book_id}
    r = requests.post(url=url, json=data)
    res = r.json()
    return res
