from PIL import Image
import pytesseract
# Open an image file
image_path = "D:/OneDrive/Pictures/42daab7e07e71d66869fc64bcfead5b2.jpg"
img = Image.open(image_path)

# Use pytesseract to extract text
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)
