
import os
from PIL import Image

def load_employee_graphs(base_dir: str, employee_name: str):
    """
    Load all graph images for a given employee.

    Args:
        base_dir (str): Path to the root folder containing employee subfolders.
        employee_name (str): Name of the employee (subfolder name).

    Returns:
        dict: Dictionary with image variables keyed by filename.
    """
    employee_dir = os.path.join(base_dir, employee_name)

    if not os.path.exists(employee_dir):
        raise FileNotFoundError(f"No folder found for employee: {employee_name}")

    # Collect all image files (assuming .png/.jpg)
    image_files = [
        f for f in os.listdir(employee_dir)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    if not image_files:
        raise FileNotFoundError(f"No images found in {employee_dir}")

    # Load images into variables
    images = {}
    for img_file in image_files:
        img_path = os.path.join(employee_dir, img_file)
        images[img_file] = Image.open(img_path)

    return images


# Example usage:

