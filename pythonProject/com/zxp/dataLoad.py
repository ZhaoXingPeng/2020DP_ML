import torch
from torch.utils.data import Dataset
# 读取图片
from PIL import Image
# print(torch.cuda.is_available())
# help(Dataset)
import os


class MyData(Dataset):
    # 初始化类，每次允许一个实例的时候创建
    def __init__(self, root_dir, label_dir):
        # 创建全局使用的变量,就我来看是this的作用类似
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        # print("path:"+self.path)
        self.img_path = os.listdir(self.path)
        # print("img_path:")
        # print(self.img_path)

    def __getitem__(self, index):
        img_name = self.img_path[index]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        # print("img_item_path:"+img_item_path)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)


root_dir = "dataset/train"
ants_label_dir = "ants_image"
bees_label_dir = "bees_image"
ants_dataset = MyData(root_dir, ants_label_dir)
bees_dataset = MyData(root_dir,bees_label_dir)
# 拼接数据集
train_dataset = ants_dataset + bees_dataset
print(len(train_dataset))
# print(ants_dataset[0])
# img, label = ants_dataset[0]
# # img.show()
# print(label)
