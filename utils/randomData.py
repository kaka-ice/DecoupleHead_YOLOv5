#-*- coding = utf-8 -*- 
#@time:2022/6/10 1:45
#@Author:ice

import os
import random
from shutil import copy

# 实现功能：将图片、标签文件随机划分并且创建符合训练规范的文件格式

# 随机划分比例 训练集：验证集=7:3
train_rate = 0.8
# 原始图像及标签文件夹
image_Dir = r"H:\\原数据集+扩充数据集\\Stage_Y_Img"
text_Dir = r"H:\\原数据集+扩充数据集\\Stage_Y_Text"
# 创建符合训练标准的文件夹
image_train = r"H:\原数据集+扩充数据集\new_file\\litchi_data\\images\\train"
image_val = r"H:\原数据集+扩充数据集\new_file\\litchi_data\\images\\val"

text_train = r"H:\原数据集+扩充数据集\new_file\\litchi_data\\labels\\train"
text_val = r"H:\原数据集+扩充数据集\new_file\\litchi_data\\labels\\val"

dir_list = [image_train, image_val, text_train, text_val]

for i in dir_list:
    if not os.path.exists(i):
        os.makedirs(i)

# 获取标签目录下所有文件，并返回为列表格式
text_list = os.listdir(text_Dir)
sum_num = len(text_list)
print(text_list)

train_nums = int(train_rate * sum_num)
# 返回[0,1,2,3,4,5...,sum_nums]
list = range(sum_num)
# 随机一段长为train_nums的字符串,返回一个列表
train_index = random.sample(list, train_nums)
print(train_index)

for i in range(len(text_list)):
    # 如果为训练集，则将图像和标签复制到对应的文件夹
    if i in train_index:
        # 图像
        copy(os.path.join(image_Dir, text_list[i].split(".")[0] + ".jpg"), image_train)
        # 标签
        copy(os.path.join(text_Dir, text_list[i]), text_train)
    # 验证集
    else:
        # 图像
        copy(os.path.join(image_Dir, text_list[i].split(".")[0] + ".jpg"), image_val)
        # 标签
        copy(os.path.join(text_Dir, text_list[i]), text_val)
