import rospy
import cv2
import threading
import time
from datetime import datetime

from drone_wrapper import DroneWrapper


# Hardware Abstraction Layer
class HAL:
    IMG_WIDTH = 320
    IMG_HEIGHT = 240
    
    def __init__(self):
        rospy.init_node("HAL")
    
        self.image = None
        self.drone = DroneWrapper(name="rqt", ns="cat/")
        # self.camera = ListenerCamera("/cat/drone_wrapper/cam_frontal/image_raw")
        # self.camera = ListenerCamera("/F1ROS/cameraL/image_raw")
        # self.motors = PublisherMotors("/F1ROS/cmd_vel", 4, 0.3)

    # Explicit initialization functions
    # Class method, so user can call it without instantiation
    @classmethod
    def initRobot(cls):
        new_instance = cls()
        return new_instance
    
    # Get Image from ROS Driver Camera
    def getFrontalImage(self):
        image = self.drone.get_frontal_image()
        return image

    def getVentralImage(self):
        image = self.drone.get_ventral_image()
        return image

    def takeoff(self):
        self.drone.takeoff()
