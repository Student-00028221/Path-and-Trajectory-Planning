from ctypes import RTLD_GLOBAL
import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

# link lengths in mm
a1 = float(input("a1 = ")) # For testing, 100 mm
a2 = float(input("a2 = ")) # For testing, 70 mm
a3 = float(input("a3 = ")) # For testing, 40 mm

# link mm to meters converter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)

# link limits converted to meters
lm3 = float(input("lm3 = "))
lm3 = mm_to_meter(lm3)


# Create Links
# [robot variable]=DHRobot([RevoluteDH(d,r/a,alpha,offset),PrismaticDH(theta,r/a,alpha,offset)])
Sphe_Modern = DHRobot([
    RevoluteDH(a1,0,(90/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,a2,(90/180)*np.pi,(90/180)*np.pi,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    PrismaticDH(0,0,0,a3,qlim=[0,lm3]),
], name='Spherical')

print(Sphe_Modern)


# degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi


# q Paths
q0 = np.array([0,0,0])
q1 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                mm_to_meter(float(input("d3 = ")))])
q2 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                mm_to_meter(float(input("d3 = ")))])
q3 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                mm_to_meter(float(input("d3 = ")))])
q4 = np.array([0,0,0])

# Trajectory commands
traj1 = rtb.jtraj(q0,q1,50)
#print(traj1)
#print(traj1.q)
traj2 = rtb.jtraj(q1,q2,50)
#print(traj2)
#print(traj2.q)
traj3 = rtb.jtraj(q2,q3,50)
#print(traj3)
#print(traj3.q)
traj4 = rtb.jtraj(q3,q4,50)
#print(traj4)
#print(traj4.q)

#plot scale
x1 = -0.2
x2 = 0.2
y1 = -0.2
y2 = 0.2
z1 = -0.2
z2 = 0.2


# for Joint Variable vs Time(s) table
rtb.qplot(traj1.q)
rtb.qplot(traj2.q)
rtb.qplot(traj3.q)
rtb.qplot(traj4.q)

Sphe_Modern.plot(traj1.q, limits = [x1, x2, y1, y2, z1, z2],movie='Spherical1.gif')
Sphe_Modern.plot(traj2.q, limits = [x1, x2, y1, y2, z1, z2],movie='Spherical2.gif')
Sphe_Modern.plot(traj3.q, limits = [x1, x2, y1, y2, z1, z2],movie='Spherical3.gif')
Sphe_Modern.plot(traj4.q, limits = [x1, x2, y1, y2, z1, z2],movie='Spherical4.gif')

#plot commands
Sphe_Modern.teach(jointlabels=1) # for teach