import math
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
            total_words_book = books[0].count_words

            tf_idf = (word_occ_book/total_words_book) * math.log((total_books//freq_obj.count()+1),10)

            if not res_book_dict.get(book_id, None):
                res_book_dict[book_id] = tf_idf
            else:
                res_book_dict[book_id] += tf_idf

    results = sorted(res_book_dict.items(), key=lambda kv: (-1*kv[1]))
    return results[:k]
