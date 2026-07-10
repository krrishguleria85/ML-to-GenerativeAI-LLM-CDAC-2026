import streamlit as st 
from PIL import Image
import numpy as np
import os
import tempfile

from inference import ImageEnhancer
from utils.metrics import ImageMetrics

st.set_page_config(
  page_title="Low-Light Image Enhancement",
  page_icon="🔦",
  layout="wide"
)

with st.sidebar:
  st.header("Project Information")
  st.write("**Project:** Low-Light Image Enhancement")
  st.write("**Framework:** Stable Diffusion")
  st.write("**Library:** Diffusers")
  st.write("**Backend:** PyTorch")
  st.write("**Dataset:** LOL Dataset")


st.title("🔦 Low-Light Image Enhancement Framework")
st.write("AI-powered enhancement using Stable Diffusion, Diffusers and PyTorch.")

st.markdown("---")


#call the model
@st.cache_resource
def load_enhancer():
  try:
    return ImageEnhancer()
  except Exception as e:
    st.error(f"Failed to load the model: {e}")
    st.stop()
  
  
# upload files
upload_files = st.file_uploader(
  "📤 Upload a Low-Light Image",
  type=["png", "jpg", "jpeg"]
)


# enhance button
if upload_files is not None:
  
  st.write(f"**Uploaded File!** {upload_files.name}")

  image = Image.open(upload_files).convert("RGB")
  st.subheader("Input Image")
  st.image(image, use_container_width=True)
  st.write(f"Image Size: {image.size[0]} x {image.size[1]}")
  

  if st.button("✨ Enhance Image"):
    with st.spinner("Enhancing image... Please wait..."):
      
      
      temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
      temp_path = temp_file.name
      temp_file.close()
      
      image.save(temp_path)
        
      try:
        enhancer = load_enhancer()
        original, enhanced, output_path, runtime = enhancer.enhance(
          temp_path
        )
        
      except Exception as e:
        st.error(f"Error: {e}")
        st.stop()
        
      finally:
        if os.path.exists(temp_path):
          os.remove(temp_path)
    
    
    #compare images
    col1, col2 = st.columns(2)
    
    with col1:
      st.subheader("Original")
      st.image(original, use_container_width=True)
      
    with col2:
      st.subheader("Enhanced")
      st.image(enhanced, use_container_width=True)
      
    #calculate Metrics
    metrics = ImageMetrics()
    original_np = np.array(original)
    
    enhanced = enhanced.resize(original.size)
    enhanced_np = np.array(enhanced)
      
    psnr = metrics.cal_psnr(
      original_np,
      enhanced_np
    )
      
    ssim = metrics.cal_ssim(
      original_np,
      enhanced_np
    )
      
      
    #show results
    st.success("✅ Enhancement Completed")
    
    metric1, metric2, metric3 = st.columns(3)
    
    metric1.metric("PSNR", f"{psnr:.2f}")
    metric2.metric("SSIM", f"{ssim:.4f}")
    metric3.metric("Time", f"{runtime:.2f} s")
    
    
    #download button
    with open(output_path, "rb") as file:
      st.download_button(
        "⬇ Download Enhanced Image",
        data = file,
        file_name="enhanced_image.png",
        mime="image/png"
      )

st.markdown("---")
st.caption(
  "Developed for CDAC Summer Training (AI & ML) Project using Stable Diffusion, Diffusers, and PyTorch."
)