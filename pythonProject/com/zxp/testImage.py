from PIL import Image
# windows环境之下使用双斜杠
img_path = "E:\\2020DP_ML\\2020DP_ML\\pythonProject\\com\\zxp\\dataset\\train\\ants_image\\0013035.jpg"
img = Image.open(img_path)
# 展示图片
# img.show()
# 使用os函数读取文件夹下的所有文件名称
import os
dir_path = "dataset/train/ants_image"
img_path_list = os.listdir(dir_path)
print(img_path_list[0])