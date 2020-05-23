from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from utils.process_data import process
from utils.search_query import search
import json

@csrf_exempt
def preprocess(request):
    # result = process()
    result = search("is your problems", 3)

    return JsonResponse({"result" : result})
