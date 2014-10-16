1.)
111-binary
7-decimal

2.)
(B**N)-1

3.)
def totalBill(checkAmount):
  tip=checkAmount*(.15)
  print tip

4.)  
def newPic():
  color=makeColor(18,52,86)
  makeEmptyPicture(200,200,color)
  show(pic)
  
5.)
def fibseq
  d1=1
  d2=0
  d3=0

  print d1

  for i in range(0,n-1):
    d3=d2
    d2=d1
    d1=d3+d2
  return=d1
  
6.)
def fibseq
  d1=1
  d2=0
  d3=0

  print d1

  for i in range(0,n-1):
    d3=d2
    d2=d1
    d1=d3+d2
    return d1
    fibList=[]
    fibList.append(d1)
    fibList=a
  print a
  
  
7.)
pic=makeEmptyPicture(800,800,white)
blackPic=makeEmptyPicture(100,100,black)
for row in range(0,8,2):
  for col in range(1,8,2):
    copyInto(blackPic,pic,col*100,row*100)
for row in range(1,8,2)
  for col in range (0,8,2):
    copyInto(blackPic,pic,col*100,row*100)
show(pic)

8.)
This function makes an 800X800 white canvas 
and then copies black squares into it every
100x100 pixels.

9.)The second function which is being defined
needs to be moved to the leftmost column instead
of being indented.

10.)
d= sqrt((100-50)**2 + (50-10)**2 + (150-50)**2)
d=118.74

11.)
def removeRed(x):
  getPixels(x)=px
  getGreen(px)=g
  getBlue(px)=b
  makeColor(0,g,b)=color
  setColor(px,color)
  
12.)
Red=39
Blue=49
Green=28

13.)
def func13(pic):
  getPixels(pic)=px
  for px in (pic)
    getRed(px)=r
    getGreen(px)=g
    getBlue(px)=b

    (sqrt(r-0)**2 + (g-0)**2 + (b-0)**2))=v

    if v>222
      setColor(px,white)
    if v==222
      return none
    if v<222
      setColor(px,black)

14.)
This function draws a circle.  
The arguments which are passed 
in determine which picture 
the circle will be superimposed upon
and what its diameter will be.
  
15.)
makeEmptyPicture(200,200)=pic
def drawCircle(pic,diameter):
  for i in range(628):
    x=diameter*cos(2*pi*i/628)+150
    y=diameter*sin(2*pi*i/628)+150
    p=getPixel(pic,int(x),int(y))
    setColor(p,black)

def draw4Circles():        
  drawCircle(pic,25)
  drawCircle(pic,50)
  drawCircle(pic,75)
  drawCircle(pic,100)
  show(pic)
  
16.)  
This code fills a circular shape with red.  
The first argument determines which picture 
the red circle is placed in and the second 
specifies its diameter.

17.)
def colorCenter(pic,25):
  for p in getPixels(pic):
    if sqrt(pow(getX(p)-150,2)+pow(getY(p)-150,2))<diameter:
      setColor(p,red)

18.)
pic=makeEmptyPicture(300,300,white)    <--or use “pic” from previous problem

def drawDiagLines(pic):
  addLine(pic,0,0,300,300)
  addLine(pic,300,0,0,300)
  show(pic)

19.)
pic=makeEmptyPicture(300,300,white)   <--or use “pic” from previous problem

def drawVertHorzLines(pic):
  addLine(pic,150,0,150,300)
  addLine(pic,0,150,300,150)
  show(pic)


20.)
1048576 bytes in one megabyte
1024 kilobytes = 1 megabyte
  
  

  


