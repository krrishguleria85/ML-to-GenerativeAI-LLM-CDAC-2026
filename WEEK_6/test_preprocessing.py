from utils.preprocessing import ImagePreprocessor

processor = ImagePreprocessor()

image = processor.load_image(
  "dataset/lol_dataset/eval15/low/1.png"
)

processor.show_image_info(image)
image = processor.resize_image(image)

print("Resized: ", image.size)