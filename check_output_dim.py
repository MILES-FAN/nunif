from PIL import Image
import os

filename = "dummy_output_c1.png"
if not os.path.exists(filename):
    print(f"{filename} not found")
    exit(1)

img = Image.open(filename)
print(f"Dimensions: {img.size}")
if img.size == (1280, 600):
    print("Verification SUCCESS: Dimensions match C1 quilt (1280x600)")
else:
    print(f"Verification FAILED: Expected (1280, 600), got {img.size}")
