import cv2
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .detection_status import face_detection_status
from .selfie_segmentation import face_segmentation


@csrf_exempt
def detect(request):

    response, flag = token_authentication(request)
    print("#############")
    print(response)
    print(flag)
    print("############")
    if not flag:
        # here the health check endpoint will fall
        return JsonResponse(response)
    if response:
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
                return JsonResponse(json_data)
        else:
            json_data = dict()
            message = "Health Check End Point"
            json_data["message"] = message
            return JsonResponse(json_data)

    else:
        json_data = dict()
        message = "Token Authentication Failed"
        json_data["message"] = message
        return JsonResponse(json_data, status=400)


def token_authentication(request):
    """
    the key for the auth has been defined as "Authorization" and it value has been set as
    XYZ. Which can be changed later on
    """

    if 'Authorization' not in request.headers:
        json_data = dict()

        json_data["Successful"] = False
        message = "Token has not been provided in request header"
        json_data["message"] = message
        json_data["base64"] = None
        flag = False
        # Here the application health check end point will fall.
        return json_data, flag
    try:

        our_defined_token = "XYZ"
        auth_token = request.headers['Authorization']
        if auth_token == our_defined_token:
            # here the authentication token will be tested, which will be sent with API
            response = True
            response = (response.__bool__())
            flag = True
            return response, flag
        else:
            return False, True

    except Exception as e:
        return False, False

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
