from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from utils.process_data import process
import json

@csrf_exempt
def preprocess(request):
    result = process()
    return JsonResponse({"result" : result})
