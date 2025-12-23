from PIL import Image
import numpy as np

# Create a 640x480 RGB image with a gradient
width, height = 640, 480
array = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        array[y, x] = [x % 255, y % 255, (x + y) % 255]

img = Image.fromarray(array)
img.save("dummy_input.png")
print("dummy_input.png created")
