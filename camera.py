'''
	Raspberry Camera libray for python
	name	: Camera
	version	: 1.7.9.16.17.51
	author	: Danny Vaca
'''
# opencv library is required
import cv2
# the camera will use the rpi module
Rpi=0
# the camera will use the opencv module
CV2=1
class Keypad(object):
	'''
		Allows to catch the keyboard keys
	'''
	def __init__(self):
		# empty constructor
		pass
	def isPressed(self,key='q'):
		'''
			Ask if key is pressed, by default key is 'q'
		'''
		# check if the kwy is pressed
		return (cv2.waitKey(5)&0xFF)==ord(key)
class Window(object):
	'''
		Allows to create and destroy windows to show the images
	'''
	def __init__(self):
		# empty constructor
		pass
	def __del__(self):
		# destroy all windows
		cv2.destroyAllWindows()
	def show(self,image,name='image'):
		# shows the image with the identifier name
		# name bay default is 'image'
		cv2.imshow(name,image)
	def close(self,name='image'):
		# close the image called name
		cv2.destroyWindow(name)
class Camera(object):
	'''
		Object that allows to take and save photos
	'''
	# the camera will use the rpi module
	Rpi=0
	# the camera will use the opencv module
	CV2=1
	def __init__(self,type=Rpi):
		'''
			by default will use the Rpi module
			to use Rpi module the PiCamera library must be installed
			to use cv2 module the openCv library must be installed
		'''
		# save the type of the camera module
		self.type=type
		if self.type==self.Rpi:
			# if is rpi import piCamera
			from picamera import PiCamera
			self.camera=PiCamera()
		elif self.type==self.CV2:
			# id is cv2 use the opencv module
			self.camera=cv2.VideoCapture(0)
			while not self.camera.isOpened():
				# do nothing while the camera is not opened
				pass
		else:
			# if the camera type is not valid
			raise Exception('Invalid camera type '+str(type))
	def __del__(self):
		if self.type==self.CV2:
			# if is ussing the cv2 module then realse the camera resources
			self.camera.release()
	def capture(self):
		if self.type==self.CV2:
			# if is cv2 module take a photo
			success,image=self.camera.read()
			while not success:
				# re-take the photo if is has any problem
				success,image=self.camera.read()
		elif self.type==self.Rpi:
			# rpi take and save the photo
			self.camera.capture('image.jpg')
			# we have to load the saved image
			image=cv2.imread('image.jpg')
		return image
	def getBytes(self):
		# takes the photo and get this as bytes
		image=self.capture()
		ret,jpeg=cv2.imencode('.jpg',image)
		bytes=jpeg.tobytes()
		return bytes
