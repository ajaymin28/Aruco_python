from imutils.video import VideoStream
import imutils
import cv2

class Imutils_Master(object):

	# Default resolution of camera
	# if you're getting black image change width and height to your camera resolution.
	frame_width = 640
	frame_height = 360
	source = "rtsp://34.168.1.65:554/ISAPI/streaming/channels/101?auth=YWRtaW46QWRtaW5AMTIz"
	obj = None

	def __init__(self,src=None):
		if src is None:
			self.obj = VideoStream(src=self.source).start()
			h,w,c = self.obj.read().shape
			self.frame_width = w
			self.frame_height = h
		else:
			self.obj = VideoStream(src=src).start()
			h,w,c = self.obj.read().shape
			self.frame_width = w
			self.frame_height = h


	def setsource(self,src):
		self.source = src

	def setframesize(self,width,height):
		self.frame_width = width
		self.frame_height = height

	def getframe(self):
		img = self.obj.read()
		imutils.resize(img,width=self.frame_width)
		return img

	def gray(self,img):
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		return img

	def resize(self,img,width):
		img = imutils.resize(img,width=width)
		return img


		