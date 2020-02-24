import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt




def overlay_image_alpha(img, img_overlay, pos, alpha_mask):
    """Overlay img_overlay on top of img at the position specified by
    pos and blend using alpha_mask.

    Alpha mask must contain values within the range [0, 1] and be the
    same size as img_overlay.
    """

    x, y = pos

    # Image ranges
    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    # Overlay ranges
    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    # Exit if nothing to do
    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    channels = img.shape[2]

    alpha = alpha_mask[y1o:y2o, x1o:x2o]
    alpha_inv = 1.0 - alpha

    for c in range(channels):
        img[y1:y2, x1:x2, c] = (alpha * img_overlay[y1o:y2o, x1o:x2o, c] +
                                alpha_inv * img[y1:y2, x1:x2, c])




eyes_cascade = cv2.CascadeClassifier("Train/third-party/frontalEyes35x16.xml")
nose_cascade = cv2.CascadeClassifier("Train/third-party/Nose18x15.xml")


spec_img = cv2.imread("Train/glasses.png", -1)
mus_img =  cv2.imread("Train/mustache.png", -1)


frame  = cv2.imread("Test/Before.png")


eyes  = eyes_cascade.detectMultiScale(frame,1.1,5)
nose  = nose_cascade.detectMultiScale(frame,1.1,5)

for (x,y,w,h) in eyes:
    #cv2.rectangle(frame,(x,y),(x+h,y+w),(255,0,0),2)
    s_img = cv2.resize(spec_img,(h,w))
    overlay_image_alpha(frame,
                    s_img[:, :, 0:3],
                    (x, y),
                    s_img[:, :, 3] / 255.0)
    break


for (x,y,w,h) in nose:
    #cv2.rectangle(frame,(x,y),(x+h,y+w),(255,0,0),2)

    s_img = cv2.resize(mus_img,(h+w,w))
    w = int(w/2)
    h = int(h/2)
    overlay_image_alpha(frame,
                    s_img[:, :, 0:3],
                    (x-w, y+h),
                    s_img[:, :, 3] / 255.0)
    break



cv2.imshow("Video Frame", frame)


cv2.waitKey(2000)
cv2.destroyAllWindows()


frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.figure(figsize=(12,12))
plt.imshow(frame)
plt.show()

frame = np.array(frame, dtype="float32")/255.

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
cv2.imwrite("img.jpg", frame)

frame = frame.reshape((-1,3))

df = pd.DataFrame(frame, columns=["Channel 1","Channel 2", "Channel 3"])
df.to_csv("pred.csv", index=False)
