from PIL import Image
import os

def main():
    INPUT_FOLDER = "./"
    OUTPUT_FOLDER = "./output"
    FORMATS = [
        {"name": "android-chrome-192x192.png", "size": 192},
        {"name": "android-chrome-512x512.png", "size": 512},
        {"name": "android-chrome-maskable-192x192.png", "size": 192},
        {"name": "android-chrome-maskable-512x512.png", "size": 512},
        {"name": "apple-touch-icon-60x60.png", "size": 60},
        {"name": "apple-touch-icon-76x76.png", "size": 76},
        {"name": "apple-touch-icon-120x120.png", "size": 120},
        {"name": "apple-touch-icon-152x152.png", "size": 152},
        {"name": "apple-touch-icon-180x180.png", "size": 180},
        {"name": "apple-touch-icon.png", "size": 180},
        {"name": "favicon-16x16.png", "size": 16},
        {"name": "favicon-32x32.png", "size": 32},
        {"name": "msapplication-icon-144x144.png", "size": 144},
        {"name": "mstile-150x150.png", "size": 150}
    ]

    clearOutputDirectory(OUTPUT_FOLDER)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for filename in os.listdir(INPUT_FOLDER):
        if filename.endswith(".png"):
            input_path = os.path.join(INPUT_FOLDER, filename)

            for format in FORMATS:
                output_path = os.path.join(OUTPUT_FOLDER, format["name"])
                resize_image(input_path, output_path, (format["size"], format["size"]))

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        resized_img = img.resize(size)
        resized_img.save(output_path)

def clearOutputDirectory(dir):
    try:
        for filename in os.listdir(dir):
            filepath = os.path.join(dir, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
