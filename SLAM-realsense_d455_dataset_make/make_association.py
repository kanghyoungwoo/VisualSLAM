import os

file_list_rgb = os.listdir('dataset/rgb')
file_list_depth = os.listdir('dataset/depth')

file_list_rgb.sort()
file_list_depth.sort()

time_stamp = 0.10374

f = open("dataset/association_d455.txt", 'w')
for i in range(len(file_list_rgb)):
    data = f"{time_stamp*i:.4f} rgb/{file_list_rgb[i]} {time_stamp*i:.4f} depth/{file_list_depth[i]}\n"
    f.write(data)
f.close()
