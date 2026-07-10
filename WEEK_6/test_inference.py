from inference import ImageEnhancer

enhancer = ImageEnhancer()

result, runtime = enhancer.enhance(
  "dataset/lol_dataset/eval15/low/1.png"
)

print(runtime)