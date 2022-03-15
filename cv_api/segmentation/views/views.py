import cv2
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .detection_status import face_detection_status
from .selfie_segmentation import face_segmentation


@csrf_exempt
def detect(request):
    if request.method == "POST":
        if request.FILES.get("files", None) is not None:
            image = _grab_image(stream=request.FILES["files"])
            # here I have got the image file from the mobile application
            json_data, level = face_segmentation(image)
            if level == "INFO":
                return JsonResponse(json_data)
            else:
                return JsonResponse(json_data, status=400)
        else:
            message = "Some Error Occurred, Try Again"
            level = "ERROR"
            json_data = face_detection_status(message, level)
            return JsonResponse(json_data,status=200)
    else:
        json_data = dict()
        message = "Health Check End Point"
        json_data["message"] = message
        return JsonResponse(json_data)


def _grab_image(stream=None):
    """
    The following method is to get an image as input and
    to convert it into bytearray
    """

    if stream is not None:
        data = stream.read()
        data = np.asarray(bytearray(data), dtype="uint8")
        data = cv2.imdecode(data, cv2.IMREAD_COLOR)
        return data
