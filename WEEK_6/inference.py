import time

from PIL import Image

from models.model_loader import ModelLoader

class ImageEnhancer():
  def __init__(self):
    self.loader = ModelLoader()
    self.pipe = self.loader.load_model()
    
  def enhance(self, image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((512,512))
    
    prompt = (
      "Enhance this low-light image while preserving all objects, "
      "natural colors, realistic lighting, sharp details, "
      "high quality, photorealistic."
    )
    
    
    start_time = time.time()
    
    enhanced = self.pipe(
      prompt=prompt,
      image=image,
      strength=0.15,
      guidance_scale=5.0,
      num_inference_steps=50
    ).images[0]
    
    end_time = time.time()
    
    output_path = "outputs/enhanced_image.png"
    enhanced.save(output_path)
    
    return image, enhanced, output_path, end_time - start_time