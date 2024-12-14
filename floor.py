from ion import keydown as kd
from kandinsky import set_pixel as stp, draw_string as ds, get_pixel as gp, fill_rect as rect
from random import *
from time import sleep as sp, monotonic as mt

def draw_floor(o):
  rect(0,0,240,320,(255,255,255))
  n="123456789"
  wtr = (30,40,190)
  dr = (105,55,34)
  gs = (1,255,1)
  sd = (203,189,147)
  lv = (255,1,1)
  rk = (85,85,85)
  dmd = (200,200,255)
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
    y=222#x=320
    if i in n:
      h=int(i)*4
      rect(x,y-h,4,h,dr)
      h=(int(i))*4
      rect(x,y-h-4,4,4,gs)
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
          h=randint(2,4)*4
          rect(x,y-h,4,h,dmd)
        else:
          h=randint(1,4)*4
          rect(x,y-h,4,h,lv)
    else:
      h=6*4
      rect(x,y-h,4,h,sd)
    x+=4
def finds(list,find):
  rs=-1
  for i in list:
    if i == find:
      rs+=1
  return rs
  
def d_p(x,y,c=(160,160,255)):
  rect(x,y,4,8,c)

def e(x,y,n,i=1):
  h=0
  while i > h:
    try:
      c=n[h]
    except IndexError:
      c=n[0]
    rect(x,y+h*4,4,4,c)
    h+=1
    

def ne(x,y,p,i):
  t=0
  m=0
  n,m=0,0
  while m < x+8:
    while n < y+12:
      if not n > 4 or n < 12 or m > 4 or m < 8:
        stp(x+m,y+n,p[t])
        t+=1
      n+=1
    m+=1
    
def c():
  sp(0.05)

def ngp(x,y):
  result=[]
  n,m=0,0
  while m < x+8:
    while n < y+12:
      if not n > 4 or n < 12 or m > 4 or m < 8:
        result.append(gp(x+m,y+n))
      n+=1
    m+=1
  return result

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
    "White":(255,255,255),
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
  xnd,ynd=40,170
  mds=("Health bar","Hearts")
  dc=("No","Yes")
  ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
  ds("Start >",90,90,c3)
  ds("Config >",90,130,c3)
  ds("[!]New background >  "+dc[newd],xnd,ynd,c3)
  if newd:
    draw_floor(80)
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
      ds("Start >",90,90,c2)
      ds("Config >",90,130,c3)
      ds("[!]New background >  "+dc[newd],xnd,ynd,c3)
      if kd(4) or kd(3):
        sp(0.1)
        rect(0,0,320,220,(255,255,255))
        break
    elif e==0:
      ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
      ds("Start >",90,90,c3)
      ds("Config >",90,130,c2)
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
      ds("Start >",90,90,c3)
      ds("Config >",90,130,c3)  
      ds("[!]New background >  "+dc[newd],xnd,ynd,c2)
        
      if kd(0):
        newd+=1
        if newd>1:
          newd=0
          rect(90,170,300,20,c1)
        ds("[!]New background >  "+dc[newd],xnd,ynd,c2)
        sp(0.2)
      elif kd(3):
        newd-=1
        if newd<0:
          newd=1
        rect(90,170,300,20,c1)
        ds("[!]New background >  "+dc[newd],xnd,ynd,c2)
        sp(0.2)
      if kd(4):
        rect(0,0,320,240,c1)
        if newd:
          draw_floor(80)
        ds("{Floor.py} by Sentyl_",xf,yf,(130,130,255))
        ds("Start >",90,90,c3)
        ds("Config >",90,130,c3)
        ds("[!]New background >  "+dc[newd],xnd,ynd,c2)
        one_click(4)
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
            ds("Start >",90,90,c3)
            ds("Config >",90,130,c2)
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
  return l,m,blocks,display,cls[cs[csn]]
def d_l(lives,d_l_mode,color):
  x=4
  y=4
  if d_l_mode:
    rect(x-2,y-2,lastlives*8+1,7,(0,0,0))
  else:
    rect(x-2,y-2,lastlives+3,7,(0,0,0))
  i=0
  while i < lives:
    #if not lives==:
    if d_l_mode:
      rect(x,y,4,4,color)
      x+=8
    else:
      rect(x,y,1,4,color)
      x+=1
    i+=1
class new_player:
  def __init__(self,x,y,lives,d_l_mode,blocks,isdisplay,color):
    self.x=x
    self.y=y
    self.lives=lives
    self.d_l_mode=d_l_mode
    self.blocks=blocks
    self.isdisplay=isdisplay
    self.color=color
    self.isend=True
    self.is_in_start=True
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
lives,d_l_mode,blocks,isdisplay,color=menu()
p=new_player(randint(1,12)*randint(1,12),randint(1,12)*randint(1,12),lives,d_l_mode,blocks,isdisplay,color)
def move(lives,d_l_mode,blocks,isdisplay,color,xp=p.g_x(),yp=p.g_x(),func1=gp,func2=e):
  print("Starting")
  color=p.g_color()
  #p=new_player(randint(1,12)*randint(1,12),randint(1,12)*randint(1,12),lives,d_l_mode,blocks,isdisplay,color)
  xp=p.g_x()
  yp=p.g_x()
  func1=gp
  func2=e
  p.s_x(xp)
  p.s_y(yp)
  x,s_x=p.g_x,p.s_x
  y,s_y=p.g_y,p.s_y
  blocks,s_blocks=p.g_blocks,p.s_blocks
  lives,s_lives=p.g_lives,p.s_lives
  d_l_mode=p.g_d_l_mode()
  color=p.g_color()
  display=p.g_isdisplay()
  global lastlives
  if not d_l_mode:
    s_lives(lives()*10)
  lastlives=lives()
  lt=mt()
  fall=0
  pt=0
  if p.check_is_in_start():
    p.turn_in_run()
    rect(x(),y()+8,4,4,(0,255,0))
  mi=[[func1(x(),y())]]
  d_l(lastlives,d_l_mode,color)
  pp=mt()
  b=-1
  isonwtr=0
  isnotonwtr=0
  isnotonf=False
  while lives() > 0:
    b+=1
    if kd(51):
      plt=mt()
      pte=0
      while pte<=7:
        rect(x(),y()+pte,4,1,(pte*11,pte*22,pte*30))
        pte+=1
      sp(0.2)
      while True:
        if kd(51):
          sp(0.2)
          pt+=mt()-plt
          break
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

    isonb=True
    resf=[]
    iter=0
    while iter < 4:
      floor=gp(x()+iter,y()+8)
      resf.append(floor)
      iter+=1
    d=finds(resf,(255,255,255))
    wfs=finds(resf,((24,40,189)))
    
    if kd(46) or kd(17):
      if d<3:
        s_blocks(blocks()+1)
        rect(x(),y()+8,4,4,(255,255,255))
        sp(0.05)    
    if display:
      rect(200,20,24,15,(255,255,255))
      ds(str(blocks()),200,20,(160,160,255))
    no=mt()-pp
    pp=mt()
    if not d>=3:
      if wfs>-1:
        isonwtr+=1
        fall=0
        c()
      else:
        isnotonwtr+=1
        fall/=4
        if fall>=4:
          fall/=4
          if d_l_mode:
            s_lives(lives()-int(fall))
          else:
             s_lives(lives()-int(fall*10))
          d_l(lives(),d_l_mode,color) 
      isonb=False
    if isonb:
      mi.append([func1(x(),y()+8)])
      func2(x(),y(),mi[0],1)
      mi.pop(0)
      s_y(y()+1)
      d_p(x(),y())
      fall+=1
      continue
    mp=0
    if kd(0):      
      if kd(12) or kd(52):
        mp=-4
      else:
        mp=-1
      mi.append([func1(x()+mp,y())])
      func2(x(),y(),mi[0],2)
      mi.pop(0)
      s_x(x()+mp)
    elif kd(3):
      if kd(12) or kd(52):
        
        mp=4
      else:
        mp=1
      mi.append([func1(x()+4+mp,y())])
      func2(x(),y(),mi[0],2)
      mi.pop(0)
      s_x(x()+mp)
    elif kd(1):
      mi.append([func1(x(),y()-4),func1(x(),y()-4)])
      func2(x(),y()+4,mi[0],1)
      mi.pop(0)
      s_y(y()-4)
    elif kd(2):      
      if kd(12) or kd(52):
        mp=4
      else:
        mp=1
      mi.append([func1(x(),y()+8+(mp-1)),func1(x(),y()+8+(mp-1))])
      func2(x(),y(),mi[0],1)
      mi.pop(0)
      s_y(y()+mp)
    fall=0
    d_p(x(),y())
    
    c()
  p.turn_over()
  s_lives(0)
  d_l(0,d_l_mode,color)
  ds("Game Over",100,80,(255,0,0))
  tig=str((mt()-lt)-pt)
  pfp=tig.find(".")
  ds("Time in game : "+tig[:pfp]+tig[pfp:pfp+4]+"s",55,120,(160,160,245))
  #ds(str(tig),80,180)
def init(lives=p.g_lives(),d_l_mode=p.g_d_l_mode(),blocks=p.g_blocks(),display=p.g_isdisplay(),color=p.g_color(),x=p.g_x(),y=p.g_y(),n=True):
  sp(0.01)
  if n:draw_floor(80)
  while p.check():
    try:
      move(lives,d_l_mode,blocks,isdisplay,color)
    except KeyboardInterrupt or NameError as e:
      init(p.g_lives(),p.g_d_l_mode(),p.g_blocks(),p.g_isdisplay(),p.g_color(),p.g_x(),p.g_y(),False)

init(p.g_lives(),p.g_d_l_mode(),p.g_blocks(),p.g_isdisplay(),p.g_color())