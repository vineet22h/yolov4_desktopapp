# Yolov4 Desktop Application
<br>
The project deals with creation of application which is feeded with a real-time video that is accquired by users webcam.
The project is dockerized and prepared for deployment using kuberenetes.<br><br>

![alt text](https://miro.medium.com/max/803/1*2cHZKUvMpDqgSBeXhfCvfg.png)

# Pretrained yolov4 model
Pretrained yolov4 model can be downloaded here:
https://drive.google.com/drive/folders/1hMW_cmxAPmJOGV-1EPz1OB98Qwmpe6f4?usp=sharing <br>

# DockerHub Image
Dockerized image can be pulled using:<br>
docker pull vineet22h/yolov4_desktopapp:latest<br>

Run docker container on ubuntu using:<br>
sudo docker run --rm --net=host -e DISPLAY=$DISPLAY --volume="$HOME/.Xauthority:/home/root/.Xauthority:rw" --device /dev/video0 vineet22h/yolov4_desktopapp

# References 
https://github.com/taipingeric/yolo-v4-tf.keras
