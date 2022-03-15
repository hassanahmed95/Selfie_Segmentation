# importing all necessary packages. . . .
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


@csrf_exempt
def health(request):
    if request.method == "GET":
        jsondata = dict()
        digi_ocr_ev = "http://localhost:8000/"
        url = digi_ocr_ev+'face_segmentation/detect'
        response = requests.post(url)
        response = response.status_code
        if response == 200:
            jsondata["http status"] = response
            jsondata["status"] = "UP"
            return JsonResponse(jsondata)
        else:
            jsondata["http status"] = response
            jsondata["status"] = "DOWN"
            return JsonResponse(jsondata)
