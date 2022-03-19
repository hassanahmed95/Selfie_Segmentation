import requests
import base64
import numpy as np
import cv2

URL = "http://ec2-3-110-46-239.ap-south-1.compute.amazonaws.com/face_segmentation/detect/"

files = {
    'files': ('3.jpeg', open('3.jpeg', 'rb')),
}

response = requests.post(url=URL, files=files)

data = response.json()
print(data)
# exit()
status = data["Successful"]
if status:
    base64_data = data["base64"]
    base64_data = base64_data.encode()
    # print(base64_data)

    binary = base64.decodebytes(base64_data)
    # binary = base64.b64decode(image_b64)
    image = np.asarray(bytearray(binary), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    print(image)
    cv2.imshow("sd", image)
    cv2.waitKey()
else:
    print("Some Error Occurred")

#
#
# import requests
#
# URL = "http://ec2-3-110-46-239.ap-south-1.compute.amazonaws.com/face_segmentation/detect/"
# files = {
#     'files': ('3.jpeg', open('3.jpeg', 'rb')),
# }
#
# response = requests.post(url=URL, files=files)
#
# data = response.json()
# status = data["Successful"]
# if status:
#     base64_data = data["base64"]
#     print(base64_data)
# else:
#     print("Some Error Occurred")
