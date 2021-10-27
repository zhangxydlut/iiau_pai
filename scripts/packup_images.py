with open('docker_image_list.txt') as f:
    image_list = [it for it in f][1:]

image_list = [[v for v in item.strip('\n').split(' ') if v is not ''] for item in image_list]
image_list = [[it[0], it[2]] for it in image_list]

with open('docker_save.sh', 'w') as f:
    for it in image_list:
        # it: ['<image-id>', '<image-name:tag>']
        cmd = "sudo docker save -o {}.tar {}\n".format(it[1], it[0])  # 使用<image-name:tag>索引需要打包的镜像，保存为 <image-id>.tar
        # cmd = "sudo docker save -o {}.tar {}\n".format(it[1], it[1])  # 使用<image-id>索引需要打包的镜像，加载后Image Name和Tag显示<none>, 不影响使用
        print(it)
        f.write(cmd)

with open('docker_load.sh', 'w') as f:
    for it in image_list:
        cmd = "sudo docker load -i {}.tar\n".format(it[1])
        f.write(cmd)