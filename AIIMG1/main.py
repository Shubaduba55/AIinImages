import math
import cv2
import imutils
import numpy as np

from Draw import rectangle, draw_lines, draw_circle, draw_text


def glue_images(path1: str, path2: str):
    # Task 8
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    glued = np.hstack((img1, img2))
    cv2.imshow("Glued images", glued)
    cv2.waitKey()
    cv2.destroyAllWindows()


def blur_image(path_read: str, path_write: str = ""):
    # Task 8
    img = cv2.imread(path_read)
    blurred = cv2.GaussianBlur(img, (11, 11), 0)
    cv2.imshow("Blurred Image", blurred)
    cv2.waitKey()
    cv2.destroyAllWindows()

    if path_write != "":
        cv2.imwrite(path_write, blurred)


def rotate_image_imutils(path: str):
    # Task 7
    img = cv2.imread(path)

    rotated = imutils.rotate(img, 45, scale=0.7)
    cv2.imshow("Rotated Imutils", rotated)
    cv2.waitKey()
    cv2.destroyAllWindows()


def rotate_image(path: str):
    # Task 7
    img = cv2.imread(path)
    h, w = img.shape[0:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, -45, 0.7)
    rotated = cv2.warpAffine(img, matrix, (w, h))

    cv2.imshow("Rotated", rotated)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return


def resize_imutils(path: str):
    # Task 6
    img = cv2.imread(path)

    resized = imutils.resize(img, width=800)
    cv2.imshow("Resized", resized)
    cv2.waitKey()
    cv2.destroyAllWindows()


def resize_proportion(path: str):
    img = cv2.imread(path)
    h, w = img.shape[0:2]
    w_new = 300

    h_new = int((w_new / w) * h)

    resized = cv2.resize(img, (w_new, h_new))
    cv2.imshow("Resized", resized)
    cv2.waitKey()
    cv2.destroyAllWindows()


def resize_img(path: str):
    # Task 6
    img = cv2.imread(path)

    resized = cv2.resize(img, (300, 300))
    cv2.imshow("Resized", resized)
    cv2.waitKey()
    cv2.destroyAllWindows()


def roi(path: str):
    # Task 5

    img = cv2.imread(path)
    roi = img[250:550, 250:550]
    cv2.imshow("ROI", roi)
    cv2.waitKey()
    cv2.destroyAllWindows()


def invert_values(blue: int, green: int, red: int):
    # Task 4
    return 255 - blue, 255 - green, 255 - red


def change_pixels(path_read: str, path_write: str):
    # Task 4
    img = cv2.imread(path_read)

    x = img.shape[0]
    y = img.shape[1]

    for i in range(x):
        for j in range(y):
            if math.sin(i) ** 2 > 0.5:
                img[i, j] = invert_values(*img[i, j])

    cv2.imwrite(path_write, img)


def read_pixel(path: str):
    # Task 4
    img = cv2.imread(path)
    (blue, green, red) = img[500, 200]
    print(f"Blue: {blue}, Green: {green}, Red: {red}")
    return


def read_and_save_image(path_read: str, path_write: str, reading_property: int = 1):
    # Task 3
    img = cv2.imread(path_read, reading_property)
    cv2.imwrite(path_write, img)


def read_and_show_image(path: str):
    # Task 2

    # Read image
    img = cv2.imread(path)

    # Show image
    cv2.imshow("Protomen", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def main():
    # Path to image
    protomen_original = "img/protomen.jpg"
    protomen_changed = "img/protomen3.jpg"
    dawn_original = "img/dawn.jpg"

    protomen_blurred = "img/protomen_blurred.jpg"

    # points2 = [(0, 0), (200, 200)]
    # points3 = [(0, 0), (75, 90), (80, 175)]
    # draw_lines(points2, (0, 255, 0), 3)
    # draw_lines(points3, (100, 150, 50), 3)

    # draw_circle((100, 100), 70, (5, 250, 235), 2)

    draw_text("Deadpool",
              cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
              4,
              (150, 50, 200),
              2,
              cv2.LINE_AA)

    return


if __name__ == '__main__':
    main()
