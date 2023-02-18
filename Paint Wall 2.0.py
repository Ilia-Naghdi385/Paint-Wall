from turtle import*

def syyyss():
    bye()
    print('Hope to see you again')
onkey(syyyss,'space')
listen()

def cli():
    undo()
onkey(cli,'u')
listen()
u=getshapes()
pu()
addshape('khosha.gif')
shape('khosha.gif')

goto(-400,0)
tracer()

for p in range(600):
    update()
    fd(2)

print('Hi there !')
print('say hello to Paint Wall !')
print('first enter your forms name and then fill out other requests !')
title('Default')
na=textinput('title','Your tabs name ?!')

if na==''or na==' ':
    title('default')
else:
    title(na)
e=numinput('number','height ?!',600,minval=300,maxval=700)
w=numinput('number','width',600,minval=300,maxval=700)
g=textinput('title','Pens shape,choose : [[mini h3,mini h1,po,bigane1,mini h2]')
while g=='khosha' or g!='po' or g!='bigane1' or g!='mini h1' or g!='mini h2' or g!='mini h1' or g!='mini h3':

    if g=='po' or g=='mini h1' or g=='mini h2' or g=='mini h3' or g=='bigane1':
        break

    else:
        print('Please choose your pen shape from the list')
        g=textinput('title','Choose your pen shape[mini h3,mini h1,po,bigane1,mini h2]')

addshape(g+'.gif')
shape(g+'.gif')
goto(0,0)
pd()

siz=numinput('numper','Pens size ?!')
col=textinput('title','Back ground color ?!')
cn=textinput('title','Pens color ?!')
sor=numinput('number','Speed')
bgcolor(col)
color(cn)
pensize(siz)
speed(sor)
setup(width=w,height=e)
#####################################################
#                                                   #
#               tavab'a barname 1                   #
#                                                   #
#                                                   #
#####################################################
def ranga():
    color('olive')
    begin_fill()
onkey(ranga,'S')
listen()
#####################################################
#                                                   #
#               tavab'a barname 2                   #
#                                                   #
#                                                   #
#####################################################
def endd():
    end_fill()
onkey(endd,'P')
listen()
#####################################################
#                                                   #
#               tavab'a barname 3                   #
#                                                   #
#                                                   #
#####################################################
def clicked(x,y):
    goto(x,y)        
onclick(clicked)
listen()
#####################################################
#                                                   #
#               tavab'a barname 4                   #
#                                                   #
#                                                   #
#####################################################
def harkat(x,y):
    ondrag(None)
    setheading(towards(x, y))
    goto(x,y)
    ondrag(harkat)
speed(20)    
ondrag(harkat)
#####################################################
#                                                   #
#               tavab'a barname 5                   #
#                                                   #
#                                                   #
#####################################################
def fzelea():
    vk=textinput('Pen color','choose your pen color :')
    color(vk)
onkey(fzelea,'c')
listen()
#####################################################
#                                                   #
#               tavab'a barname 6                   #
#                                                   #
#                                                   #
#####################################################
def daeere():
    o=numinput('Darwing circle','Circles size')
    circle(o)
onkey(daeere,'d')
listen()
#####################################################
#                                                   #
#               tavab'a barname 7                   #
#                                                   #
#                                                   #
#####################################################
def nzelee():
    andaze=numinput('size','your sides size :')
    for ml in range(5):
        fd(andaze)
        rt(360/5)
onkey(nzelee,'p')
listen()
#####################################################
#                                                   #
#               tavab'a barname 8                   #
#                                                   #
#                                                   #
#####################################################
def ms():
    zz=numinput('triangles angle size ','tell us the angles ?! ')
    cv=zz-180

    while zz*3<180 or zz*3>180:
        print('ERROR ,Please enter the correct angle !')
        zz=numinput('triangles angle size ','tell us the angles ?! ')
    nn=numinput('triangles angle size ','tell us the angles ?! ')

    for ww in range(3):
        fd(nn)
        lt(cv)

onkey(ms,'3')
listen()
#####################################################
#                                                   #
#               tavab'a barname 9                   #
#                                                   #
#                                                   #
#####################################################
def ghalamm():
    bj=textinput('Pen size','your pen size : ')
    pensize(bj)
onkey(ghalamm,'r')
listen()
#####################################################
#                                                   #
#               tavab'a barname 10                  #
#                                                   #
#                                                   #
#####################################################
def tipee():
    cooo=textinput('color','Enter your typing color : ')
    uyu=textinput('Writing','type your writing : ')
    sizet=textinput('size','Your writing size : ')
    color(cooo)
    write(uyu,font=('arial',sizet))
onkey(tipee,'t')
listen()
#####################################################
#                                                   #
#               tavab'a barname 11                  #
#                                                   #
#                                                   #
#####################################################
def puuu():
    pu()
    print('The pen has been disappeared ! ')
onkey(puuu,'e')
listen()
#####################################################
#                                                   #
#               tavab'a barname 12                  #
#                                                   #
#                                                   #
#####################################################
def pddd():
    pd()
    print('The pen has been appeared')
onkey(pddd,'y')
listen()
#####################################################
#                                                   #
#               tavab'a barname 13                  #
#                                                   #
#                                                   #
#####################################################
def avatar():
    g=textinput('title','Pen shape . shapes name : [[mini h3,mini h1,po,bigane1,mini h2]')
    while g=='khosha' or g!='po' or g!='bigane1' or g!='mini h1' or g!='mini h2' or g!='mini h1' or g!='mini h3':
        if g=='po' or g=='mini h1' or g=='mini h2' or g=='mini h3' or g=='bigane1':
            addshape(g+'.gif')
            shape(g+'.gif')
            print('the logo has been changed ! ')
            break
        else:
            print('Please use the define shape !')
            g=textinput('title','Pens shape . shapes name : [mini h3,mini h1,po,bigane1,mini h2]')
onkey(avatar,'A')
listen()
#####################################################
#                                                   #
#               tavab'a barname 14                  #
#                                                   #
#                                                   #
#####################################################
def glo():
    fd(5)
onkey(glo,'w')
listen()
def aghab():
    bk(5)
onkey(aghab,'s')
listen()
def rast():
    rt(10)
onkey(rast,'d')
listen()
def chap():
    lt(10)
onkey(chap,'a')
listen()
#####################################################
#                                                   #
#               tavab'a barname 15                  #
#                                                   #
#                                                   #
#####################################################
def safhe():
    lot=textinput('back ground color ','Choose your back ground color : ')
    na=textinput('title','Your forms name ?!')
    if na==''or na==' ':
        title('default')
    else:
        title(na)
    e=numinput('number','Height ?',600,minval=300,maxval=700)
    w=numinput('number','Width ?',600,minval=300,maxval=700)
    setup(width=w,height=e)
onkey(safhe,'g')
listen()
