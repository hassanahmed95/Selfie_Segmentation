from django.test import TestCase

# Create your tests here.

# # import the necessary packages
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# import numpy as np
# import urllib
# import cv2
# from passporteye import read_mrz
# import urllib.request
# from .MRZ_Extractor import MRZ
#
#
# @csrf_exempt
# def detect(request):
#     # initialize the data dictionary to be returned by the request
#     data = {"success": False}
#     # a = MRZ()
#     # print(a)
#
#     # check to see if this is a post request
#     if request.method == "POST":
#         # check to see if an image was uploaded
#         if request.FILES.get("image", None) is not None:
#             # grab the uploaded image
#             image = _grab_image(stream=request.FILES["image"])
#         # otherwise, assume that a URL was passed in
#         else:
#             # grab the URL from the request
#             url = request.POST.get("url", None)
#             print(url)
#             print("I am in the else condition of getting the URL . .. ")
#
#             # if the URL is None, then return an error
#             if url is None:
#                 data["error"] = "No URL provided."
#                 return JsonResponse(data)
#
#             # load the image and convert
#             image = _grab_image(url=url)
#             # print(type(image))
#             # cv2.imwrite("my_image.jpg",image)
#             print("I have been stucked in the else condition of passing URL. .  .")
#         print(type(image))
#
#         mrz = read_mrz(image)
#         mrz_data = mrz.to_dict()
#         #
#         data["success"] = True
#         data.update(mrz_data)
#
#     # return a JSON response
#     return JsonResponse(data)
#
#
# def _grab_image(path=None, stream=None, url=None):
#     # if the path is not None, then load the image from disk
#     if path is not None:
#         image = cv2.imread(path)
#     # otherwise, the image does not reside on disk
#     else:
#         # if the URL is not None, then download the image
#         if url is not None:
#             resp = urllib.request.urlopen(url)
#             print(type(resp))
#             data = resp.read()
#             print(type(data))
#             print("I am in the ELSE condition . . ")
#         # if the stream is not None, then the image has been uploaded
#         elif stream is not None:
#             data = stream.read()
#         # convert the image to a NumPy array and then read it into
#         # OpenCV format
#         # image = np.asarray(bytearray(data), dtype = "uint8")
#         # print(type(image))
#         # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#     # return the image
#     # return image
#     return data