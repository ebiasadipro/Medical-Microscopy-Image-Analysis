import cv2
import os


def preprocess_image(input_path, output_path):
    """
    Basic preprocessing pipeline for microscopy images.
    """

    image = cv2.imread(input_path)

    if image is None:
        raise ValueError("Image not found")

    # Resize
    image = cv2.resize(image, (224, 224))

    # Normalize illumination
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    cv2.imwrite(output_path, image)


if __name__ == "__main__":
    print("Preprocessing pipeline ready.")
