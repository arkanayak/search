from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from utils.process_data import process
from utils.search_query import search, get_author_api
import json


@csrf_exempt
def preprocess(request):
    """ preprocess and create all the data required for faster future querying"""
    result = process()
    return JsonResponse({"result": result})


@csrf_exempt
def search_queries(request):
    """ take input: list of queries and k, and return a list of k matching results for each query"""
    post_body = json.loads(request.body.decode('utf-8'))
    list_queries = post_body.get("queries", None)
    k = post_body.get("k", None)

    final_res = []
    if not list_queries and not k:
        return JsonResponse({"error": "invalid input/s"})
    else:
        """ add author and query to response"""
        for item in list_queries:
            temp_res = search(item, k)
            for j in temp_res:
                book_id = j['id']
                author = get_author_api(book_id)
                j['author'] = author
                j['query'] = item
            final_res.append(temp_res)

    return JsonResponse({"result": final_res})
