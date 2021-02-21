from vpython import *

G=6.67e-11 #重力常數
RE=6.378e6 #地球半徑
ME=5.972e24 #地球質量

Earth = sphere(pos=vector(0,0,0),radius=RE, texture=textures.earth) #地球物件
Earth.m = ME #地球物件質量
Earth.p=Earth.m*vector(0,0,0) #地球物件重心

sat=sphere(pos=vector(0,0,RE+20180000),radius=0.02*RE, make_trail=True) #線條物件
sat.m=774 #線條質量
v0 = 3700 #切線初速度
sat.p=sat.m*vector(0,v0,0) #線條物件重心

while True:
    rate(10000) #線條產生速率
    r1= sat.pos - Earth.pos #線條與地球半徑差
    F1= -G * Earth.m *sat.m *norm(r1) / mag(r1)**2 #重力
    sat.p=sat.p+F1 #線條物件重心隨位置改變
    sat.pos += sat.p  / sat.m #線條物件位置
