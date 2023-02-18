from turtle import*
from tkinter import*
from pyautogui import*
from time import*

#perf_counter()
#addshape('khosha.gif')
#shape('khosha.gif')

#goto(-400,0)
#tracer()

#for p in range(800):
#    update()
#    fd(2)

#speed(7)
################################
#                              #
#             base             #
#                              #
################################
ol=Turtle()
addshape('po.gif')
ol.shape('po.gif')
win=Tk()
win.resizable(False,False)
win.title('Tool box')
win.geometry('300x450')
ab=StringVar()
ab.set('po')
def te():
    st=strftime('%H:%M:%S:%p')
    lbbb.config(text=st)
    lbbb.after(1000,te)
lbbb=Label(win,bg='yellow')
lbbb.pack()
te()
lb=Label(win,text='General settings',fg='white',bg='black')
lb.pack()
fram=Frame(win,relief=SUNKEN,bd=7)
lb1=Label(fram,text='Choosing the avatar')
lb1.pack()
fram.pack()
oo=OptionMenu(fram,ab,'mini h1','mini h2','mini h3','bigane1','po')
oo.pack()
###############################
def xx():
    aa=ab.get()
    bb=sc.get()
    cc=lx.get()
    addshape(aa+'.gif')
    ol.shape(aa+'.gif')
    ol.color(cc)
    ol.pensize(bb)  
def mh():
    win1=Toplevel(win)
    win1.title('Pen settings')
    win1.resizable(False,False)
    win1.geometry('300x450')
    fram1=Frame(win1,relief=SUNKEN,bd=7)
    fram1.pack()
    lb2=Label(fram1,text='Pen size')
    lb2.pack()
    sc=Scale(fram1,from_=1,to=20,fg='black',orient='horizontal')
    sc.pack()
    lb3=Label(fram1,text='Pen color')
    lb3.pack()
    sp=Spinbox(fram1,values=('green','blue','yellow','red','black','brown','pink','white','orange','gray'))
    sp.pack()
    def xxt():
        aa=ab.get()
        bb=sc.get()
        cc=sp.get()
        addshape(aa+'.gif')
        ol.shape(aa+'.gif')
        ol.color(cc)
        ol.pensize(bb)
    butt1=Button(win1,text='Done',command=xxt)
    butt1.pack()
    bl=Label(win1,text='Writing')
    bl.pack()
    frame2=Frame(win1,relief=SUNKEN,bd=7)
    frame2.pack()
    bl1=Label(frame2,text='please type your sentences down here!')
    bl1.pack()
    ent=Entry(frame2)
    ent.pack()
    bl4=Label(win1,text='Coloring')
    bl4.pack()
    frame3=Frame(win1,relief=SUNKEN,bd=10)
    frame3.pack()
    frame4=Frame(win1,relief=SUNKEN,bd=5)
    frame4.pack()
    def boi3():
        ol.begin_fill()
    def boi4():
        ol.end_fill()
    def pupu():
        ol.pu()
    def pdpd():
        ol.pd()
        
    buut3=Button(frame3,text='Start coloring',command=boi3)
    buut3.pack(side=RIGHT)
    buut4=Button(frame3,text='Finish coloring',command=boi4)
    buut4.pack(side=LEFT)
    buut5=Button(frame4,text='Pen up',command=pupu)
    buut6=Button(frame4,text='Pen down',command=pdpd)
    buut5.pack(side=RIGHT)
    buut6.pack(side=LEFT)
    def nvs():
        amd=ent.get()
        bb=sc.get()
        cc=sp.get()
        ol.color(cc)
        ol.write(amd,font=('arial',bb))
    buut=Button(frame2,text='Write',command=nvs)
    buut.pack()
        
def mh1():
    ###################################
    #                                 #
    #            commands             #
    #                                 #
    #                                 #
    ###################################
    
    def buu():
        bgcolor('blue')
    def g():
        bgcolor('green')
    def b():
        bgcolor('black')
    def r():
        bgcolor('red')
    def y():
        bgcolor('yellow')
    def br():
        bgcolor('brown')
    def p():
        bgcolor('pink')
    def wh():
        bgcolor('white')
    def gjk():
        title(e_n_t.get())
        setup(width=skk.get(),height=skk2.get())
    ###################################
    #                                 #
    #            front end            #
    #                                 #
    #                                 #
    ###################################
    w2=Toplevel(win)
    w2.title('Wall settings')
    w2.resizable(False,False)
    b_ll=Label(w2,text='Walls name')
    b_ll.pack()
    f_rm1=Frame(w2,relief=SUNKEN,bd=4)
    f_rm1.pack()
    e_n_t=Entry(f_rm1)
    e_n_t.pack()
    b_ll2=Label(f_rm1,text='Walls length')
    b_ll2.pack()
    skk=Scale(f_rm1,from_=150,to=700,orient='horizontal')
    skk.pack()
    b_ll2=Label(f_rm1,text='Walls width')
    b_ll2.pack()
    skk2=Scale(f_rm1,from_=150,to=700)
    skk2.pack(side=LEFT)
    b_l4=Button(f_rm1,text='done',command=gjk)
    b_l4.pack()
    bll=Label(w2,text='Background color')
    bll.pack()
    f_rm=Frame(w2,relief=SUNKEN,bd=7)
    f_rm.pack()
    buut7=Button(f_rm,text='    ',bg='green',activebackground='green',command=g)
    buut7.pack(side=LEFT)
    buut8=Button(f_rm,text='    ',bg='blue',activebackground='blue',command=buu)
    buut8.pack(side=LEFT)
    buut9=Button(f_rm,text='    ',bg='black',activebackground='black',command=b)
    buut10=Button(f_rm,text='    ',bg='red',activebackground='red',command=r)
    buut11=Button(f_rm,text='    ',bg='yellow',activebackground='yellow',command=y)
    buut9.pack(side=RIGHT)
    buut10.pack(side=RIGHT)
    buut11.pack(side=LEFT)
    buut12=Button(f_rm,text='    ',bg='brown',activebackground='brown',command=br)
    buut13=Button(f_rm,text='    ',bg='pink',activebackground='pink',command=p)
    buut14=Button(f_rm,text='    ',bg='white',activebackground='white',command=wh)
    buut14.pack(side=LEFT)
    buut12.pack(side=LEFT)
    buut13.pack(side=LEFT)
def mm3():
    ###########################
    #                         #
    #         tavabe          #
    #                         #
    ###########################
    def boi3():
        ol.begin_fill()
    def boi4():
        ol.end_fill()
    def mosall():
        for t in range(3):
            ol.fd(int(snpb.get()))
            ol.lt(120)
    def morab():
        for t in range(4):
            ol.fd(int(snpb.get()))
            ol.lt(90)
    def fivz():
        for ml in range(5):
            ol.fd(int(snpb.get()))
            ol.rt(360/5)
    def sixz():
        for vvv in range(6):
            ol.fd(int(snpb.get()))
            ol.rt(360/6)
    def ez():
        for nbnb in range(8):
            ol.fd(int(snpb.get()))
            ol.rt(360/8)
    def tez():
        for rttb in range(10):
            ol.fd(int(snpb.get()))
            ol.rt(360/10)
    def dbd():
        ol.circle(int(snpb.get()))
    ###################################
    #                                 #
    #            front end            #
    #                                 #
    #                                 #
    ###################################
    w_in=Toplevel(win)
    w_in.title('Drawing Shapes')
    w_in.resizable(False,False)
    lb_bb=Label(w_in,text='Size')
    lb_bb.pack()
    snpb=Spinbox(w_in,from_=15,to=120)
    snpb.pack()
    l_a_b=Label(w_in,text='Shapes')
    l_a_b.pack()
    fra_m1=Frame(w_in,relief=SUNKEN,bd=5)
    fra_m1.pack()
    b_uu_t=Button(fra_m1,text='Triangle',command=mosall)
    b_uu_t.pack()
    fra_m2=Frame(w_in,relief=SUNKEN,bd=5)
    fra_m2.pack()
    b_uu_t1=Button(fra_m2,text='Square',command=morab)
    b_uu_t1.pack(side=LEFT)
    b_uu_t2=Button(fra_m2,text='Circle',command=dbd)
    b_uu_t2.pack(side=RIGHT)
    fra_m3=Frame(w_in,relief=SUNKEN,bd=5)
    fra_m3.pack()
    fra_m4=Frame(w_in,relief=SUNKEN,bd=5)
    fra_m4.pack()
    b_uu_t4=Button(fra_m4,text='Panjzelii',command=fivz)
    b_uu_t4.pack(side=RIGHT)
    b_uu_t5=Button(fra_m4,text='Sheshzelii',command=sixz)
    b_uu_t5.pack(side=LEFT)
    b_uu_t6=Button(fra_m4,text='Hashtzelii',command=ez)
    b_uu_t6.pack()
    b_uu_t7=Button(fra_m4,text='Dahzelii',command=tez)
    b_uu_t7.pack()
    frame_3=Frame(w_in,relief=SUNKEN,bd=10)
    frame_3.pack()
    buut3=Button(frame_3,text='Start coloring',command=boi3)
    buut3.pack(side=RIGHT)
    buut4=Button(frame_3,text='Finish coloring',command=boi4)
    buut4.pack()
    b_u1=Button(w_in,text='Delete',command=clcl)
    b_u1.pack(side=LEFT)
    b_u2=Button(w_in,text='Return',command=udud)
    b_u2.pack(side=RIGHT)
def bb():
    img=screenshot('SCREEN.jpeg')
def bbt():
    img=screenshot('SCREEN.jpeg')
onkey(bbt,'C')
listen()
def rah():
    wi_nn=Toplevel(win)
    wi_nn.title('guide')
    wi_nn.resizable(False,False)
    lcv=Label(wi_nn,text='Screen shots guide',fg='white',bg='gray')
    lcv.pack()
    lcv1=Label(wi_nn,text='You can take an screen shot in two ways')
    lcv1.pack()
    lcv2=Label(wi_nn,text='First one : ')
    lcv2.pack()
    fraam=Frame(wi_nn,relief=SUNKEN,bd=6,bg='black')
    fraam.pack()
    lcv3=Label(fraam,text='You can choose the screen shot from the menu',fg='white',bg='black')
    lcv3.pack()
    lcv4=Label(fraam,text='and',fg='white',bg='black')
    lcv4.pack()
    lcv5=Label(fraam,text='by choosing the screen shot option',fg='white',bg='black')
    lcv5.pack()
    lcv6=Label(fraam,text='you are able to take an screen shot!',fg='white',bg='black')
    lcv6.pack()
    lcv7=Label(wi_nn,text='Second one : ')
    lcv7.pack()
    fraam1=Frame(wi_nn,relief=SUNKEN,bd=6)
    fraam1.pack()
    lcv8=Label(fraam1,text='By pressing the shift + C keyboard',fg='white',bg='black')
    lcv8.pack()
    lcv9=Label(fraam1,text='You can take an screen shot',fg='white',bg='black')
    lcv9.pack()
    lcv10=Label(wi_nn,text='!! Warning !!' , fg = 'black' , bg = 'red')
    lcv10.pack()
    lcv10=Label(wi_nn,text='Be careful before pressing these two buttons')
    lcv10.pack()
    lcv11=Label(wi_nn,text='the painting canvas should be on choosing mode')
    lcv11.pack()
    lcv12=Label(wi_nn,text='and before taking the screen shots')
    lcv12.pack()
    lcv13=Label(wi_nn,text='remove the previous screen shot in Paint Wall folder')
    lcv13.pack()
def fgk():
    ww_ii=Toplevel(win)
    ww_ii.title('Developers')
    ww_ii.resizable(False,False)
    lb_bl=Label(ww_ii,text='Developers')
    lb_bl.pack()
    lb_b4=Label(ww_ii,text='* * * * * * * * * * * * *',fg='red')
    lb_b4.pack()
    lb_bl1=Label(ww_ii,text='^ILIA NAGHDI^')
    lb_bl1.pack()
    lb_b2=Label(ww_ii,text='*AMIR ALI ERFANI*')
    lb_b2.pack()
    lb_b6=Label(ww_ii,text='* * * * * * * * * * * * *',fg='red')
    lb_b6.pack()
    lb_b3=Label(ww_ii,text='Proud of the Paint Wall development team!')
    lb_b3.pack()
def rahnb():
    ww_ni=Toplevel(win)
    ww_ni.title('Apps guide')
    ww_ni.resizable(False,False)
    lco=Label(ww_ni,text='*  *  *  *  *  *  *  *  *  * *')
    lco.pack()
    lco1=Label(ww_ni,text='* Wellcome to Paint Wall *')
    lco1.pack()
    lco2=Label(ww_ni,text='*  *  *  *  *  *  *  *  *  * *')
    lco2.pack()
    frt=Frame(ww_ni,relief=SUNKEN,bd=5)
    frt.pack()
    lco3=Label(frt,text='in this app we tried to')
    lco3.pack()
    lco4=Label(frt,text='develope a simple UI')
    lco4.pack()
    lco5=Label(frt,text='for doing your tasks easier')
    lco5.pack()
    lco6=Label(frt,text='and it lets you to')
    lco6.pack()
    lco7=Label(frt,text='draw without any difficulties')
    lco7.pack()
    lco8=Label(frt,text='*  *  *  *  *  *  *  *  *  *  *  *')
    lco8.pack()
    lco9=Label(frt,text='The app doesnt have any ambiguity')
    lco9.pack()
    lco10=Label(frt,text='and with settings you can')
    lco10.pack()
    lco11=Label(frt,text='change the walls color, pen and .... that you like!')
    lco11.pack()
    lco12=Label(ww_ni,text='!A little warning!')
    lco12.pack()
    frt1=Frame(ww_ni,relief=SUNKEN,bd=5)
    frt1.pack()
    lco12=Label(frt1,text='Click the done button after you')
    lco12.pack()
    ###################################
    #                                 #
    #            front end            #
    #                                 #
    #                                 #
    ###################################    
lb2=Label(fram,text='Pen size')
lb2.pack()
sc=Scale(fram,from_=1,to=20,fg='black',orient='horizontal')
sc.pack()
lb3=Label(fram,text='Pen color')
lb3.pack()
lx=Spinbox(fram,values=('green','blue','yellow','red','black','brown','pink','white','orange','gray'))
lx.pack()
def clcl():
    ol.clear()
def udud():
    ol.undo()
butt=Button(win,text='Done',command=xx)
butt.pack()
fmr=Frame(win,relief=SUNKEN,bd=4)
fmr.pack()
b_u1=Button(fmr,text='Clear',command=clcl)
b_u1.pack(side=LEFT)
b_u2=Button(fmr,text='Return',command=udud)
b_u2.pack(side=RIGHT)
frm2=Frame(win,relief=SUNKEN,bd=4)
frm2.pack()
def htht():
    ol.ht()
def shsh():
    ol.st()
b_u3=Button(frm2,text='Show',command=shsh)
b_u3.pack(side=RIGHT)
b_u4=Button(frm2,text='Hide',command=htht)
b_u4.pack(side=LEFT)
menub=Menu(win)
win.config(menu=menub)
m1=Menu(menub,tearoff=0)
m1.add_command(label='Pen settings',command=mh)
m1.add_command(label='Wall settings',command=mh1)
m1.add_command(label='Drawing shapes',command=mm3)
menub.add_cascade(label='Appearance settings',menu=m1)
m2=Menu(menub,tearoff=0)
m2.add_command(label='screenshot (shift+c)',command=bb)
m2.add_command(label='guide',command=rah)
menub.add_cascade(label='screenshot',menu=m2)
m3=Menu(menub,tearoff=0)
m3.add_command(label='Developers',command=fgk)
m3.add_command(label='Apps guide',command=rahnb)
menub.add_cascade(label='Application',menu=m3)
    ###################################
    #                                 #
    #            starting             #
    #                                 #
    #                                 #
    ###################################
title('Default')

#####################################################
#                                                   #
#               tavab'a barname 1                   #
#                                                   #
#                                                   #
#####################################################
def clicked(x,y):
    ol.goto(x,y)        
ol.onclick(clicked)
listen()
#####################################################
#                                                   #
#               tavab'a barname 2                   #
#                                                   #
#                                                   #
#####################################################
def harkat(x,y):
    ol.ondrag(None)
    ol.setheading(towards(x, y))
    ol.goto(x,y)
    ol.ondrag(harkat)
ol.speed(20)    
ol.ondrag(harkat)
#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#
def tooll():
    win=Tk()
    win.resizable(False,False)
    win.title('Tool box')
    win.geometry('500x400')
    ab=StringVar()
    ab.set('po')
    def te():
        st=strftime('%H:%M:%S:%p')
        lbbb.config(text=st)
        lbbb.after(1000,te)
    lbbb=Label(win,bg='blue')
    lbbb.pack()
    te()
    lb=Label(win,text='General settings',fg='white',bg='black')
    lb.pack()
    fram=Frame(win,relief=SUNKEN,bd=7)
    lb1=Label(fram,text='Choosing the avatar')
    lb1.pack()
    fram.pack()
    oo=OptionMenu(fram,ab,'mini h1','mini h2','mini h3','bigane1','po')
    oo.pack()
    

    def xx():
        aa=ab.get()
        bb=sc.get()
        cc=lx.get()
        addshape(aa+'.gif')
        ol.shape(aa+'.gif')
        ol.color(cc)
        ol.pensize(bb)  
    def mh():
        win1=Toplevel(win)
        win1.title('Pen settings')
        win1.resizable(False,False)
        win1.geometry('300x400')
        fram1=Frame(win1,relief=SUNKEN,bd=7)
        fram1.pack()
        lb2=Label(fram1,text='Pen size')
        lb2.pack()
        sc=Scale(fram1,from_=1,to=20,fg='black',orient='horizontal')
        sc.pack()
        lb3=Label(fram1,text='Pen color')
        lb3.pack()
        sp=Spinbox(fram1,values=('green','blue','yellow','red','black','brown','pink','white','orange','gray'))
        sp.pack()
        def xxt():
            aa=ab.get()
            bb=sc.get()
            cc=sp.get()
            addshape(aa+'.gif')
            ol.shape(aa+'.gif')
            ol.color(cc)
            ol.pensize(bb)
        butt1=Button(win1,text='Done',command=xxt)
        butt1.pack()
        bl=Label(win1,text='Writing')
        bl.pack()
        frame2=Frame(win1,relief=SUNKEN,bd=7)
        frame2.pack()
        bl1=Label(frame2,text='please type your sentences down here!')
        bl1.pack()
        ent=Entry(frame2)
        ent.pack()
        bl4=Label(win1,text='Coloring')
        bl4.pack()
        frame3=Frame(win1,relief=SUNKEN,bd=10)
        frame3.pack()
        frame4=Frame(win1,relief=SUNKEN,bd=5)
        frame4.pack()
        def boi3():
            ol.begin_fill()
        def boi4():
            ol.end_fill()
        def pupu():
            ol.pu()
        def pdpd():
            ol.pd()
            
        buut3=Button(frame3,text='Start coloring',command=boi3)
        buut3.pack(side=RIGHT)
        buut4=Button(frame3,text='Finish coloring',command=boi4)
        buut4.pack(side=LEFT)
        buut5=Button(frame4,text='Pen up',command=pupu)
        buut6=Button(frame4,text='Pen down',command=pdpd)
        buut5.pack(side=RIGHT)
        buut6.pack(side=LEFT)
        def nvs():
            amd=ent.get()
            bb=sc.get()
            cc=sp.get()
            ol.color(cc)
            ol.write(amd,font=('arial',bb))
        buut=Button(frame2,text='Write',command=nvs)
        buut.pack()
            
    def mh1():
        ###################################
        #                                 #
        #            commands             #
        #                                 #
        #                                 #
        ###################################
        def buu():
            bgcolor('blue')
        def g():
            bgcolor('green')
        def b():
            bgcolor('black')
        def r():
            bgcolor('red')
        def y():
            bgcolor('yellow')
        def br():
            bgcolor('brown')
        def p():
            bgcolor('pink')
        def wh():
            bgcolor('white')
        def gjk():
            title(e_n_t.get())
            setup(width=skk.get(),height=skk2.get())
        ###################################
        #                                 #
        #            front end            #
        #                                 #
        #                                 #
        ###################################
        w2=Toplevel(win)
        w2.title('Wall settings')
        w2.resizable(False,False)
        b_ll=Label(w2,text='Walls name')
        b_ll.pack()
        f_rm1=Frame(w2,relief=SUNKEN,bd=4)
        f_rm1.pack()
        e_n_t=Entry(f_rm1)
        e_n_t.pack()
        b_ll2=Label(f_rm1,text='Walls length')
        b_ll2.pack()
        skk=Scale(f_rm1,from_=150,to=700,orient='horizontal')
        skk.pack()
        b_ll2=Label(f_rm1,text='Walls width')
        b_ll2.pack()
        skk2=Scale(f_rm1,from_=150,to=700)
        skk2.pack(side=LEFT)
        b_l4=Button(f_rm1,text='done',command=gjk)
        b_l4.pack()
        bll=Label(w2,text='Background color')
        bll.pack()
        f_rm=Frame(w2,relief=SUNKEN,bd=7)
        f_rm.pack()
        buut7=Button(f_rm,text='    ',bg='green',activebackground='green',command=g)
        buut7.pack(side=LEFT)
        buut8=Button(f_rm,text='    ',bg='blue',activebackground='blue',command=buu)
        buut8.pack(side=LEFT)
        buut9=Button(f_rm,text='    ',bg='black',activebackground='black',command=b)
        buut10=Button(f_rm,text='    ',bg='red',activebackground='red',command=r)
        buut11=Button(f_rm,text='    ',bg='yellow',activebackground='yellow',command=y)
        buut9.pack(side=RIGHT)
        buut10.pack(side=RIGHT)
        buut11.pack(side=LEFT)
        buut12=Button(f_rm,text='    ',bg='brown',activebackground='brown',command=br)
        buut13=Button(f_rm,text='    ',bg='pink',activebackground='pink',command=p)
        buut14=Button(f_rm,text='    ',bg='white',activebackground='white',command=wh)
        buut14.pack(side=LEFT)
        buut12.pack(side=LEFT)
        buut13.pack(side=LEFT)
    def mm3():
        ###########################
        #                         #
        #         tavabe          #
        #                         #
        ###########################
        def boi3():
            ol.begin_fill()
        def boi4():
            ol.end_fill()
        def mosall():
            for t in range(3):
                ol.fd(int(snpb.get()))
                ol.lt(120)
        def morab():
            for t in range(4):
                ol.fd(int(snpb.get()))
                ol.lt(90)
        def fivz():
            for ml in range(5):
                ol.fd(int(snpb.get()))
                ol.rt(360/5)
        def sixz():
            for vvv in range(6):
                ol.fd(int(snpb.get()))
                ol.rt(360/6)
        def ez():
            for nbnb in range(8):
                ol.fd(int(snpb.get()))
                ol.rt(360/8)
        def tez():
            for rttb in range(10):
                ol.fd(int(snpb.get()))
                ol.rt(360/10)
        def dbd():
            ol.circle(int(snpb.get()))
        ###################################
        #                                 #
        #            front end            #
        #                                 #
        #                                 #
        ###################################
        w_in=Toplevel(win)
        w_in.title('Drawing shapes')
        w_in.resizable(False,False)
        lb_bb=Label(w_in,text='Size')
        lb_bb.pack()
        snpb=Spinbox(w_in,from_=15,to=120)
        snpb.pack()
        l_a_b=Label(w_in,text='Shapes')
        l_a_b.pack()
        fra_m1=Frame(w_in,relief=SUNKEN,bd=5)
        fra_m1.pack()
        b_uu_t=Button(fra_m1,text='Triangle',command=mosall)
        b_uu_t.pack()
        fra_m2=Frame(w_in,relief=SUNKEN,bd=5)
        fra_m2.pack()
        b_uu_t1=Button(fra_m2,text='Square',command=morab)
        b_uu_t1.pack(side=LEFT)
        b_uu_t2=Button(fra_m2,text='Circle',command=dbd)
        b_uu_t2.pack(side=RIGHT)
        fra_m3=Frame(w_in,relief=SUNKEN,bd=5)
        fra_m3.pack()
        fra_m4=Frame(w_in,relief=SUNKEN,bd=5)
        fra_m4.pack()
        b_uu_t4=Button(fra_m4,text='Panjzelii',command=fivz)
        b_uu_t4.pack(side=RIGHT)
        b_uu_t5=Button(fra_m4,text='Sheshzelii',command=sixz)
        b_uu_t5.pack(side=LEFT)
        b_uu_t6=Button(fra_m4,text='Hashtzelii',command=ez)
        b_uu_t6.pack()
        b_uu_t7=Button(fra_m4,text='Dahzelii',command=tez)
        b_uu_t7.pack()
        frame_3=Frame(w_in,relief=SUNKEN,bd=10)
        frame_3.pack()
        buut3=Button(frame_3,text='Start coloring',command=boi3)
        buut3.pack(side=RIGHT)
        buut4=Button(frame_3,text='Finish coloring',command=boi4)
        buut4.pack()
        b_u1=Button(w_in,text='Delete',command=clcl)
        b_u1.pack(side=LEFT)
        b_u2=Button(w_in,text='Return',command=udud)
        b_u2.pack(side=RIGHT)
    def bb():
        img=screenshot('SCREEN.jpeg')
    def bbt():
        img=screenshot('SCREEN.jpeg')
    onkey(bbt,'C')
    listen()
    def rah():
        wi_nn=Toplevel(win)
        wi_nn.title('guide')
        wi_nn.resizable(False,False)
        lcv=Label(wi_nn,text='Screen shots guide',fg='white',bg='black')
        lcv.pack()
        lcv1=Label(wi_nn,text='You can take an screen shot in two ways')
        lcv1.pack()
        lcv2=Label(wi_nn,text='First one : ')
        lcv2.pack()
        fraam=Frame(wi_nn,relief=SUNKEN,bd=6,bg='black')
        fraam.pack()
        lcv3=Label(fraam,text='You can choose the screen shot from the menu',fg='white',bg='black')
        lcv3.pack()
        lcv4=Label(fraam,text='and',fg='white',bg='black')
        lcv4.pack()
        lcv5=Label(fraam,text='by choosing the screen shot option',fg='white',bg='black')
        lcv5.pack()
        lcv6=Label(fraam,text='you are able to take an screen shot!',fg='white',bg='black')
        lcv6.pack()
        lcv7=Label(wi_nn,text='Second one : ')
        lcv7.pack()
        fraam1=Frame(wi_nn,relief=SUNKEN,bd=6)
        fraam1.pack()
        lcv8=Label(fraam1,text='By pressing the shift + C keyboard',fg='white',bg='black')
        lcv8.pack()
        lcv9=Label(fraam1,text='You can take an screen shot',fg='white',bg='black')
        lcv9.pack()
        lcv10=Label(wi_nn,text='!! Warning !!')
        lcv10.pack()
        lcv10=Label(wi_nn,text='Be careful before pressing these two buttons')
        lcv10.pack()
        lcv11=Label(wi_nn,text='the painting canvas should be on choosing mode')
        lcv11.pack()
        lcv12=Label(wi_nn,text='^and before taking the screen shots ^')
        lcv12.pack()
        lcv13=Label(wi_nn,text='remove the previous screen shot in Paint Wall folder')
        lcv13.pack()
    def fgk():
        ww_ii=Toplevel(win)
        ww_ii.title('Developers')
        ww_ii.resizable(False,False)
        lb_bl=Label(ww_ii,text='Developers')
        lb_bl.pack()
        lb_b4=Label(ww_ii,text='* * * * * * * * * * * * *',fg='red')
        lb_b4.pack()
        lb_bl1=Label(ww_ii,text='^ILIA NAGHDI^')
        lb_bl1.pack()
        lb_b2=Label(ww_ii,text='*AMIR ALI ERFANI*')
        lb_b2.pack()
        lb_b6=Label(ww_ii,text='* * * * * * * * * * * * *',fg='red')
        lb_b6.pack()
        lb_b3=Label(ww_ii,text='Proud of the Paint Wall development team!')
        lb_b3.pack()
    def rahnb():
        ww_ni=Toplevel(win)
        ww_ni.title('Apps guide')
        ww_ni.resizable(False,False)
        lco=Label(ww_ni,text='*  *  *  *  *  *  *  *  *  * *')
        lco.pack()
        lco1=Label(ww_ni,text='* Wellcome to Paint Wall *')
        lco1.pack()
        lco2=Label(ww_ni,text='*  *  *  *  *  *  *  *  *  * *')
        lco2.pack()
        frt=Frame(ww_ni,relief=SUNKEN,bd=5)
        frt.pack()
        lco3=Label(frt,text='in this app we tried to')
        lco3.pack()
        lco4=Label(frt,text='develope a simple UI')
        lco4.pack()
        lco5=Label(frt,text='for making your jobs easier')
        lco5.pack()
        lco6=Label(frt,text='and it lets you to')
        lco6.pack()
        lco7=Label(frt,text='draw your paint without any difficulties')
        lco7.pack()
        lco8=Label(frt,text='*  *  *  *  *  *  *  *  *  *  *  *')
        lco8.pack()
        lco9=Label(frt,text='The app doesnt have any ambiguity')
        lco9.pack()
        lco10=Label(frt,text='and with settings you can')
        lco10.pack()
        lco11=Label(frt,text='change the walls color, pen and .... that you like!')
        lco11.pack()
        lco12=Label(ww_ni,text='!A little warning!')
        lco12.pack()
        frt1=Frame(ww_ni,relief=SUNKEN,bd=5)
        frt1.pack()
        lco12=Label(frt1,text='Click the done button after you')
        lco12.pack()
        ###################################
        #                                 #
        #            front end            #
        #                                 #
        #                                 #
        ###################################    
    lb2=Label(fram,text='Pen size')
    lb2.pack()
    sc=Scale(fram,from_=1,to=20,fg='black',orient='horizontal')
    sc.pack()
    lb3=Label(fram,text='Pen color')
    lb3.pack()
    lx=Spinbox(fram,values=('green','blue','yellow','red','black','brown','pink','white','orange','gray'))
    lx.pack()
    def clcl():
        ol.clear()
    def udud():
        ol.undo()
    butt=Button(win,text='Done',command=xx)
    butt.pack()
    fmr=Frame(win,relief=SUNKEN,bd=4)
    fmr.pack()
    b_u1=Button(fmr,text='Clear',command=clcl)
    b_u1.pack(side=LEFT)
    b_u2=Button(fmr,text='Return',command=udud)
    b_u2.pack(side=RIGHT)
    frm2=Frame(win,relief=SUNKEN,bd=4)
    frm2.pack()
    def htht():
        ol.ht()
    def shsh():
        ol.st()
    b_u3=Button(frm2,text='Show',command=shsh)
    b_u3.pack(side=RIGHT)
    b_u4=Button(frm2,text='Hide',command=htht)
    b_u4.pack(side=LEFT)
    menub=Menu(win)
    win.config(menu=menub)
    m1=Menu(menub,tearoff=0)
    m1.add_command(label='Pen settings',command=mh)
    m1.add_command(label='Wall settings',command=mh1)
    m1.add_command(label='Drawing shapes',command=mm3)
    menub.add_cascade(label='Appearance settings',menu=m1)
    m2=Menu(menub,tearoff=0)
    m2.add_command(label='screenshot (shift+c)',command=bb)
    m2.add_command(label='guide',command=rah)
    menub.add_cascade(label='screenshot',menu=m2)
    m3=Menu(menub,tearoff=0)
    m3.add_command(label='Developers',command=fgk)
    m3.add_command(label='Apps guide',command=rahnb)
    menub.add_cascade(label='Application',menu=m3)
onkey(tooll,'T')
listen()
