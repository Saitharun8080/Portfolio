from PIL import Image
import sys

try:
    img = Image.open('profile.jpg')
    width, height = img.size
    print(f"Size: {width}x{height}")
    corners = [
        img.getpixel((0, 0)),
        img.getpixel((width-1, 0)),
        img.getpixel((0, height-1)),
        img.getpixel((width-1, height-1))
    ]
    print(f"Corners: {corners}")
except Exception as e:
    print(f"Error: {e}")
