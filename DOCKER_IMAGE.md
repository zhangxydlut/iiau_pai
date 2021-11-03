## Requirements

A base docker image support pytorch and CUDA
   - Official docker hub [pytoch-docker-hub](https://hub.docker.com/r/pytorch/pytorch)
     - also used by **[mmdetection](https://github.com/open-mmlab/mmdetection/blob/master/docker/Dockerfile)**
   - A repo of prebuilt docker images (https://github.com/anibali/docker-pytorch)
   - A tutorial (https://medium.com/@zaher88abd/pytorch-with-docker-b791edd67850)

## Set up the Docker
```
sudo docker pull pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel
```
in this docker, the network is not available as a result of dns problem, run the following
```
nmcli dev show | grep 'IP4.DNS'  # check the write DNS
```
Get a output like `IP4.DNS[1]:  202.118.66.6`

```
sudo docker run \
--rm -it --init \
--gpus=all \
--dns 202.118.66.6 \
--ipc=host \
--volume="/home/zxy/Desktop/EventVision/EvTrack:/EvTrack" \
pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel bash
```

## Install Requirements for Project
```
apt-get update && apt-get install -y ffmpeg libsm6 libxext6 git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 
pip install opencv-python
pip install pyyaml yacs tqdm colorama matplotlib cython numba
pip install dv
pip install tikzplotlib
pip install pandas
apt-get install libturbojpeg
pip install jpeg4py visdom
pip install h5py pre-commit matplotlib progress mlflow
pip install mmcv-full==1.3.14 -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.6.0/index.html

```

## Create Image and Serialized it
```
docker ps -a  # get the ID of the container
docker commit -m "message" <container-id> <image-name>:<viersion>
docker save -o docker save -o ./evtrack-train-v1.0-image.tar evtrack/train:v1.0
```

## Use the Docker image
```
sudo docker run \
--rm -it --init --gpus=all \
--dns 202.118.66.6 --ipc=host \ 
--volume="/home/zxy/Desktop/EventVision/EvTrack:/EvTrack" \
evtrack/train:v1.0 \
bash
```

## Upload to Local Registry
```
# get the container
sudo docker ps -a

# make the image
sudo docker commit -a "zxy" -m "my image" <container-id> <image-name>:<version>
sudo docker commit -a "author" -m "image information" fj3i2rjf0sd pytorch:1.6.0-cuda10.1-cudnn7-devel
# rename
sudo docker tag pytorch:1.6.0-cuda10.1-cudnn7-devel 10.7.xx.xx:5000/pytorch:1.6.0-cuda10.1-cudnn7-devel
# upload to <host> e.g. 10.7.xx.xx:5000
sudo docker push 10.7.xx.xx:5000/pytorch:1.6.0-cuda10.1-cudnn7-devel
```

