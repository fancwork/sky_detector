# Sky Detector
This repository contains a Python script implementing a simple sky detection algorithm using Gradio and OpenCV for image processing. The algorithm takes an input image, detects the sky region, and isolates it from the rest of the image.

Live Gradio Link: [Sky Detector on Gradi](https://huggingface.co/spaces/fancwork/sky_detector)

## Output Example
![Screenshot of output example of the sky detector](https://github.com/fancwork/sky_detector/blob/main/output_example.jpg)

## Dependencies
Gradio ('pip install gradio')

## How to Use
1. Install the required dependencies:
`pip install gradio`

2. Run the provided code in your Python environment:
`python sky_detector.py`

3. Once the script is running, it will launch a Gradio interface for interactive testing of the sky detection algorithm.

4. Upload an image using the interface, and the algorithm will process it, isolating and displaying the detected sky region.

## Functions
**convert_to_grayscale**
Converts the input image to grayscale to prepare for edge detection.

**apply_blur**
Applies Gaussian blurring to the grayscale image to reduce noise.

**calculate_gradient**
Uses Laplacian gradient to detect edges in the blurred image.

**refine_mask_morphological**
Applies morphological erosion to refine the edge detection mask.

**refine_mask_median**
Uses median blur to further refine the mask.

**get_sky_region**
Extracts the sky region from the original image using the refined mask.

**sky_detector**
Main function that combines the above functions to detect and display the sky region.

## Gradio Interface
The Gradio interface allows users to upload an image and visualize the detected sky region. It uses the sky_detector function to process the image and display the result interactively.

**Note:** Uncomment the relevant sections in the code if running in a Google Colab environment or if you want to display intermediate steps.
