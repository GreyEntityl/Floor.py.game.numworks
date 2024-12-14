from ion import keydown as kd
from kandinsky import set_pixel as stp, draw_string as ds, get_pixel as gp, fill_rect as rect
from random import *
from time import sleep as sp, monotonic as mt
from math import *

def draw_floor(o,y=222):
  rect(0,0,320,220,(255,255,255))
  n="123456789"
  wtr = (30,40,190)
  dr = (105,55,34)
  gs = (1,255,1)
  sd = (203,189,147)
  lv = (255,1,1)
  rk = (85,85,85)
  dmd = (185,242,255)
  x=0
  k=0
  tmp=0
  while tmp <= o:
    tmp+=1
    top = '123654789##%%rr&'
    r=[]
    while len(r)<2:
      r.append(choice(top))
    s = randint(1,2)
    if s == 2:
      r.append(choice(top))  
    else:
      r.append(r[0])    
    r.pop(0)
    if len(r) < 3:
      i=r[0]
    else:
      i=r[1]
    if i in n:
      h=int(i)*4
      rect(x,y-h,4,h,dr)
      h=(int(i))*4
      rect(x,y-h-4,4,4,gs)
      l=randint(0,2)
      if l==0:
        rect(x+randint(0,2),y-h-6,2,2,choice([lv,dmd]))
    elif i=="#":
      h=randint(5,6)*4
      rect(x,y-h,4,h,wtr)
    elif i == "r":
      h=randint(5,10)*4
      rect(x,y-h,4,h,rk)  
    elif i=="&":
      l = randint(1,4)
      if l > 1:
        h=l*4
        rect(x,y-h,4,h,rk)
      else:
        l=randint(0,12)
        if l==6:
          h=randint(1,2)*4
          rect(x,y-h,4,h,dmd)
          p=(randint(4,10)*4)-h
          rect(x,y-(p+h),4,p,rk)
        else:
          h=randint(1,4)*4
          rect(x,y-h,4,h,lv)
    else:
      h=randint(5,7)*4
      rect(x,y-h,4,h,sd)
    x+=4
def finds(list,*find):
  findslen=len(find)
  values=[-1,]*findslen
  for i in list:
    f=0
    while f<findslen:
      values[f]+=(i==find[f])
      f+=1
  return values
def d_p(x,y,c=(160,160,255)):
  rect(x,y,4,8,c)

def e(x,y,n,i=1):
  h=0
  while i > h:
    try:
      c=n[h]
    except IndexError as e:
      c=n[0]
    rect(x,y+h*4,4,4,c)
    h+=1
        
def c():
  sp(0.05)

def menu():
  blocks=50
  display=1
  l=20
  m=1
  newd=0
  d=0
  e=-1
  d1=0
  d2=0
  cls={
    "Red":(255,1,1),
    "Blue":(1,1,255),
    "Green":(1,255,1),
    "White":(250,250,250),
    "Purple":(160,160,255),
    "Brown":(105,55,34),
    "Gray":(130,130,130),
    "Yellow":(245,245,10)
  }
  cs=list(cls.keys())
  csn=2
  c1=(245,245,255)
  c2=(160,160,255)
  c3=(90,90,160)
  rect(0,0,320,220,c1)
  xf,yf=40,25
  xnd,ynd=40,150
  mds=("Health bar","Hearts")
  dc=("No","Yes")
  ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
  ds("Start >",90,70,c3)
  ds("Config >",90,110,c3)
  ds("[!]New background >  "+dc[newd],xnd,ynd,c3)
  while True:
    if kd(1):
      e-=1
      sp(0.2)
    elif kd(2):
      e+=1
      sp(0.2)
    if e < -1:
      e=1
    if e > 1:
      e=-1
    if e==-1:
      ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
      ds("Start >",90,70,c2)
      ds("Config >",90,110,c3)
      ds("[!]New background >  "+dc[newd],xnd,ynd,c3)
      if kd(4) or kd(3):
        sp(0.1)
        ybm=220
        if newd:
          ybm=180
        rect(0,0,320,ybm,(255,255,255))
        break
    elif e==0:
      ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
      ds("Start >",90,70,c3)
      ds("Config >",90,110,c2)
      ds("[!]New background >  "+dc[newd],xnd,ynd,c3)
      if kd(4) or kd(3):
        d=True
        e=2
        rect(0,0,320,220,c1)
        if newd:
          draw_floor(80)
        ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))        
        ds("< Config",90,50,c2)
        ds("Lives >",90,90,c3)
        ds("Blocks >",90,130,c3)
        sp(0.2)
    elif e==1:
      ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
      ds("Start >",90,70,c3)
      ds("Config >",90,110,c3)  
      ds("[!]New background >  "+dc[newd],xnd,ynd,c2)
        
      if kd(0):
        newd+=1
        if newd>1:
          newd=0
          rect(90,150,300,20,c1)
        ds("[!]New background >  "+dc[newd],xnd,ynd,c2)
        sp(0.2)
      elif kd(3):
        newd-=1
        if newd<0:
          newd=1
        rect(90,150,300,20,c1)
        ds("[!]New background >  "+dc[newd],xnd,ynd,c2)
        sp(0.2)
      if kd(4):
        rect(0,0,320,240,c1)
        if newd:
          draw_floor(80)
        ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
        ds("Start >",90,70,c3)
        ds("Config >",90,110,c3)
        ds("[!]New background >  "+dc[newd],xnd,ynd,c2)
        while kd(4):
          pass
    if d:
      while d:
        if kd(1):
          e-=1
          sp(0.2)
        elif kd(2):
          e+=1
          sp(0.2)
        if e < 2:
          e=4
        elif e > 4:
          e=2
        if e==2:
          ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
          ds("< Config",90,50,c2)
          ds("Lives >",90,90,c3)
          ds("Blocks >",90,130,c3)
          if kd(0) or kd(4):
            d=False
            e=0
            rect(0,0,320,240,c1)
            if newd:
              draw_floor(80)
            ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
            ds("Start >",90,70,c3)
            ds("Config >",90,110,c2)
            ds("[!]New background >  "+dc[newd],xnd,ynd,c3)
            sp(0.2) 
        elif e==3:
          ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
          ds("< Config",90,50,c3)
          ds("Lives >",90,90,c2)
          ds("Blocks >",90,130,c3)
          if kd(3) or kd(4):
            d1=True
            e=5
            rect(0,0,320,240,c1)
            if newd:
              draw_floor(80)
            ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
            ds("< Lives",90,50,c2)
            ds("Lives >  "+str(l),90,90,c3)
            ds("Mode >  "+mds[m],90,130,c3)
            ds("Color >  "+cs[csn],90,170,c3)
            sp(0.2)
        elif e==4:
          ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
          ds("< Config",90,50,c3)
          ds("Lives >",90,90,c3)
          ds("Blocks >",90,130,c2)
          if kd(3) or kd(4):
            d2=True
            e=9
            rect(0,0,320,240,c1)
            if newd:
              draw_floor(80)
            ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
            ds("< Blocks",90,50,c2)
            ds("Blocks >  "+str(blocks),90,90,c3)
            ds("Display >  "+dc[display],90,130,c3)
            sp(0.2)
        while d1:
          if kd(1):
            e-=1
            sp(0.2)
          elif kd(2):
            e+=1
            sp(0.2)
          if e < 5:
            e=8
          elif e > 8:
            e=5
          if e==5:
            ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
            ds("< Lives",90,50,c2)
            ds("Lives >  "+str(l),90,90,c3)
            ds("Mode >  "+mds[m],90,130,c3)
            ds("Color >  "+cs[csn],90,170,c3)
            if kd(0) or kd(4):
              d1=False
              e=3
              rect(0,0,320,220,c1)
              if newd:
                draw_floor(80)
              ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
              ds("< Config",90,50,c3)
              ds("Lives >",90,90,c2)
              ds("Blocks >",90,130,c3)
              sp(0.2)
          elif e==6:
            ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
            ds("< Lives",90,50,c3)
            ds("Lives >  "+str(l),90,90,c2)
            ds("Mode >  "+mds[m],90,130,c3)
            ds("Color >  "+cs[csn],90,170,c3)
            if kd(0):
              l-=1
              if l<1:
                  l=31
              rect(90,90,250,20,c1)
              ds("Lives >  "+str(l),90,90,c2)
              sp(0.1)
            elif kd(3):
              l+=1
              if l>31:
                l=1
              rect(90,90,250,20,c1)
              ds("Lives >  "+str(l),90,90,c2)
              sp(0.1)
            
          elif e==7:
            ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
            ds("< Lives",90,50,c3)
            ds("Lives >  "+str(l),90,90,c3)
            ds("Mode >  "+mds[m],90,130,c2)
            ds("Color >  "+cs[csn],90,170,c3)
            if kd(0):
              m+=1
              if m>1:
                m=0
              rect(90,130,300,20,c1)
              ds("Mode >  "+mds[m],90,130,c2)
              sp(0.2)
            elif kd(3):
              m-=1
              if m<0:
                m=1
              rect(90,130,300,20,c1)
              ds("Mode >  "+mds[m],90,130,c2)
              sp(0.2)
          elif e==8:
            ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
            ds("< Lives",90,50,c3)
            ds("Lives >  "+str(l),90,90,c3)
            ds("Mode >  "+mds[m],90,130,c3)
            ds("Color >  "+cs[csn],90,170,c2)
            if kd(0):
              csn+=1
              if csn>len(cs)-1:
                csn=0
              rect(90,170,300,20,c1)
              ds("Color >  "+cs[csn],90,170,c2)
              sp(0.2)
            elif kd(3):
              csn-=1
              if csn<0:
                csn=len(cs)-1
              rect(90,170,300,20,c1)
              ds("Color >  "+cs[csn],90,170,c2)
              sp(0.2)
        while d2:
          if kd(1):
            e-=1
            sp(0.2)
          elif kd(2):
            e+=1
            sp(0.2)
          if e < 9:
            e=11
          elif e > 11:
            e=9
          if e==9:
            ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
            ds("< Blocks",90,50,c2)
            ds("Blocks >  "+str(blocks),90,90,c3)
            ds("Display >  "+dc[display],90,130,c3)
            if kd(0) or kd(4):
              d2=False
              e=4
              rect(0,0,320,240,c1)
              if newd:
                draw_floor(80)
              ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
              ds("< Config",90,50,c3)
              ds("Lives >",90,90,c3)
              ds("Blocks >",90,130,c2)
              sp(0.2)
          elif e==10:
            ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
            ds("< Blocks",90,50,c3)
            ds("Blocks >  "+str(blocks),90,90,c2)
            ds("Display >  "+dc[display],90,130,c3)
            if kd(0):
              blocks-=1
              if blocks<0:
                  blocks=100
              rect(90,90,350,20,c1)
              ds("Blocks >  "+str(blocks),90,90,c2)
              sp(0.1)
            elif kd(3):
              blocks+=1
              if blocks>100:
                blocks=0
              rect(90,90,350,20,c1)
              ds("Blocks >  "+str(blocks),90,90,c2)
              sp(0.1)
          elif e==11:
            ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
            ds("< Blocks",90,50,c3)
            ds("Blocks >  "+str(blocks),90,90,c3)
            ds("Display >  "+dc[display],90,130,c2)
            if kd(0):
              display+=1
              if display>1:
                display=0
              rect(90,130,300,20,c1)
              ds("Display >  "+dc[display],90,130,c2)
              sp(0.2)
            elif kd(3):
              display-=1
              if display<0:
                display=1
              rect(90,130,300,20,c1)
              ds("Display >  "+dc[display],90,130,c2)
              sp(0.2)
  global lastlives
  l=l*((1-m)*10)+(m*l)
  lastlives=l
  return l,m,blocks,display,cls[cs[csn]],newd
def d_l(lives,d_l_mode,color):
  x=4
  y=12
  if d_l_mode:
    rect(x-2,y-2,lastlives*8+1,7,(0,0,0))
  else:
    rect(x-2,y-2,lastlives+3,7,(0,0,0))
  i=0
  while i < lives:
    if d_l_mode:
      rect(x,y,4,4,color)
      x+=8
    else:
      rect(x,y,1,4,color)
      x+=1
    i+=1

def d_b(blks,color):
  x=4
  y=4
  rect(x-2,y-2,310,7,(0,0,0))
  if not blks==0:
    pb=int(blks/3.1)
    rect(x,y,pb,4,color)

class new_player:
  def __init__(self,x,y,lives,d_l_mode,blocks,isdisplay,color,newd):
    self.x=x
    self.y=y
    self.lives=lives
    self.d_l_mode=d_l_mode
    self.blocks=blocks
    self.isdisplay=isdisplay
    self.color=color
    self.isend=True
    self.is_in_start=True
    self.mi=[[(255,255,255)],[(255,255,255)]]
    self.newd=newd
    self.fall=0
    self.fps_targ=60
    self.lt=mt()
  def g_mi(self,s):
    return self.mi[s]
  def mi_pop(self,s):
    self.mi.pop(s)
  def mi_append(self,s):
    self.mi.append(s)
  def check(self):
    return self.isend
  def turn_over(self):
    if self.check():
      self.isend=False
  def s_x(self,xo):
    self.x=xo
  def s_y(self,yo):
    self.y=yo
  def s_lives(self,l):
    self.lives=l
  def s_blocks(self,b):
    self.blocks=b
  def g_x(self):
    return self.x
  def g_y(self):
    return self.y
  def g_lives(self):
    return self.lives
  def g_blocks(self):
    return self.blocks
  def g_d_l_mode(self):
    return self.d_l_mode
  def g_isdisplay(self):
    return self.isdisplay
  def g_color(self):
    return self.color
  def check_is_in_start(self):
    return self.is_in_start
  def turn_in_run(self):
    self.is_in_start=False
paramtrs=menu()
p=new_player(randint(0,316),randint(20,200),*paramtrs)
def move(lives,d_l_mode,blocks,isdisplay,color,newd):
  color=p.g_color()
  func1=gp
  func2=e
  mi_app,mi,mi_pop=p.mi_append,p.g_mi,p.mi_pop
  x,s_x=p.g_x,p.s_x
  y,s_y=p.g_y,p.s_y
  blocks,s_blocks=p.g_blocks,p.s_blocks
  lives,s_lives=p.g_lives,p.s_lives
  d_l_mode=p.g_d_l_mode()
  color=p.g_color()
  display=p.g_isdisplay()
  fps,globalfps=0,0.000000000000001
  if display:
    d_b(blocks(),color)
  if p.check_is_in_start():
    print("Starting...")
    p.turn_in_run()
    rect(x(),y()+8,4,4,(0,255,0))
  else:
    print("Restarting...")
  d_l(lives(),d_l_mode,color)
  b=-1
  isonwtr=0
  isnotonwtr=0
  isnotonf=False
  print("Success")
  while lives() > 0:
    b+=1
    if kd(51):
      stpt=mt()
      pte=0
      while pte<=7:
        rect(x(),y()+pte,4,1,(pte*11,pte*22,pte*30))
        pte+=1
      sp(0.2)
      while kd(51):
        pass
      while not kd(51):
        pass
      while kd(51):
        pass
      p.lt+=mt()-stpt
    if kd(45) or kd(4):
      if not blocks() <= 0:
        isnotonf=True
        i=0 
        while i < 4:
          j=0
          while j < 4:
            res=gp(i+x(),y()+8+j)
          
            if not res==(255,255,255):
              isnotonf=False
              break
            j+=1
          i+=1
        if isnotonf:
          s_blocks(blocks()-1)
          rect(x(),y()+8,4,4,(145,145,170))
          if display:
            d_b(blocks(),color)

    isonb=True
    resf=[]
    iter=0
    while iter < 4:
      floor=gp(x()+iter,y()+8)
      resf.append(floor)
      iter+=1
    fd=finds(resf,(255,255,255),(24,40,189))
    d,wfs=fd[0],fd[1]
    if kd(46) or kd(17):
      if d<3:
        bo=blocks()
        if bo<950:
          s_blocks(bo+1)
          rect(x(),y()+8,4,4,(255,255,255))
          sp(0.05)
          if display:
            d_b(blocks(),color)
      
    if not d>=3:
      if wfs>-1:
        p.fall=0
        c()
      else:
        p.fall/=4
        if p.fall>=4:
          p.fall/=4
          if d_l_mode:
            s_lives(lives()-int(p.fall))
          else:
             s_lives(lives()-int(p.fall*10))
          d_l(lives(),d_l_mode,color)
      isonb=False
    currentfps=1/(mt()-fps)
    globalfps=(currentfps+globalfps)/2
    #ds(str(currentfps)[:5],90,90)
    fps=mt()
    if isonb:
      mi_app([func1(x(),y()+8)])
      func2(x(),y(),mi(0),1)
      mi_pop(0)
      s_y(y()+1)
      d_p(x(),y())
      p.fall+=1
      continue
    mp=1+(3*(kd(12) or kd(52)))
    if kd(0):      
      mi_app([func1(x()-mp,y()),func1(x()-mp,y()+4)])
      func2(x(),y(),mi(0),2)
      mi_pop(0)
      s_x(x()-mp)
    elif kd(3):
      mi_app([func1(x()+4+mp,y()),func1(x()+4+mp,y()+4)])
      func2(x(),y(),mi(0),2)
      mi_pop(0)
      s_x(x()+mp)
    elif kd(1):
      mi_app([func1(x(),y()-4)])
      func2(x(),y()+4,mi(0))
      mi_pop(0)
      s_y(y()-4)
    elif kd(2):      
      mi_app([func1(x(),y()+8+(mp))])
      func2(x(),y(),mi(0))
      mi_pop(0)
      s_y(y()+mp)
    fall=0
    d_p(x(),y())
    
    c()
  end=mt()
  rect(x(),y(),4,8,(255,255,255))
  rect(x(),y()+4,8,4,(255,0,0))
  p.turn_over()
  s_lives(0)
  d_l(0,d_l_mode,color)
  ds("Game Over",100,80,(255,255,255),(255,0,0))
  gtime=end-p.lt
  tig=str(gtime)
  ds("Time in game : "+tig[:tig.find(".")+4]+"s",55,120,(255,255,255),(160,160,245))
  print("\n[-------{Game stats}--------]")
  print("[ For more time precision:  ]\n[ +",gtime,"      ]")
  print("[ Average fps reached:      ]\n[ +",globalfps,"      ]")
  print("[ Average time per lives :  ]\n[ +",gtime/lastlives,"     ]")
def init(n=True,lives=p.g_lives(),d_l_mode=p.g_d_l_mode(),blocks=p.g_blocks(),display=p.g_isdisplay(),color=p.g_color(),newd=p.newd):
  if n and not newd:draw_floor(80)
  while p.check():
    try:
      move(*paramtrs)
    except KeyboardInterrupt or NameError:
      init(False)

init(True,p.g_lives(),p.g_d_l_mode(),p.g_blocks(),p.g_isdisplay(),p.g_color())