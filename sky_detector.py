import gradio as gr
#from google.colab import files
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import medfilt

# upload input image
#def upload_image():
#    uploaded = files.upload()
#    file = next(iter(uploaded))
#    img = cv2.imread(file)
#    return img

# display input image
#def display_image(img, title="Image"):
#    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert from BGR to RGB for OpenCV
#    plt.imshow(img_rgb)
#    plt.title(title)
#    plt.axis("off")
#    plt.show()

# convert input image to grayscale to prepare for edge detection
def convert_to_grayscale_and_blur(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.blur(img_gray, (5, 5)) # Gaussian blurring with a kernel size of (9, 3) to reduce noise
    return img_blurred

# detect edges using Laplacian filter
def calculate_gradient(img_blurred, threshold=7):
    laplacian = cv2.Laplacian(img_blurred, cv2.CV_8U)
    gradient_mask = (laplacian < threshold).astype(np.uint8)
    return gradient_mask

# refine skyline using median filtering and morphological operation
def refine_skyline(mask):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    eroded_mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)
    skyline_mask = cal_skyline(eroded_mask)
    return skyline_mask

# adjust skyline using median filtering to isolate the sky
def cal_skyline(mask):
    h, w = mask.shape
    for i in range(w):
        column = mask[:, i]
        after_median = medfilt(column, kernel_size=21)
        try:
            first_white_index = np.where(after_median == 1)[0][0]
            first_black_index = np.where(after_median == 0)[0][0]
            if first_black_index > first_white_index:
                mask[:first_black_index, i] = 1
                mask[first_black_index:, i] = 0
        except IndexError:
            continue
    return mask

# extract sky region by applying the mask
def get_sky_region(img, mask):
    sky_region = cv2.bitwise_and(img, img, mask=mask)
    return sky_region

# run in order and show the detected sky region
#def sky_detector(img):
#    display_image(img, "Original Image")
#    img_blurred = convert_to_grayscale_and_blur(img)
#    gradient_mask = calculate_gradient(img_blurred)
#    skyline_mask = refine_skyline(gradient_mask)
#    sky_region = get_sky_region(img, skyline_mask)
#    display_image(sky_region, "Sky Region")

# main
#image = upload_image()
#sky_detector(image)

# run in order for Gardio
def sky_detection(image):
    img_blurred = convert_to_grayscale_and_blur(image)
    gradient_mask = calculate_gradient(img_blurred)
    skyline_mask = refine_skyline(gradient_mask)
    sky_region = get_sky_region(image, skyline_mask)
    sky_region_rgb = cv2.cvtColor(sky_region, cv2.COLOR_BGR2RGB)  # Convert to RGB for Gradio display
    return sky_region_rgb

# set up Gardio interface
interface = gr.Interface(fn=sky_detection, inputs=gr.Image(), outputs="image")
interface.launch()