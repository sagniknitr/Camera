# import all modules from camera file
from camera import *

# use the camera with the piCamera module
camera=Camera(type=Rpi)
# create the keypad object
keypad=Keypad()
# create the windows manager
window=Window()

# forever loop
while True:
	# take a photo
	image=camera.capture()
	# show the photo
	window.show(image,'Press "q" to quit')
	if keypad.isPressed('q'):
		#  hear for the 'q' key to break the forever loop
		break
# close the window by the identifier 'Press "q" to quit'
window.close('Press "q" to quit')
