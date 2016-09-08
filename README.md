# Camera library

Project description:

 * Control the Raspberry Pi camera.


## Download code
Install git and clone the repository
```
sudo apt-get install git
```
Install the openCV library and the PiCamera library
```
sudo apt-get install python-opencv
sudo apt-get install python-picamera
```
## Enable the camera module
```
sudo raspi-config
```
Select "6 Enable Camera"<br>
![raspi-config execution](https://github.com/danny270793/Camera/blob/master/images/raspiconfig.png)<br>
Select "6 Enable Camera"<br>
![Enable module](https://github.com/danny270793/Camera/blob/master/images/enable.png)<br>
Confirm you want to enable it<br>
![Module enabled](https://github.com/danny270793/Camera/blob/master/images/enabled.png)<br>
At the end it will ask you for reboot, reboot it<br>
![Ask for reboot](https://github.com/danny270793/Camera/blob/master/images/reboot.png)<br>
Download the Gpio library code
```
sudo git clone https://github.com/danny270793/Camera.git
cd Camera
```

## Install the library
```
sudo python setup.py install
```

## Test the Gpio library
* Go to the examples folder and try it.

## Follow me
* [Facebook](https://www.facebook.com/danny.vaca.9655)
* [Instagram](https://www.instagram.com/danny27071993/)
* [Youtube](https://www.youtube.com/channel/UC5MAQWU2s2VESTXaUo-ysgg)
* [Github](https://www.github.com/danny270793/)
* [LinkedIn](https://www.linkedin.com/in/danny270793)

## Version
Camera library version 1.8.9.0.25<br> 
Last update 078/09/2016