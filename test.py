##jpg剪裁方法

from PIL import Image
import matplotlib.pyplot as plt

# img = Image.open('C:/Users/16941/Desktop/biye/train/000000.jpg')  # 打开图像
# size_img = img.size
# size_x = size_img[0]
# size_y = size_img[1]
# print(size_x, size_y)
# plt.figure("beauty")
# plt.subplot(1, 2, 1), plt.title('origin')
# plt.imshow(img, "gray")
# plt.axis('off')

file_path = "C:/Users/16941/Desktop/biye/train/position.txt"
a=[]
with open(file_path) as pos:
    a=pos.read()
    a=a.split("\n")

len=len(a)-1
print(a)
b=a[0]
print(b)
print(len(b))
b=b.split(" ")
print(len(b))
c=a[1]
print(b[0])
print(c)

# x_c = float(center[0])
# y_c = float(center[1])
# # patch=59
# x = x_c * size_x
# y = y_c * size_y
# w = 29
# h = 29
# box = (x, y, x + w, y + h)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
# roi = img.crop(box)
# plt.subplot(1, 2, 2)
# plt.title("roi")
# plt.imshow(roi, "gray")
# plt.axis('off')
# plt.show()

# with open(file_path) as pos:
#     center=pos.readline()




