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
        freq_obj = FreqIndex.objects.filter(word__text=term)
        for item in freq_obj:
            word_occ_book = item.count_words

            books = item.book.all()
            book_id = books[0].id
            """ get total words in the book summary """
            total_words_book = books[0].words_count

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
        query_dict = {}
        book_id = item[0]
        # mapping_file = settings.BASE_DIR + '/search_app/input/data.json'
        # f = open(mapping_file, 'r')
        # data = (json.load(f, encoding="utf-8"))
        #
        # summaries = data['summaries']
        # summary = summaries[book_id]
        summary = Book.objects.get(id=book_id).summary
        query_dict['id'] = book_id
        query_dict['summary'] = summary
        final_res.append(query_dict)
    return final_res


def get_author_api(book_id):
    """ returns the author for a book_id"""
    url = settings.BOOK_API
    data = {"book_id": book_id}
    r = requests.post(url=url, json=data)
    res = r.json()
    return res
