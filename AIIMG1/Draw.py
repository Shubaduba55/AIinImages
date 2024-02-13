import math
import cv2
import imutils
import numpy as np


def draw_text(text: str,
              font_face,
              font_scale: int,
              colour: tuple,
              thickness: int,
              line_type):
    img = np.zeros((300, 500, 3), np.uint8)

    cv2.putText(img, text, (0, 200),
                fontFace=font_face,
                fontScale=font_scale,
                color=colour,
                thickness=thickness,
                lineType=line_type)

    cv2.imshow("Text", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def draw_circle(center: tuple, radius: int, colour: tuple, thickness: int):
    # Task 9
    img = np.zeros((200, 200, 3), np.uint8)
    cv2.circle(img, center, radius, colour, thickness)

    cv2.imshow("Circle", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def draw_lines(points: list, colour: tuple, thickness: int):
    # Task 9
    img = np.zeros((200, 200, 3), np.uint8)
    if len(points) == 2:
        cv2.line(img, points[0], points[1], colour, thickness)
    elif len(points) > 2:
        cv2.polylines(img, pts=np.int32([points]), color=colour, thickness=thickness, isClosed=True)

    cv2.imshow("Lines", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def rectangle(path: str):
    # Task 9
    img = cv2.imread(path)
    # pt(x, y)
    pt1 = (179, 100)
    pt2 = (550, 550)
    colour = (100, 100, 100)
    thickness = 2
    cv2.rectangle(img, pt1, pt2, colour, thickness)
    cv2.imshow("Rectangle", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
