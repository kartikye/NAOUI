import proxy
import random

import config
import motion
import math
import time
#import AppMainWindow

def standup():
	proxy.behavior.post.runBehavior('User/turnOnEyesLED')
	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 1.66667])
	keys.append([ [ 0.00916, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 1.66667])
	keys.append([ [ -0.10964, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 1.66667])
	keys.append([ [ 1.58458, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 1.66667])
	keys.append([ [ 0.17637, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 1.66667])
	keys.append([ [ -1.21650, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 1.66667])
	keys.append([ [ -0.55833, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 1.66667])
	keys.append([ [ 0.09200, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 1.66667])
	keys.append([ [ 0.00397, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 1.66667])
	keys.append([ [ 1.51870, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 1.66667])
	keys.append([ [ -0.13503, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 1.66667])
	keys.append([ [ 1.19188, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 1.66667])
	keys.append([ [ 0.45104, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 1.66667])
	keys.append([ [ 0.14109, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 1.66667])
	keys.append([ [ 0.00703, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 1.66667])
	keys.append([ [ -0.16103, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 1.66667])
	keys.append([ [ 0.11202, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 1.66667])
	keys.append([ [ 0.20406, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 1.66667])
	keys.append([ [ -0.09208, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 1.66667])
	keys.append([ [ 0.07359, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 1.66667])
	keys.append([ [ -0.10734, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 1.66667])
	keys.append([ [ -0.06592, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 1.66667])
	keys.append([ [ 0.19017, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 1.66667])
	keys.append([ [ -0.07512, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 1.66667])
	keys.append([ [ 0.07061, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 1.66667])
	keys.append([ [ 0.06600, [ 3, -0.55556, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.angleInterpolationBezier(names, times, keys);
	
def squat():

	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 2.00000])
	keys.append([ [ 0.00763, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 2.00000])
	keys.append([ [ 0.02757, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 2.00000])
	keys.append([ [ 1.69963, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 2.00000])
	keys.append([ [ 0.17944, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 2.00000])
	keys.append([ [ -1.45427, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 2.00000])
	keys.append([ [ -0.80991, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 2.00000])
	keys.append([ [ 0.00916, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 2.00000])
	keys.append([ [ 0.00037, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 2.00000])
	keys.append([ [ 1.86385, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 2.00000])
	keys.append([ [ -0.18412, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 2.00000])
	keys.append([ [ 1.46953, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 2.00000])
	keys.append([ [ 1.01555, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 2.00000])
	keys.append([ [ 0.13035, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 2.00000])
	keys.append([ [ 0.00032, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 2.00000])
	keys.append([ [ -0.10734, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 2.00000])
	keys.append([ [ -0.00609, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 2.00000])
	keys.append([ [ -0.85440, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 2.00000])
	keys.append([ [ 2.11255, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 2.00000])
	keys.append([ [ -1.18944, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 2.00000])
	keys.append([ [ -0.00149, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 2.00000])
	keys.append([ [ 0.04146, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 2.00000])
	keys.append([ [ -0.84067, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 2.00000])
	keys.append([ [ 2.11255, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 2.00000])
	keys.append([ [ -1.18630, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 2.00000])
	keys.append([ [ -0.04291, [ 3, -0.66667, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.angleInterpolationBezier(names, times, keys);


def shakehead():
	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 0.40000, 0.80000, 1.06667])
	keys.append([ [ -0.60039, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.68259, [ 3, -0.13333, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.00771, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 0.40000, 0.80000, 1.06667])
	keys.append([ [ 0.04751, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.02604, [ 3, -0.13333, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.04598, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.post.angleInterpolationBezier(names, times, keys);


def r_kick():
	
	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 0.60000, 4.80000])
	keys.append([ [ 0.03491, [ 2, -0.20000, 0.00000], [ 2, 1.40000, 0.00000]], [ 0.03491, [ 2, -1.40000, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 0.60000, 4.80000])
	keys.append([ [ 0.13963, [ 2, -0.20000, 0.00000], [ 2, 1.40000, 0.00000]], [ 0.13963, [ 2, -1.40000, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 0.60000, 2.13333, 2.40000, 4.80000])
	keys.append([ [ 1.31460, [ 2, -0.20000, 0.00000], [ 2, 0.51111, 0.00000]], [ 2.08560, [ 2, -0.51111, 0.00000], [ 2, 0.08889, 0.00000]], [ 1.08210, [ 2, -0.08889, 0.00000], [ 2, 0.80000, 0.00000]], [ 1.31460, [ 2, -0.80000, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.60000, 4.80000])
	keys.append([ [ 0.40493, [ 2, -0.20000, 0.00000], [ 2, 1.40000, 0.00000]], [ 0.40493, [ 2, -1.40000, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.60000, 4.80000])
	keys.append([ [ 0.05211, [ 2, -0.20000, 0.00000], [ 2, 1.40000, 0.00000]], [ 0.05211, [ 2, -1.40000, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.60000, 4.80000])
	keys.append([ [ -0.44635, [ 2, -0.20000, 0.00000], [ 2, 1.40000, 0.00000]], [ -0.44635, [ 2, -1.40000, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.60000, 2.13333, 2.40000, 4.80000])
	keys.append([ [ 1.60461, [ 2, -0.20000, 0.00000], [ 2, 0.51111, 0.00000]], [ 1.02102, [ 2, -0.51111, 0.00000], [ 2, 0.08889, 0.00000]], [ 2.08560, [ 2, -0.08889, 0.00000], [ 2, 0.80000, 0.00000]], [ 1.60461, [ 2, -0.80000, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.60000, 2.13333, 2.40000, 4.80000])
	keys.append([ [ -0.37434, [ 2, -0.20000, 0.00000], [ 2, 0.51111, 0.00000]], [ -0.40143, [ 2, -0.51111, 0.02709], [ 2, 0.08889, -0.00471]], [ -0.47124, [ 2, -0.08889, 0.00000], [ 2, 0.80000, 0.00000]], [ -0.37434, [ 2, -0.80000, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.60000, 2.13333, 4.80000])
	keys.append([ [ 0.89275, [ 2, -0.20000, 0.00000], [ 2, 0.51111, 0.00000]], [ 1.08036, [ 2, -0.51111, 0.00000], [ 2, 0.88889, 0.00000]], [ 0.89275, [ 2, -0.88889, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.60000, 2.13333, 4.80000])
	keys.append([ [ 0.56609, [ 2, -0.20000, 0.00000], [ 2, 0.51111, 0.00000]], [ 0.64228, [ 2, -0.51111, 0.00000], [ 2, 0.88889, 0.00000]], [ 0.56609, [ 2, -0.88889, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 0.60000, 1.06667, 2.13333, 2.40000, 3.73333, 4.80000])
	keys.append([ [ -0.12217, [ 2, -0.20000, 0.00000], [ 2, 0.15556, 0.00000]], [ -0.12579, [ 2, -0.15556, 0.00000], [ 2, 0.35556, 0.00000]], [ -0.11505, [ 2, -0.35556, -0.00450], [ 2, 0.08889, 0.00112]], [ -0.10891, [ 2, -0.08889, -0.00057], [ 2, 0.44444, 0.00287]], [ -0.10472, [ 2, -0.44444, 0.00000], [ 2, 0.35556, 0.00000]], [ -0.12217, [ 2, -0.35556, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 0.60000, 1.06667, 2.13333, 4.80000])
	keys.append([ [ -0.01381, [ 2, -0.20000, 0.00000], [ 2, 0.15556, 0.00000]], [ 0.13963, [ 2, -0.15556, 0.00000], [ 2, 0.35556, 0.00000]], [ -0.02148, [ 2, -0.35556, 0.00000], [ 2, 0.88889, 0.00000]], [ -0.01381, [ 2, -0.88889, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 0.60000, 1.06667, 2.13333, 2.40000, 4.80000])
	keys.append([ [ -0.31416, [ 2, -0.20000, 0.00000], [ 2, 0.15556, 0.00000]], [ -0.31685, [ 2, -0.15556, 0.00043], [ 2, 0.35556, -0.00098]], [ -0.31839, [ 2, -0.35556, 0.00000], [ 2, 0.08889, 0.00000]], [ -0.08727, [ 2, -0.08889, 0.00000], [ 2, 0.80000, 0.00000]], [ -0.31416, [ 2, -0.80000, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 0.60000, 1.06667, 2.13333, 4.80000])
	keys.append([ [ 0.61087, [ 2, -0.20000, 0.00000], [ 2, 0.15556, 0.00000]], [ 0.60149, [ 2, -0.15556, 0.00000], [ 2, 0.35556, 0.00000]], [ 0.61376, [ 2, -0.35556, 0.00000], [ 2, 0.88889, 0.00000]], [ 0.61087, [ 2, -0.88889, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 0.60000, 1.06667, 2.13333, 4.80000])
	keys.append([ [ -0.31416, [ 2, -0.20000, 0.00000], [ 2, 0.15556, 0.00000]], [ -0.31839, [ 2, -0.15556, 0.00423], [ 2, 0.35556, -0.00966]], [ -0.40143, [ 2, -0.35556, 0.00000], [ 2, 0.88889, 0.00000]], [ -0.31416, [ 2, -0.88889, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 0.60000, 1.06667, 2.13333, 2.40000, 3.73333, 4.80000])
	keys.append([ [ 0.20944, [ 2, -0.20000, 0.00000], [ 2, 0.15556, 0.00000]], [ 0.19373, [ 2, -0.15556, 0.00000], [ 2, 0.35556, 0.00000]], [ 0.24435, [ 2, -0.35556, 0.00000], [ 2, 0.08889, 0.00000]], [ 0.24435, [ 2, -0.08889, 0.00000], [ 2, 0.44444, 0.00000]], [ 0.26180, [ 2, -0.44444, 0.00000], [ 2, 0.35556, 0.00000]], [ 0.03375, [ 2, -0.35556, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 0.60000, 2.13333, 2.40000, 3.73333, 4.80000])
	keys.append([ [ 0.00000, [ 2, -0.20000, 0.00000], [ 2, 0.51111, 0.00000]], [ -0.08727, [ 2, -0.51111, 0.00000], [ 2, 0.08889, 0.00000]], [ -0.01745, [ 2, -0.08889, 0.00000], [ 2, 0.44444, 0.00000]], [ -0.08727, [ 2, -0.44444, 0.00000], [ 2, 0.35556, 0.00000]], [ 0.04909, [ 2, -0.35556, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 0.60000, 2.13333, 2.40000, 3.73333, 4.80000])
	keys.append([ [ -0.31416, [ 2, -0.20000, 0.00000], [ 2, 0.51111, 0.00000]], [ 0.33161, [ 2, -0.51111, 0.00000], [ 2, 0.08889, 0.00000]], [ -0.79936, [ 2, -0.08889, 0.00000], [ 2, 0.44444, 0.00000]], [ -0.26180, [ 2, -0.44444, 0.00000], [ 2, 0.35556, 0.00000]], [ -0.31416, [ 2, -0.35556, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 0.60000, 2.13333, 2.40000, 3.73333, 4.80000])
	keys.append([ [ 0.61087, [ 2, -0.20000, 0.00000], [ 2, 0.51111, 0.00000]], [ 0.87616, [ 2, -0.51111, 0.00000], [ 2, 0.08889, 0.00000]], [ 0.62143, [ 2, -0.08889, 0.00307], [ 2, 0.44444, -0.01534]], [ 0.60609, [ 2, -0.44444, 0.00000], [ 2, 0.35556, 0.00000]], [ 0.61087, [ 2, -0.35556, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 0.60000, 2.13333, 2.40000, 3.73333, 4.80000])
	keys.append([ [ -0.31416, [ 2, -0.20000, 0.00000], [ 2, 0.51111, 0.00000]], [ -1.18645, [ 2, -0.51111, 0.00000], [ 2, 0.08889, 0.00000]], [ 0.28449, [ 2, -0.08889, 0.00000], [ 2, 0.44444, 0.00000]], [ -0.24435, [ 2, -0.44444, 0.08727], [ 2, 0.35556, -0.06981]], [ -0.31416, [ 2, -0.35556, 0.00000], [ 2, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 0.60000, 1.06667, 2.13333, 2.40000, 3.73333, 4.80000])
	keys.append([ [ 0.41888, [ 2, -0.20000, 0.00000], [ 2, 0.15556, 0.00000]], [ 0.78540, [ 2, -0.15556, 0.00000], [ 2, 0.35556, 0.00000]], [ 0.22689, [ 2, -0.35556, 0.00000], [ 2, 0.08889, 0.00000]], [ 0.23010, [ 2, -0.08889, -0.00321], [ 2, 0.44444, 0.01604]], [ 0.47124, [ 2, -0.44444, 0.00000], [ 2, 0.35556, 0.00000]], [ -0.05062, [ 2, -0.35556, 0.00000], [ 2, 0.00000, 0.00000]]])

	proxy.mot.angleInterpolationBezier(names, times, keys);

def nodhead(numofnodhead):
	for x in range (0,numofnodhead):
		names = list()
		times = list()
		keys = list()

		names.append("HeadYaw")
		times.append([ 0.33333, 0.66667])
		keys.append([ [ -0.01385, [ 3, -0.11111, 0.00000], [ 3, 0.11111, 0.00000]], [ -0.01385, [ 3, -0.11111, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("HeadPitch")
		times.append([ 0.33333, 0.66667])
		keys.append([ [ 0.35081, [ 3, -0.11111, 0.00000], [ 3, 0.11111, 0.00000]], [ 0.02757, [ 3, -0.11111, 0.00000], [ 3, 0.00000, 0.00000]]])

		proxy.mot.post.angleInterpolationBezier(names, times, keys);

def thinking(numofscratchhead):

	#names  = ['HeadPitch', 'HeadYaw']
	#angles  = [29.5 *22/(180*7), 15.0 *22/(180*7)]
	#fractionMaxSpeed  = 0.3
	#proxy.mot.post.setAngles(names, angles, fractionMaxSpeed)

	names = list()
	times = list()
	keys = list()

	names.append("LShoulderPitch")
	times.append([ 0.66667])
	keys.append([ [ 1.81161, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.66667])
	keys.append([ [ 0.21165, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.66667])
	keys.append([ [ -1.47422, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.66667])
	keys.append([ [ -0.52459, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.66667])
	keys.append([ [ -0.85440, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.66667])
	keys.append([ [ -0.15804, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.66667])
	keys.append([ [ 1.12745, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.66667])
	keys.append([ [ 1.44200, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.post.angleInterpolationBezier(names, times, keys);

	for x in range (0,numofscratchhead):
		names = list()
		times = list()
		keys = list()

		names.append("LShoulderPitch")
		times.append([ 0.26667, 0.53333])
		keys.append([ [ 1.81161, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 1.81161, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LShoulderRoll")
		times.append([ 0.26667, 0.53333])
		keys.append([ [ 0.20091, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.20091, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LElbowYaw")
		times.append([ 0.26667, 0.53333])
		keys.append([ [ -1.47422, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ -1.47422, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LElbowRoll")
		times.append([ 0.26667, 0.53333])
		keys.append([ [ -0.52459, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.52459, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RShoulderPitch")
		times.append([ 0.26667, 0.53333])
		keys.append([ [ -0.57674, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.78997, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RShoulderRoll")
		times.append([ 0.26667, 0.53333])
		keys.append([ [ -0.14270, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.14270, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RElbowYaw")
		times.append([ 0.26667, 0.53333])
		keys.append([ [ 1.06149, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 1.16273, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RElbowRoll")
		times.append([ 0.26667, 0.53333])
		keys.append([ [ 1.23951, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 1.39752, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

		proxy.mot.post.angleInterpolationBezier(names, times, keys);

def checkrobotpose():

	if(proxy.pose.getActualPoseAndTime()[0] == 'Crouch'):
		squat()
	else:
		standup()
	
def askingagainL():

	names = list()
	times = list()
	keys = list()

	names.append("LShoulderPitch")
	times.append([ 0.46667])
	keys.append([ -0.41269])

	names.append("LShoulderRoll")
	times.append([ 0.46667])
	keys.append([ 0.35278])

	names.append("LElbowYaw")
	times.append([ 0.46667])
	keys.append([ -1.08918])

	names.append("LElbowRoll")
	times.append([ 0.46667])
	keys.append([ -1.56207])

	names.append("LWristYaw")
	times.append([ 0.46667])
	keys.append([ 0.10427])

	names.append("LHand")
	times.append([ 0.46667])
	keys.append([ 0.00040])

	names.append("RShoulderPitch")
	times.append([ 0.46667])
	keys.append([ 2.06634])

	names.append("RShoulderRoll")
	times.append([ 0.46667])
	keys.append([ -0.52927])

	names.append("RElbowYaw")
	times.append([ 0.46667])
	keys.append([ 1.49561])

	names.append("RElbowRoll")
	times.append([ 0.46667])
	keys.append([ 0.45717])

	names.append("RWristYaw")
	times.append([ 0.46667])
	keys.append([ 0.02450])

	names.append("RHand")
	times.append([ 0.46667])
	keys.append([ 0.00031])

	names.append("HeadYaw")
	times.append([ 0.46667])
	keys.append([ -1.10759])

	names.append("HeadPitch")
	times.append([ 0.46667])
	keys.append([ -0.18566])

	proxy.mot.post.angleInterpolation(names, keys, times, True);

def handstraight():

	names = list()
	times = list()
	keys = list()

	names.append("LShoulderPitch")
	times.append([ 0.46667])
	keys.append([ 0.11501])

	names.append("LShoulderRoll")
	times.append([ 0.46667])
	keys.append([ 0.00873])

	names.append("LElbowYaw")
	times.append([ 0.46667])
	keys.append([ -1.85158])

	names.append("LElbowRoll")
	times.append([ 0.46667])
	keys.append([ -0.22699])

	names.append("LWristYaw")
	times.append([ 0.46667])
	keys.append([ 0.07973])

	names.append("LHand")
	times.append([ 0.46667])
	keys.append([ 0.00033])

	names.append("RShoulderPitch")
	times.append([ 0.46667])
	keys.append([ 0.17032])

	names.append("RShoulderRoll")
	times.append([ 0.46667])
	keys.append([ -0.00873])

	names.append("RElbowYaw")
	times.append([ 0.46667])
	keys.append([ 1.58611])

	names.append("RElbowRoll")
	times.append([ 0.46667])
	keys.append([ 0.31298])

	names.append("RWristYaw")
	times.append([ 0.46667])
	keys.append([ -0.00158])

	names.append("RHand")
	times.append([ 0.46667])
	keys.append([ 0.00036])

	proxy.mot.post.angleInterpolation(names, keys, times, True);

def openRHand():
	# Choregraphe bezier export in Python.
	names = list()
	times = list()
	keys = list()

	names.append("LShoulderPitch")
	times.append([ 0.60000])
	keys.append([ [ 1.42504, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.60000])
	keys.append([ [ 0.33130, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.60000])
	keys.append([ [ -1.38371, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.60000])
	keys.append([ [ -0.99552, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.60000])
	keys.append([ [ -1.11373, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.60000])
	keys.append([ [ 0.00006, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.60000])
	keys.append([ [ 1.04009, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.60000])
	keys.append([ [ -0.41115, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.60000])
	keys.append([ [ 2.08567, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.60000])
	keys.append([ [ 0.81766, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.60000])
	keys.append([ [ 0.14722, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.60000])
	keys.append([ [ 0.00005, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.post.angleInterpolationBezier(names, times, keys);

def openLHand():

	# Choregraphe bezier export in Python.
	names = list()
	times = list()
	keys = list()

	names.append("LShoulderPitch")
	times.append([ 0.66667])
	keys.append([ [ 1.24710, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.66667])
	keys.append([ [ 0.60896, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.66667])
	keys.append([ [ -2.07708, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.66667])
	keys.append([ [ -0.98018, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.66667])
	keys.append([ [ -1.04776, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.66667])
	keys.append([ [ 0.00006, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.66667])
	keys.append([ [ 1.44814, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.66667])
	keys.append([ [ -0.33139, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.66667])
	keys.append([ [ 1.38976, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.66667])
	keys.append([ [ 1.02782, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.66667])
	keys.append([ [ 0.09660, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.66667])
	keys.append([ [ 0.00005, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.post.angleInterpolationBezier(names, times, keys);

def openArm():

	# Choregraphe bezier export in Python.
	names = list()
	times = list()
	keys = list()

	names.append("LShoulderPitch")
	times.append([ 0.73333])
	keys.append([ [ 0.80684, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.73333])
	keys.append([ [ 0.53226, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.73333])
	keys.append([ [ -2.08567, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.73333])
	keys.append([ [ -0.92496, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.73333])
	keys.append([ [ -0.92965, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.73333])
	keys.append([ [ 0.00006, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.73333])
	keys.append([ [ 0.93732, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.73333])
	keys.append([ [ -0.58756, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.73333])
	keys.append([ [ 2.08006, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.73333])
	keys.append([ [ 0.82994, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.73333])
	keys.append([ [ 0.10120, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.73333])
	keys.append([ [ 0.00005, [ 3, -0.24444, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.post.angleInterpolationBezier(names, times, keys);

def protect():

	# Choregraphe bezier export in Python.
	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 1.00000])
	keys.append([ [ -0.00158, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 1.00000])
	keys.append([ [ -0.03686, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 1.00000])
	keys.append([ [ -0.81613, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 1.00000])
	keys.append([ [ 0.00873, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 1.00000])
	keys.append([ [ -0.58910, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 1.00000])
	keys.append([ [ -0.92649, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 1.00000])
	keys.append([ [ -1.25792, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 1.00000])
	keys.append([ [ 0.00005, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 1.00000])
	keys.append([ [ -0.38806, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 1.00000])
	keys.append([ [ -0.00873, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 1.00000])
	keys.append([ [ 1.01853, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 1.00000])
	keys.append([ [ 1.36530, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 1.00000])
	keys.append([ [ 0.09353, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 1.00000])
	keys.append([ [ 0.00004, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 1.00000])
	keys.append([ [ -0.00303, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 1.00000])
	keys.append([ [ -0.07666, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 1.00000])
	keys.append([ [ -0.96178, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 1.00000])
	keys.append([ [ 2.11255, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 1.00000])
	keys.append([ [ -1.18944, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 1.00000])
	keys.append([ [ 0.08288, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 1.00000])
	keys.append([ [ 0.01385, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 1.00000])
	keys.append([ [ -0.94345, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 1.00000])
	keys.append([ [ 2.11083, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 1.00000])
	keys.append([ [ -1.18630, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 1.00000])
	keys.append([ [ -0.00916, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.post.angleInterpolationBezier(names, times, keys);



def Mpoint():

	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ 0.00916, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ -0.05373, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ -0.02612, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ -0.16725, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ 1.39436, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ 1.42198, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ 0.31596, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ 0.31596, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ -1.36070, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ -1.38064, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ -0.99246, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ -0.99246, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ -0.68727, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ -0.68727, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.06667, 0.20000, 0.73333])
	keys.append([ [ 0.01745, [ 3, -0.02222, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.01745, [ 3, -0.04444, 0.00000], [ 3, 0.17778, 0.00000]], [ 0.00018, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ 1.41132, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ -0.17330, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ -0.34212, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ -0.13197, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ 1.37442, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ 0.06439, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ 1.02475, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ 0.13657, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.20000, 0.73333])
	keys.append([ [ 0.00763, [ 3, -0.06667, 0.00000], [ 3, 0.17778, 0.00000]], [ 0.00456, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.06667, 0.20000, 0.73333])
	keys.append([ [ 0.01745, [ 3, -0.02222, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.01745, [ 3, -0.04444, 0.00000], [ 3, 0.17778, 0.00000]], [ 0.00593, [ 3, -0.17778, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.angleInterpolationBezier(names, times, keys);


def handhip():

	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 0.26667])
	keys.append([ [ 0.01530, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 0.26667])
	keys.append([ [ -0.01078, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 0.26667])
	keys.append([ [ 1.25784, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.26667])
	keys.append([ [ 0.02450, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.26667])
	keys.append([ [ -0.46331, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.26667])
	keys.append([ [ -0.87280, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.26667])
	keys.append([ [ -0.68727, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.26667])
	keys.append([ [ 0.00020, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.26667])
	keys.append([ [ 1.46041, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.26667])
	keys.append([ [ -0.02612, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.26667])
	keys.append([ [ 0.75008, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.26667])
	keys.append([ [ 0.98180, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.26667])
	keys.append([ [ 0.00609, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.26667])
	keys.append([ [ 0.00034, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 0.26667])
	keys.append([ [ -0.00763, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 0.26667])
	keys.append([ [ -0.09200, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 0.26667])
	keys.append([ [ -0.92343, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 0.26667])
	keys.append([ [ 2.11255, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 0.26667])
	keys.append([ [ -1.18944, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 0.26667])
	keys.append([ [ 0.07674, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 0.26667])
	keys.append([ [ 0.01078, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 0.26667])
	keys.append([ [ -0.93271, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 0.26667])
	keys.append([ [ 2.11255, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 0.26667])
	keys.append([ [ -1.18630, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 0.26667])
	keys.append([ [ -0.00609, [ 3, -0.08889, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.angleInterpolationBezier(names, times, keys);

def squatopenarm():

	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 0.66667])
	keys.append([ [ 0.01376, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 0.66667])
	keys.append([ [ -0.01845, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 0.66667])
	keys.append([ [ 1.36982, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.66667])
	keys.append([ [ 0.01990, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.66667])
	keys.append([ [ -2.08567, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.66667])
	keys.append([ [ -1.53396, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.66667])
	keys.append([ [ -0.68574, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.66667])
	keys.append([ [ 0.00064, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.66667])
	keys.append([ [ 1.24872, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.66667])
	keys.append([ [ -0.02459, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.66667])
	keys.append([ [ 1.99109, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.66667])
	keys.append([ [ 1.18582, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.66667])
	keys.append([ [ 0.02757, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.66667])
	keys.append([ [ 0.00034, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 0.66667])
	keys.append([ [ -0.01223, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 0.66667])
	keys.append([ [ -0.09200, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 0.66667])
	keys.append([ [ -0.94030, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 0.66667])
	keys.append([ [ 2.11255, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 0.66667])
	keys.append([ [ -1.18944, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 0.66667])
	keys.append([ [ 0.07521, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 0.66667])
	keys.append([ [ 0.02305, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 0.66667])
	keys.append([ [ -0.94192, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 0.66667])
	keys.append([ [ 2.11255, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 0.66667])
	keys.append([ [ -1.18630, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 0.66667])
	keys.append([ [ -0.01683, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.angleInterpolationBezier(names, times, keys);

def thinking2():

	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.00763, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00763, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.01223, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.19478, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 1.42504, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 1.42504, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.32823, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.32823, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ -1.38678, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ -1.38831, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ -0.99246, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.99246, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ -0.67960, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.67960, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.00012, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00012, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 1.41592, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.56609, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ -0.31144, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.00873, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 1.37289, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.62583, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 1.04623, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 1.56207, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ -0.01692, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.24548, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.00019, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00035, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.00004, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00004, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.00004, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00004, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ -0.43561, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.43561, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.69946, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.69946, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ -0.34979, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.34826, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.00004, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00004, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.00004, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00158, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ -0.43723, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.43723, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ 0.69955, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.69801, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ -0.34971, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.34971, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 0.06667, 0.53333])
	keys.append([ [ -0.00149, [ 3, -0.02222, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.00149, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.angleInterpolationBezier(names, times, keys);

def excited(numofexcited):
	
	for x in range(0,numofexcited):

		names = list()
		times = list()
		keys = list()

		names.append("HeadYaw")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -0.48632, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.75929, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("HeadPitch")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -0.44490, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.47251, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LShoulderPitch")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -0.53081, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.27770, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LShoulderRoll")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.95104, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 1.05382, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LElbowYaw")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -0.84374, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -1.38678, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LElbowRoll")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -1.17807, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.37732, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LWristYaw")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -1.64142, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -1.63989, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LHand")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.00116, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00116, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RShoulderPitch")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -0.29295, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.50311, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RShoulderRoll")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -1.05083, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.94959, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RElbowYaw")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 1.38823, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.84673, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RElbowRoll")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.37741, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 1.17969, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RWristYaw")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -0.67807, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.67807, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RHand")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.00120, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00120, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LHipYawPitch")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -0.53993, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.54146, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LHipRoll")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.38508, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.01223, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LHipPitch")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.04453, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.25929, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LKneePitch")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.79917, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.21779, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LAnklePitch")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -0.48939, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.01837, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("LAnkleRoll")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ -0.12881, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.06285, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RHipRoll")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.01078, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.38806, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RHipPitch")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.26074, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.04444, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RKneePitch")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.21787, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.79926, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RAnklePitch")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.02152, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.49237, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("RAnkleRoll")
		times.append([ 1.00000, 2.00000])
		keys.append([ [ 0.06140, [ 3, -0.33333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.12890, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

		proxy.mot.angleInterpolationBezier(names, times, keys);

def hold_trolley():

	names = list()
	times = list()
	keys = list()

	names.append("LShoulderPitch")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ 1.42351, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ 1.42198, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ 0.34511, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.33130, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ -1.38678, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ -1.38218, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ -1.01853, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ -1.01853, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ 0.09200, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.09200, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ 0.00011, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00013, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ 0.70415, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.73636, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ -0.68421, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.15804, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ 0.37886, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.09055, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ 0.79005, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.12890, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ -0.01998, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.02459, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.66667, 1.66667])
	keys.append([ [ 0.01745, [ 3, -0.22222, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00000, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.angleInterpolationBezier(names, times, keys);

def falldown():

	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ -0.29764, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.42649, [ 3, -0.22222, 0.05113], [ 3, 0.13333, -0.03068]], [ -0.54308, [ 3, -0.13333, 0.03298], [ 3, 0.13333, -0.03298]], [ -0.62438, [ 3, -0.13333, 0.01813], [ 3, 0.11111, -0.01511]], [ -0.64279, [ 3, -0.11111, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.63972, [ 3, -0.15556, -0.00307], [ 3, 0.13333, 0.00263]], [ -0.57529, [ 3, -0.13333, -0.03422], [ 3, 0.15556, 0.03992]], [ -0.41729, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 0.37579, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.36198, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.41567, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.41567, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ 0.40187, [ 3, -0.11111, 0.00298], [ 3, 0.15556, -0.00418]], [ 0.39420, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.39420, [ 3, -0.13333, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.35431, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 1.11824, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.76542, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.76542, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.99706, [ 3, -0.13333, -0.09567], [ 3, 0.11111, 0.07972]], [ 1.29159, [ 3, -0.11111, -0.07350], [ 3, 0.15556, 0.10291]], [ 1.52629, [ 3, -0.15556, -0.09279], [ 3, 0.13333, 0.07953]], [ 1.80854, [ 3, -0.13333, -0.07741], [ 3, 0.15556, 0.09031]], [ 2.02944, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 0.36045, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.51385, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.51385, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.48163, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ 0.64577, [ 3, -0.11111, -0.04432], [ 3, 0.15556, 0.06204]], [ 0.80071, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.66265, [ 3, -0.13333, 0.05050], [ 3, 0.15556, -0.05892]], [ 0.47243, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ -0.55535, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.08901, [ 3, -0.22222, -0.12751], [ 3, 0.13333, 0.07651]], [ 0.05672, [ 3, -0.13333, -0.03094], [ 3, 0.13333, 0.03094]], [ 0.09660, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ -0.84988, [ 3, -0.11111, 0.22754], [ 3, 0.15556, -0.31856]], [ -1.54171, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ -1.04163, [ 3, -0.13333, -0.18479], [ 3, 0.15556, 0.21559]], [ -0.34059, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ -0.96331, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -1.18267, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.95257, [ 3, -0.13333, -0.07926], [ 3, 0.13333, 0.07926]], [ -0.70713, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ -0.80684, [ 3, -0.11111, 0.02514], [ 3, 0.15556, -0.03520]], [ -0.88814, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.49237, [ 3, -0.13333, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.65958, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 0.04291, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.70261, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.70261, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.70261, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ -0.70261, [ 3, -0.11111, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.70261, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.70261, [ 3, -0.13333, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.71335, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 0.00410, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00407, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00407, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00407, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ 0.00407, [ 3, -0.11111, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00407, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00407, [ 3, -0.13333, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00407, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 2.07861, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 2.07248, [ 3, -0.22222, 0.00614], [ 3, 0.13333, -0.00368]], [ 1.81630, [ 3, -0.13333, 0.05471], [ 3, 0.13333, -0.05471]], [ 1.74420, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ 2.04486, [ 3, -0.11111, -0.00877], [ 3, 0.15556, 0.01227]], [ 2.05714, [ 3, -0.15556, -0.00732], [ 3, 0.13333, 0.00628]], [ 2.08567, [ 3, -0.13333, 0.00000], [ 3, 0.15556, 0.00000]], [ 2.08015, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ -0.22707, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.49859, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.36053, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.52620, [ 3, -0.13333, 0.00184], [ 3, 0.11111, -0.00153]], [ -0.52774, [ 3, -0.11111, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.52160, [ 3, -0.15556, -0.00614], [ 3, 0.13333, 0.00526]], [ -0.49092, [ 3, -0.13333, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.53541, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 1.52936, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.04146, [ 3, -0.22222, 0.00256], [ 3, 0.13333, -0.00153]], [ -0.04299, [ 3, -0.13333, 0.00153], [ 3, 0.13333, -0.00153]], [ -0.07061, [ 3, -0.13333, 0.01701], [ 3, 0.11111, -0.01418]], [ -0.13657, [ 3, -0.11111, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.13657, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.10742, [ 3, -0.13333, -0.02915], [ 3, 0.15556, 0.03400]], [ 0.11808, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 0.02459, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.48172, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.31911, [ 3, -0.13333, 0.06571], [ 3, 0.13333, -0.06571]], [ 0.08748, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ 0.09055, [ 3, -0.11111, -0.00307], [ 3, 0.15556, 0.00430]], [ 0.20867, [ 3, -0.15556, -0.05424], [ 3, 0.13333, 0.04649]], [ 0.39275, [ 3, -0.13333, -0.05806], [ 3, 0.15556, 0.06773]], [ 0.58603, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 0.19631, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 1.04615, [ 3, -0.22222, -0.00256], [ 3, 0.13333, 0.00153]], [ 1.04768, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.04768, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ 1.04921, [ 3, -0.11111, 0.00000], [ 3, 0.15556, 0.00000]], [ 1.04615, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.04615, [ 3, -0.13333, 0.00000], [ 3, 0.15556, 0.00000]], [ 1.04768, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 0.00716, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00712, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00712, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00713, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ 0.00712, [ 3, -0.11111, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00712, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00712, [ 3, -0.13333, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00712, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ -0.39726, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.42181, [ 3, -0.22222, 0.02454], [ 3, 0.13333, -0.01473]], [ -0.67952, [ 3, -0.13333, 0.08105], [ 3, 0.13333, -0.08105]], [ -0.90809, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ -0.73935, [ 3, -0.11111, -0.04432], [ 3, 0.15556, 0.06204]], [ -0.58901, [ 3, -0.15556, -0.03442], [ 3, 0.13333, 0.02950]], [ -0.54760, [ 3, -0.13333, -0.00657], [ 3, 0.15556, 0.00767]], [ -0.53993, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 0.18259, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.31144, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.02612, [ 3, -0.13333, 0.09536], [ 3, 0.13333, -0.09536]], [ -0.26074, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ 0.00771, [ 3, -0.11111, -0.07713], [ 3, 0.15556, 0.10798]], [ 0.29457, [ 3, -0.15556, -0.07875], [ 3, 0.13333, 0.06750]], [ 0.44644, [ 3, -0.13333, -0.03611], [ 3, 0.15556, 0.04213]], [ 0.52927, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ -0.59668, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.86974, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.44022, [ 3, -0.13333, -0.14368], [ 3, 0.13333, 0.14368]], [ -0.00763, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ -0.25460, [ 3, -0.11111, 0.08565], [ 3, 0.15556, -0.11991]], [ -0.62430, [ 3, -0.15556, 0.15198], [ 3, 0.13333, -0.13027]], [ -1.10137, [ 3, -0.13333, 0.14302], [ 3, 0.15556, -0.16685]], [ -1.55390, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 2.11255, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 2.11255, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.96808, [ 3, -0.13333, 0.04888], [ 3, 0.13333, -0.04888]], [ 1.81928, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ 1.92820, [ 3, -0.11111, -0.02216], [ 3, 0.15556, 0.03102]], [ 1.97882, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.60299, [ 3, -0.13333, 0.13924], [ 3, 0.15556, -0.16245]], [ 1.07376, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ -1.18944, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -1.18944, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ -1.18944, [ 3, -0.13333, 0.00000], [ 3, 0.13333, 0.00000]], [ -1.18889, [ 3, -0.13333, -0.00055], [ 3, 0.11111, 0.00046]], [ -0.92198, [ 3, -0.11111, -0.09247], [ 3, 0.15556, 0.12945]], [ -0.52314, [ 3, -0.15556, -0.17594], [ 3, 0.13333, 0.15080]], [ 0.05825, [ 3, -0.13333, -0.19423], [ 3, 0.15556, 0.22660]], [ 0.73935, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 0.04299, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.07828, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.07521, [ 3, -0.13333, 0.00307], [ 3, 0.13333, -0.00307]], [ 0.04146, [ 3, -0.13333, 0.02733], [ 3, 0.11111, -0.02278]], [ -0.07512, [ 3, -0.11111, 0.06882], [ 3, 0.15556, -0.09634]], [ -0.45402, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.36505, [ 3, -0.13333, -0.04201], [ 3, 0.15556, 0.04901]], [ -0.18097, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ -0.13802, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.25614, [ 3, -0.22222, 0.03611], [ 3, 0.13333, -0.02167]], [ -0.31136, [ 3, -0.13333, 0.02071], [ 3, 0.13333, -0.02071]], [ -0.38039, [ 3, -0.13333, 0.03765], [ 3, 0.11111, -0.03138]], [ -0.51845, [ 3, -0.11111, 0.02685], [ 3, 0.15556, -0.03758]], [ -0.57367, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.57367, [ 3, -0.13333, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.53532, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ -0.76551, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.85908, [ 3, -0.22222, 0.06743], [ 3, 0.13333, -0.04046]], [ -1.08918, [ 3, -0.13333, 0.08539], [ 3, 0.13333, -0.08539]], [ -1.37144, [ 3, -0.13333, 0.08953], [ 3, 0.11111, -0.07461]], [ -1.58160, [ 3, -0.11111, 0.02958], [ 3, 0.15556, -0.04142]], [ -1.62301, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ -1.61995, [ 3, -0.13333, -0.00307], [ 3, 0.15556, 0.00358]], [ -1.54171, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 1.89760, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.77625, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.95879, [ 3, -0.13333, -0.06085], [ 3, 0.13333, 0.06085]], [ 1.14134, [ 3, -0.13333, 0.00000], [ 3, 0.11111, 0.00000]], [ 1.14134, [ 3, -0.11111, 0.00000], [ 3, 0.15556, 0.00000]], [ 1.15054, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.09992, [ 3, -0.13333, 0.01699], [ 3, 0.15556, -0.01982]], [ 1.04009, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ -0.72094, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.33599, [ 3, -0.22222, -0.13295], [ 3, 0.13333, 0.07977]], [ 0.41576, [ 3, -0.13333, -0.02020], [ 3, 0.13333, 0.02020]], [ 0.45717, [ 3, -0.13333, -0.04142], [ 3, 0.11111, 0.03451]], [ 0.66120, [ 3, -0.11111, -0.04495], [ 3, 0.15556, 0.06294]], [ 0.78085, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.74557, [ 3, -0.13333, 0.01062], [ 3, 0.15556, -0.01239]], [ 0.71182, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 0.86667, 1.53333, 1.93333, 2.33333, 2.66667, 3.13333, 3.53333, 4.00000])
	keys.append([ [ 0.21020, [ 3, -0.28889, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.50626, [ 3, -0.22222, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.31911, [ 3, -0.13333, 0.07440], [ 3, 0.13333, -0.07440]], [ 0.05987, [ 3, -0.13333, 0.06526], [ 3, 0.11111, -0.05439]], [ -0.03984, [ 3, -0.11111, 0.00767], [ 3, 0.15556, -0.01074]], [ -0.05058, [ 3, -0.15556, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.04606, [ 3, -0.13333, -0.03682], [ 3, 0.15556, 0.04295]], [ 0.18872, [ 3, -0.15556, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.angleInterpolationBezier(names, times, keys);



def trolley_handstobody():

	names = list()
	times = list()
	keys = list()

	names.append("HeadYaw")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ -0.27309, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.04146, [ 3, -0.15556, -0.07747], [ 3, 0.15556, 0.07747]], [ 0.19171, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.01530, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.01530, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.01530, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.01530, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.01530, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadPitch")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.42181, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.47396, [ 3, -0.15556, -0.01551], [ 3, 0.15556, 0.01551]], [ 0.51487, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.51487, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.51487, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.51487, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.51487, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.51487, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 2.00183, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 2.02484, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 1.50021, [ 3, -0.15556, 0.28212], [ 3, 0.08889, -0.16121]], [ 0.69486, [ 3, -0.08889, 0.03988], [ 3, 0.08889, -0.03988]], [ 0.65498, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.78076, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.71173, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.79610, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.49544, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.49237, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.64117, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.16410, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.18404, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.16103, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.17790, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.16410, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ -0.34979, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.33445, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ -1.09839, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.54921, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.76551, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.64739, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.81920, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ -0.69034, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ -0.63964, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.65804, [ 3, -0.15556, 0.00639], [ 3, 0.15556, -0.00639]], [ -0.67799, [ 3, -0.15556, 0.00911], [ 3, 0.08889, -0.00521]], [ -0.70100, [ 3, -0.08889, 0.00153], [ 3, 0.08889, -0.00153]], [ -0.70253, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.69946, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.70100, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ -0.69639, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ -0.63205, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.65199, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.64125, [ 3, -0.15556, -0.01074], [ 3, 0.08889, 0.00614]], [ -0.42036, [ 3, -0.08889, -0.00153], [ 3, 0.08889, 0.00153]], [ -0.41882, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.42036, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.42036, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ -0.42036, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.00048, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00048, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00044, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.00044, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.00043, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.00044, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.00044, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.00044, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 1.34383, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.46178, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.72869, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.72869, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.73176, [ 3, -0.08889, -0.00088], [ 3, 0.06667, 0.00066]], [ 0.73329, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.73329, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.73176, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ -0.84528, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.07828, [ 3, -0.15556, -0.06750], [ 3, 0.15556, 0.06750]], [ -0.01078, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.01231, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.01231, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.01231, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.01231, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ -0.01231, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.56600, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.34971, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.40340, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.40340, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.40340, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.40340, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.40340, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.40340, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.51086, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.69034, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.68114, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.68114, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.67807, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.67807, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.67807, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.67960, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.99246, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.48930, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.49697, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.49697, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.49697, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.49697, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.49697, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.49697, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.00128, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00128, [ 3, -0.15556, 0.00001], [ 3, 0.15556, -0.00001]], [ 0.00116, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.00116, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.00116, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.00116, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.00116, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.00116, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ -0.46476, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.44328, [ 3, -0.15556, -0.00537], [ 3, 0.15556, 0.00537]], [ -0.43255, [ 3, -0.15556, -0.00390], [ 3, 0.08889, 0.00223]], [ -0.42488, [ 3, -0.08889, -0.00665], [ 3, 0.08889, 0.00665]], [ -0.39266, [ 3, -0.08889, -0.00409], [ 3, 0.06667, 0.00307]], [ -0.38959, [ 3, -0.06667, -0.00102], [ 3, 0.06667, 0.00102]], [ -0.38653, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ -0.38653, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.34519, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.34519, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.34519, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.34519, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.34519, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.34519, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.34519, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.34519, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ -1.54163, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ -1.54163, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ -1.55543, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ -1.54776, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ -1.54776, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.54776, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.54776, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ -1.54776, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 1.11978, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 1.11978, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 1.11978, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 1.11978, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 1.11978, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.12131, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.11978, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 1.11978, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.92189, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.92189, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.92189, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.92189, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.92189, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.92189, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.92258, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.92258, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.00004, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00004, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00004, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.00456, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.00456, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.00456, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.00456, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ -0.00456, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ -0.30983, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.31136, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ -0.30829, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.30829, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ -0.30829, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.30983, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.30829, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ -0.30829, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ -1.57086, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ -1.56932, [ 3, -0.15556, -0.00051], [ 3, 0.15556, 0.00051]], [ -1.56779, [ 3, -0.15556, -0.00065], [ 3, 0.08889, 0.00037]], [ -1.56626, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ -1.56626, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.56626, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.56626, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ -1.56626, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 1.22264, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 1.21957, [ 3, -0.15556, 0.00153], [ 3, 0.15556, -0.00153]], [ 1.21344, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 1.21344, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 1.21344, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.21344, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.21344, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 1.21344, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.92351, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.92351, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.92351, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.92351, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.92351, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.92351, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.92351, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.92351, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 0.53333, 1.00000, 1.46667, 1.73333, 2.00000, 2.20000, 2.40000, 2.53333])
	keys.append([ [ 0.00004, [ 3, -0.17778, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.00004, [ 3, -0.15556, 0.00000], [ 3, 0.15556, 0.00000]], [ 0.01078, [ 3, -0.15556, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.01078, [ 3, -0.08889, 0.00000], [ 3, 0.08889, 0.00000]], [ 0.01078, [ 3, -0.08889, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.01231, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.01078, [ 3, -0.06667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.01231, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

	proxy.mot.angleInterpolation(names, keys, times, True);


def PeekAPoo():
	
	names = list()
	times = list()
	keys = list()
	
	names.append("HeadYaw")
	times.append([ 0.93333])
	keys.append([ [ 0.03677, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("HeadPitch")
	times.append([ 0.93333])
	keys.append([ [ -0.06600, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LShoulderPitch")
	times.append([ 0.93333])
	keys.append([ [ 0.15882, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LElbowYaw")
	times.append([ 0.93333])
	keys.append([ [ -0.68242, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LElbowRoll")
	times.append([ 0.93333])
	keys.append([ [ -1.54462, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LWristYaw")
	times.append([ 0.93333])
	keys.append([ [ -1.82387, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RShoulderPitch")
	times.append([ 0.93333])
	keys.append([ [ 0.15882, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RShoulderRoll")
	times.append([ 0.93333])
	keys.append([ [ -0.06807, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RElbowYaw")
	times.append([ 0.93333])
	keys.append([ [ 0.87266, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RElbowRoll")
	times.append([ 0.93333])
	keys.append([ [ 1.51669, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RWristYaw")
	times.append([ 0.93333])
	keys.append([ [ 1.62490, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipYawPitch")
	times.append([ 0.93333])
	keys.append([ [ -0.16103, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipRoll")
	times.append([ 0.93333])
	keys.append([ [ 0.12276, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipPitch")
	times.append([ 0.93333])
	keys.append([ [ 0.24855, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LKneePitch")
	times.append([ 0.93333])
	keys.append([ [ -0.09208, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LAnklePitch")
	times.append([ 0.93333])
	keys.append([ [ 0.06132, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LAnkleRoll")
	times.append([ 0.93333])
	keys.append([ [ -0.11041, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHipRoll")
	times.append([ 0.93333])
	keys.append([ [ -0.06132, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHipPitch")
	times.append([ 0.93333])
	keys.append([ [ 0.25767, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RKneePitch")
	times.append([ 0.93333])
	keys.append([ [ -0.09046, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RAnklePitch")
	times.append([ 0.93333])
	keys.append([ [ 0.06140, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RAnkleRoll")
	times.append([ 0.93333])
	keys.append([ [ 0.06907, [ 3, -0.31111, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	try:
		# uncomment the following line and modify the IP if you use this script outside Choregraphe.
		# motion = ALProxy("ALMotion", IP, 9559)
		
		proxy.mot.post.angleInterpolationBezier(names, times, keys);
	except BaseException, err:
		print err
	proxy.say.post("Peek")
	
		
	
	names = list()
	times = list()
	keys = list()
	
	names.append("HeadYaw")
	times.append([ 1.00000])
	keys.append([ [ 0.03677, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("HeadPitch")
	times.append([ 1.00000])
	keys.append([ [ -0.06600, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LShoulderPitch")
	times.append([ 1.00000])
	keys.append([ [ 0.01396, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LShoulderRoll")
	times.append([ 1.00000])
	keys.append([ [ 0.00873, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LElbowYaw")
	times.append([ 1.00000])
	keys.append([ [ -0.75922, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LElbowRoll")
	times.append([ 1.00000])
	keys.append([ [ -1.18159, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LWristYaw")
	times.append([ 1.00000])
	keys.append([ [ -1.82387, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHand")
	times.append([ 1.00000])
	keys.append([ [ 0.00209, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RShoulderPitch")
	times.append([ 1.00000])
	keys.append([ [ 0.01396, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RShoulderRoll")
	times.append([ 1.00000])
	keys.append([ [ -0.00873, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RElbowYaw")
	times.append([ 1.00000])
	keys.append([ [ 0.79587, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RElbowRoll")
	times.append([ 1.00000])
	keys.append([ [ 1.16588, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RWristYaw")
	times.append([ 1.00000])
	keys.append([ [ 1.49226, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHand")
	times.append([ 1.00000])
	keys.append([ [ 0.00489, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipYawPitch")
	times.append([ 1.00000])
	keys.append([ [ -0.16103, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipRoll")
	times.append([ 1.00000])
	keys.append([ [ 0.12276, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipPitch")
	times.append([ 1.00000])
	keys.append([ [ 0.25008, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LKneePitch")
	times.append([ 1.00000])
	keys.append([ [ -0.09208, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LAnklePitch")
	times.append([ 1.00000])
	keys.append([ [ 0.06132, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LAnkleRoll")
	times.append([ 1.00000])
	keys.append([ [ -0.11041, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHipRoll")
	times.append([ 1.00000])
	keys.append([ [ -0.06132, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHipPitch")
	times.append([ 1.00000])
	keys.append([ [ 0.25767, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RKneePitch")
	times.append([ 1.00000])
	keys.append([ [ -0.09200, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RAnklePitch")
	times.append([ 1.00000])
	keys.append([ [ 0.06140, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RAnkleRoll")
	times.append([ 1.00000])
	keys.append([ [ 0.06907, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	try:
		# uncomment the following line and modify the IP if you use this script outside Choregraphe.
		# motion = ALProxy("ALMotion", IP, 9559)
		
		proxy.mot.angleInterpolationBezier(names, times, keys);
	except BaseException, err:
		print err
	
		
	
	names = list()
	times = list()
	keys = list()
	
	names.append("HeadYaw")
	times.append([ 0.60000])
	keys.append([ [ 0.05211, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("HeadPitch")
	times.append([ 0.60000])
	keys.append([ [ -0.02612, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LShoulderPitch")
	times.append([ 0.60000])
	keys.append([ [ 0.35954, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LShoulderRoll")
	times.append([ 0.60000])
	keys.append([ [ 0.81332, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LElbowYaw")
	times.append([ 0.60000])
	keys.append([ [ -1.66853, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LElbowRoll")
	times.append([ 0.60000])
	keys.append([ [ -1.54462, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LWristYaw")
	times.append([ 0.60000])
	keys.append([ [ -1.18889, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHand")
	times.append([ 0.60000])
	keys.append([ [ 0.00297, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RShoulderPitch")
	times.append([ 0.60000])
	keys.append([ [ 0.35954, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RShoulderRoll")
	times.append([ 0.60000])
	keys.append([ [ -0.75398, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RElbowYaw")
	times.append([ 0.60000])
	keys.append([ [ 1.82038, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RElbowRoll")
	times.append([ 0.60000])
	keys.append([ [ 1.54462, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RWristYaw")
	times.append([ 0.60000])
	keys.append([ [ 1.04615, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHand")
	times.append([ 0.60000])
	keys.append([ [ 0.00489, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipYawPitch")
	times.append([ 0.60000])
	keys.append([ [ -0.12881, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipRoll")
	times.append([ 0.60000])
	keys.append([ [ 0.12276, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipPitch")
	times.append([ 0.60000])
	keys.append([ [ 0.33139, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LKneePitch")
	times.append([ 0.60000])
	keys.append([ [ -0.09233, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LAnklePitch")
	times.append([ 0.60000])
	keys.append([ [ 0.00149, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LAnkleRoll")
	times.append([ 0.60000])
	keys.append([ [ -0.11041, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHipRoll")
	times.append([ 0.60000])
	keys.append([ [ -0.06132, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHipPitch")
	times.append([ 0.60000])
	keys.append([ [ 0.28988, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RKneePitch")
	times.append([ 0.60000])
	keys.append([ [ -0.09233, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RAnklePitch")
	times.append([ 0.60000])
	keys.append([ [ 0.05373, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RAnkleRoll")
	times.append([ 0.60000])
	keys.append([ [ 0.06907, [ 3, -0.20000, 0.00000], [ 3, 0.00000, 0.00000]]])
	time.sleep(1)
	try:
		# uncomment the following line and modify the IP if you use this script outside Choregraphe.
		# motion = ALProxy("ALMotion", IP, 9559)
		
		proxy.mot.post.angleInterpolationBezier(names, times, keys);
	except BaseException, err:
		print err

	proxy.say.post("a	boo	")
	
def OhMyGod():
	# Choregraphe bezier export in Python.

	names = list()
	times = list()
	keys = list()
	
	names.append("HeadYaw")
	times.append([ 0.20000, 0.50000, 0.90000])
	keys.append([ [ 0.02604, [ 3, -0.06667, 0.00000], [ 3, 0.10000, 0.00000]], [ 0.01070, [ 3, -0.10000, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.01070, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("HeadPitch")
	times.append([ 0.20000, 0.50000, 0.90000])
	keys.append([ [ -0.53387, [ 3, -0.06667, 0.00000], [ 3, 0.10000, 0.00000]], [ 0.30718, [ 3, -0.10000, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.30718, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LShoulderPitch")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 1.31766, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.31766, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LShoulderRoll")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.51692, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.51692, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LElbowYaw")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ -1.17662, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ -1.17662, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LElbowRoll")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ -0.61049, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.61049, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LWristYaw")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ -1.59847, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ -1.59847, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHand")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.00023, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00023, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RShoulderPitch")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.79063, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.21642, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RShoulderRoll")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ -0.00873, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.01396, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RElbowYaw")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.83427, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.37874, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RElbowRoll")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 1.54462, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.54462, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RWristYaw")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.56374, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.45910, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHand")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.00977, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00873, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipYawPitch")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ -0.17177, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.17177, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipRoll")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.11663, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.11663, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LHipPitch")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.20253, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.20253, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LKneePitch")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ -0.09208, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.09208, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LAnklePitch")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.06439, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.06439, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("LAnkleRoll")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ -0.09967, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.09967, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHipRoll")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ -0.05825, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.05825, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RHipPitch")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.18864, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.18864, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RKneePitch")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ -0.09200, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.09200, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RAnklePitch")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.06754, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.06754, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	names.append("RAnkleRoll")
	times.append([ 0.50000, 0.90000])
	keys.append([ [ 0.06907, [ 3, -0.16667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.06907, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])
	
	
	proxy.mot.post.angleInterpolationBezier(names, times, keys);
	
	
	proxy.led.post.setIntensity("LeftFaceLedsGreen", 0.5)
	proxy.led.post.setIntensity("RightFaceLedsGreen", 0.5)
	proxy.say.post("oh my god")		


spin_right_corr = 1.12+.3

def TurnToLeft():
	proxy.mot.walkTo(0,0,1.35)

def TurnToRight():
	proxy.mot.walkTo(0,0,-1.35*spin_right_corr)
		
def TurnAround():
	proxy.mot.walkTo(0,0,2.5)
	
def Turn90CW():
	proxy.mot.walkTo(0,0,-1.25*spin_right_corr)
	
def Turn90CCW():
	proxy.mot.walkTo(0,0,1.25)
	
def TurnAroundBack():
	proxy.mot.walkTo(0,0,-2.5*spin_right_corr)	
	
def motion_walkCustomization():
	motionProxy = proxy.mot
	
	# Set NAO in stiffness On
	print 'Stiff - ON'
	proxy.mot.setStiffnesses("Body" , 0.8)
	proxy.led.post.fadeRGB('AllLeds', 0x00909428, 2.0)
	config.PoseInit(proxy.mot)
	
	# TARGET VELOCITY
	X         = 0.0
	Y         = 0.0
	Theta     = -0.48
	Frequency = 1.0
	
	# Defined a limp walk
	motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency,
	    [ # LEFT FOOT
	    ["StepHeight", 0.025],
	    ["MaxStepX", 0.06],
	    #["MaxStepY", 0.2],
	    ["MaxStepFrequency", 0.0],
	    ["TorsoWx", 0],
	    ["TorsoWy", 0] ],
	    [ # RIGHT FOOT
	    ["StepHeight", 0.025],
	    ["MaxStepX", 0.0594],
	    #["MaxStepY", 0.2],
	    ["MaxStepFrequency", 0.0],
	    ["TorsoWx", 0],
	    ["TorsoWy", 0] ] )
	time.sleep(5.07)
	
	# TARGET VELOCITY
	X1         = 0.5
	Y1         = 0.0
	Theta1     = 0.0
	Frequency = 1.0
	
	motionProxy.setWalkTargetVelocity(X1, Y1, Theta1, Frequency,
	    [ # LEFT FOOT
	    ["StepHeight", 0.025],
	    ["MaxStepX", 0.06],
	    #["MaxStepY", 0.001],
	    ["MaxStepFrequency", 0.0],
	    ["TorsoWx", 0],
	    ["TorsoWy", 0] ],
	    [ # RIGHT FOOT
	    ["StepHeight", 0.025],
	    ["MaxStepX", 0.0599],
	    ["MaxStepY", -0.03],
	    ["MaxStepFrequency", 0.0],
	    ["TorsoWx", 0],
	    ["TorsoWy", 0] ] )
	time.sleep(12.0)
	proxy.mot.stopWalk()
	standup() 
	proxy.mot.setWalkArmsEnable(True,False)

def walkCustomization(X1,Y1,Theta1):
	motionProxy = proxy.mot
	
	# Set NAO in stiffness On
	print 'Stiff - ON'
	#proxy.mot.setStiffnesses("Body" , 0.8)
	proxy.led.post.fadeRGB('AllLeds', 0x00909428, 2.0)
	#config.PoseInit(proxy.mot)
	'''
	 # TARGET VELOCITY
	X1         = 0.5
	Y1         = 0.0
	Theta1     = 0.0
	'''
	Frequency = 1.0
	
	motionProxy.post.setWalkTargetVelocity(X1, Y1, Theta1, Frequency,
	    [ # LEFT FOOT
	    ["StepHeight", 0.025],
	    ["MaxStepX", 0.06],
	    #["MaxStepY", 0.001],
	    ["MaxStepFrequency", 0.0],
	    ["TorsoWx", 0],
	    ["TorsoWy", 0] ],
	    [ # RIGHT FOOT
	    ["StepHeight", 0.025],
	    ["MaxStepX", 0.06],
	    #["MaxStepY", -0.03],
	    ["MaxStepFrequency", 0.0],
	    ["TorsoWx", 0],
	    ["TorsoWy", 0] ] )
	time.sleep(2)
	#proxy.mot.stopWalk()
#	standup() 
