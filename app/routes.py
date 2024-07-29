from flask import Blueprint, render_template, current_app
import cv2
import numpy as np
import os

# Define the blueprint for the app routes
app = Blueprint('app', __name__)

# Develop a highlighted satellite image that mimics the detection of large crops
def process_image(image_path):
    # Construct the full image path and ensure the image exists
    image_path = os.path.join(current_app.root_path, 'static', image_path)
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"{image_path} does not exist.")

    # Load and process the image
    original_image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([25, 20, 20])
    upper_green = np.array([95, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    segmented_image = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    spatial_resolution = 1  # meters per pixel
    highlighted_image = image_rgb.copy()
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
    num_colors = len(colors)

    crop_type_mapping = {
        0: {'name': 'Potatoes', 'days_till_harvest': 50, 'planting_date': '15-04-2024', 'crop_health': 'healthy', 'price_per_m2': 7.84},
        1: {'name': 'Sugarbeet', 'days_till_harvest': 120, 'planting_date': '03-04-2024', 'crop_health': 'decent', 'price_per_m2': 5.96},
        2: {'name': 'Wheat', 'days_till_harvest': 20, 'planting_date': '17-10-2023', 'crop_health': 'very healthy', 'price_per_m2': 6.26}
    }

    large_crops = []
    for i, contour in enumerate(contours):
        color = colors[i % num_colors]
        area_pixels = cv2.contourArea(contour)
        area_sq_meters = area_pixels * (spatial_resolution ** 2)
        area_hectares = area_sq_meters / 10000.0
        if area_hectares > 0.3:
            crop_data = crop_type_mapping[i % len(crop_type_mapping)]
            crop_name = crop_data['name']
            cv2.drawContours(highlighted_image, [contour], -1, color, -1)
            large_crops.append((area_hectares, crop_name))
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(highlighted_image, crop_name, (cx - 50, cy), font, 0.5, (255, 255, 255), 2)
            crop_data['hectares'] = area_hectares

    # Save the processed image and return relevant data
    output_image_path = os.path.join(current_app.static_folder, 'highlighted_image.jpg')
    cv2.imwrite(output_image_path, cv2.cvtColor(highlighted_image, cv2.COLOR_RGB2BGR))
    return large_crops, 'highlighted_image.jpg', crop_type_mapping

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/valuation')
def valuation():
    try:
        large_crops, output_image_path, crop_type_mapping = process_image('cropland_edit.jpg')
        return render_template('valuation.html', large_crops=large_crops, output_image_path=output_image_path, crop_type_mapping=crop_type_mapping)
    except FileNotFoundError as e:
        return str(e), 404

@app.route('/risk_assessment')
def risk_assessment():
    return render_template('risk_assessment.html')

@app.route('/claims')
def claims():
    return render_template('claims.html')


