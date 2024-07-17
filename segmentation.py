import cv2
from ultralytics import YOLO
import numpy as np
import os

def segment_image(image_path):
    try:
        # Load the YOLOv8 model
        model = YOLO("./model/yolov8m-seg.pt")  # pretrained YOLOv8 model

        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            return None

        H, W, _ = image.shape

        # Run batched inference on the image
        results = model.predict(image, retina_masks=True)

        # Check if results contain masks
        if not results or not results[0].masks:
            print("No masks found in results.")
            return None

        # Create an empty mask for the entire image
        combined_mask = np.zeros((H, W), dtype=np.uint8)

        # Combine all masks
        for result in results:
            if result.masks:
                for mask in result.masks.data:
                    mask = mask.cpu().numpy() * 255
                    mask = cv2.resize(mask, (W, H)).astype(np.uint8)
                    combined_mask = cv2.bitwise_or(combined_mask, mask)

        # Create a 4-channel image (RGBA)
        b, g, r = cv2.split(image)
        alpha = combined_mask
        rgba = [b, g, r, alpha]
        segmented_image = cv2.merge(rgba, 4)

        # Generate the output file path
        base_name, _ = os.path.splitext(image_path)
        base_name = base_name.split("./temp/", 1)[1]
        output_path = f"./output/{base_name}_output.png"

        # Save the segmented image with transparent background
        cv2.imwrite(output_path, segmented_image)

        return output_path
    except Exception as e:
        print(f"Segmentation error: {e}")
        return None
