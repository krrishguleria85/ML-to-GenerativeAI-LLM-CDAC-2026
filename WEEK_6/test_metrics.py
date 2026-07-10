import cv2
from utils.metrics import ImageMetrics

metrics = ImageMetrics()

img = cv2.imread("dataset/lol_dataset/eval15/high/1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

metrics.start_timer()

psnr = metrics.cal_psnr(img, img)
ssim = metrics.cal_ssim(img, img)

metrics.stop_timer()


print("PSNR: ", psnr) #peak signal net ratio
print("SSIM: ", ssim) #structural similarity
print("Time: ", metrics.process_time())
