from turtle import*
title('welcome')
addshape('khosha.gif')
shape('khosha.gif')
pu()
goto(-500,0)
tracer(0)
for v in range(10000):
    update()
    fd(0.3)
goto(0,0)    
pd()
print('سلام ')
print('خوش آمديدpaint artبه ')
print('در ابتدا نام فرم خودتون و در ادامه اطلاعات خواسته شده را وارد کنيد')
title('پيش فرض')
na=textinput('title','نام فرم شما؟')
if na==''or na==' ':
    title('پيش فرض')
else:
    title(na)
vn=textinput('پس زمينه','آيا پس زمينه خاصي مد نظرتان است')
if vn=='بله' or vn=='آره':
    bx=textinput('title','چه پس زمينه اي مد نظرتان است[kah1,kah2]')
    bgpic(bx+'.gif')
e=numinput('number','ارتفاع؟')
w=numinput('number','طول؟')
g=textinput('title','اسامي اشکال.شکل قلم[star,sun,po,bigane1,bigane2,stars]')
siz=numinput('numper','اندازه قلم؟')
col=textinput('title','رنگ پس زمينه؟')
cn=textinput('title','رنگ قلم')
sor=numinput('number','سرعت؟')
if not g=='star'or g=='sun' or g=='po' or g=='bigane1'or g=='bigane2'or g=='stars':
    addshape('po.gif')
    shape('po.gif')
else:
    addshape(g+'.gif')
    shape(g+'.gif')
bgcolor(col)
color(cn)
pensize(siz)
speed(sor)
setup(width=w,height=e)

    





    

        




