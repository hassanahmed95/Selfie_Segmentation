from .detection_status import face_detection_status
import os
import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import dlib
import imutils
import numpy as np
from imutils import face_utils


def face_segmentation(image):
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    segmentor = SelfiSegmentation()
    detector = dlib.get_frontal_face_detector()

    try:
        full_image = image.copy()
        response, segmented_face_image = face_extraction(full_image, predictor, detector, segmentor)

        successful_detection = "Face has been successfully segmented"
        unsuccessful_detection = "Sorry, Face Segmentation Failed"

        if response:
            level = "INFO"
            json_data = face_detection_status(successful_detection, segmented_face_image)
            return json_data, level
        else:
            level = "ERROR"
            json_data = face_detection_status(unsuccessful_detection, None)
            return json_data, level
    except Exception:
        return {}, False


def face_extraction(img, predictor, detector, segmentor):
    img = imutils.resize(img, width=640)
    bg_img = "{base_path}/background.jpg".format(
        base_path=os.path.abspath(os.path.dirname(__file__)))

    bg_img = cv2.imread(bg_img)

    try:
        bg_img = cv2.resize(bg_img, (img.shape[1], img.shape[0]))
        height_img, width_img, width_channal = img.shape
        print("I am here")

        img = segmentor.removeBG(img, bg_img, threshold=.7)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        if len(rects) >= 2:
            return False, None
        else:
            rect = rects[0]
            shape = predictor(gray, rect)
            face = face_utils.shape_to_np(shape)

            x_pad = int(abs(face[0][0] - face[20][0]))
            y1_pad = int(abs(face[20][1] - face[33][1]))
            y2_pad = int(abs(face[8][1] - face[57][1]))
            x1 = int(face[0][0] - x_pad)
            x2 = int(face[16][0] + x_pad)
            y1 = int(face[20][1] - y1_pad - y1_pad)
            y2 = int(face[8][1] + y2_pad)

            if x1 < 0:
                x1 = 0
            if x1 > width_img:
                x1 = width_img
            if x2 < 0:
                x2 = 0
            if x2 > width_img:
                x2 = width_img
            if y1 < 0:
                y1 = 0
            if y1 > height_img:
                y1 = height_img
            if y2 < 0:
                y2 = 0
            if y2 > height_img:
                y2 = height_img

            neck_mid_x = int(face[8][0])
            neck_mid_y = int(face[8][1] + y2_pad)

            y2_p = int(face[13][1])

            pts = np.array([[x1, y2_p], [neck_mid_x, neck_mid_y], [x2, y2_p], [x2, y1], [neck_mid_x, 0], [x1, y1]])
            croped = img[y1:y2, x1:x2].copy()

            ## (2) make mask
            pts = pts - pts.min(axis=0)

            mask = np.zeros(croped.shape[:2], np.uint8)
            cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

            ## (3) do bit-op
            dst = cv2.bitwise_and(croped, croped, mask=mask)

            ## (4) add the white background
            bg = np.ones_like(croped, np.uint8) * 255
            cv2.bitwise_not(bg, bg, mask=mask)
            dst2 = bg + dst
            bg_img[y1:y2, x1:x2] = dst2

            return True, bg_img
    except Exception as e:
        print("I m in exception")
        print(e)
        return False, None
