import cv2
import base64


def face_detection_status(message, image):
    try:
        if image is not None:
            _, encimg = cv2.imencode(".jpg ", image)
            img_byte = base64.b64encode(encimg).decode("utf-8")
            json_data = generating_json_response(message, img_byte)
            return json_data
        else:
            json_data = generating_json_response(message, None)
            return json_data

    except Exception as e:
        json_data = generating_json_response(message, None)
        return json_data


# in that method the image will be segmented face
def generating_json_response(message, image):
    json_data = dict()
    error = dict()
    if image:
        json_data["Successful"] = True

        json_data["message"] = message
        json_data["base64"] = image
    else:
        json_data["Successful"] = False
        error['message'] = message
        json_data["message"] = error
    # json_data["base64"] = image
    return json_data
