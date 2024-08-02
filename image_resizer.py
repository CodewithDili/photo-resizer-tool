from PIL import Image
import os

def resize_images(directory, width):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(directory, filename)
            try:
                img = Image.open(img_path)
                wpercent = (width / float(img.size[0]))
                height = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((width, height), Image.Resampling.LANCZOS)
                resized_img_path = os.path.join(directory, f'resized_{filename}')
                img.save(resized_img_path)
                print(f'Resized and saved {filename} as {resized_img_path}')
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

if __name__ == "__main__":
    directory = "C:\\Users\\Dili\\Desktop\\image-resizer"
    width = 800
    resize_images(directory, width)



