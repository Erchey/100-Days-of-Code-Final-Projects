from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageDraw, ImageFont

def select_image():
    global original_image_path
    original_image_path = filedialog.askopenfilename(title="Select an Image File")
    status_label.config(text=f"Selected Image: {original_image_path}")

def apply_watermark():
    if original_image_path:
        original_image = Image.open(original_image_path)
        width, height = original_image.size

        # Create a transparent image for the watermark
        watermark = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark)
        font = ImageFont.load_default()
        draw.text((10, 10), "Watermark", fill=(255, 255, 255, 128), font=font)

        # Composite the original image with the watermark
        watermarked_image = Image.alpha_composite(original_image.convert('RGBA'), watermark)
        watermarked_image.show()
    else:
        status_label.config(text="Please select an image first.")

# Create the main window
root = Tk()
root.title("Watermarking App")

# Select Image Button
select_button = Button(root, text="Select Image", command=select_image)
select_button.pack()

# Apply Watermark Button
apply_button = Button(root, text="Apply Watermark", command=apply_watermark)
apply_button.pack()

# Status Label
status_label = Label(root, text="")
status_label.pack()

root.mainloop()