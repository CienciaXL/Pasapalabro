import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons
from letter import letter


def GetCoordinates(r=1, n=27):
    '''
    Get the central coordinates considering angles
    '''
    PartAng = np.linspace(90,-270.,n+1)
    x,y = [],[]
    for i in range(len(PartAng)):
        x.append(r*np.cos(PartAng[i]*np.pi/180.))
        y.append(r*np.sin(PartAng[i]*np.pi/180.))
    return x[:-1],y[:-1]

labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',r'$\rm \~{N}$','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def GetLetters(labels, r=1, color='indigo'):
  x,y = GetCoordinates(r, n=len(labels))
  return [letter(x[ii], y[ii], labels[ii],color=color) for ii in range(len(x))]

def IsPointInEllipse(p, c, r):
  d = 0
  for i in range(len(p)): d += (p[i]-c[i])*(p[i]-c[i])/(r[i]*r[i])
  return d < 1

class rosco:

  def __init__(self, letters=None, radius=1, bkgcolor='k', basecolor='indigo'):
    self.bkgcolor=bkgcolor
    self.fig, self.ax = plt.subplots(facecolor=self.bkgcolor)
    self.margin = 1.2
    plt.xlim(-radius*self.margin, radius*self.margin)
    plt.ylim(-radius*self.margin, radius*self.margin)
    self.radius = radius
    self.plots=[]
    self.letters = letters
    self.basecolor = basecolor
    self.greencolor = 'g'
    self.redcolor = 'r'
    self.selectcolor = 'y'
    if letters is None:
      labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',r'$\rm \~{N}$','O','P','Q','R','S','T','U','V','W','X','Y','Z']
      self.letters = GetLetters(labels, self.radius, self.basecolor)
    self.initAx()
    # Save letter positions in fig coordinates
    self.lpos = []
    mytrans = self.ax.transAxes + self.ax.figure.transFigure.inverted()
    for l in self.letters:
      r = self.radius; m = self.margin
      rect = [(l.x+m*r)/(2*m*r), (l.y+m*r)/(2*m*r)]
      self.lpos.append(mytrans.transform(rect[0:2]))

  def initAx(self):
    self.ax.set_facecolor(self.bkgcolor)
    self.ax.xaxis.label.set_color(self.bkgcolor)
    self.ax.yaxis.label.set_color(self.bkgcolor)
    self.ax.tick_params(axis='x', colors=self.bkgcolor)
    self.ax.tick_params(axis='y', colors=self.bkgcolor)
    for l in ['bottom', 'top', 'left', 'right']: self.ax.spines[l].set_color(self.bkgcolor)
    #for l in self.letters: l.CreateButton(self.ax)

  def init(self):
    return []

  def update(self, i):
    vals = []
    for l in self.letters: 
      l.Draw(self.ax)
    return []

  def changeColor(self, event):
    mX, mY = self.fig.get_size_inches()*self.fig.dpi
    for i in range(len(self.letters)):
      x, y = self.lpos[i]
      r = self.letters[i].size/3
      C = [x*mX, y*mY]
      P = [event.x, event.y]
      R = [r*mX, r*mY]
      if IsPointInEllipse(P, C, R): 
        print("Click en letra: %s"%self.letters[i].label)
        self.letters[i].ChangeColor()
        self.letters[i].Draw(self.ax)
        self.fig.canvas.draw()

  def draw(self):
    #ani = animation.FuncAnimation(self.fig, self.update, init_func=self.init, frames=(10), interval=80, blit=True)
    self.update(0)
    self.fig.canvas.mpl_connect('button_press_event', self.changeColor)
    plt.show()
    #return ani

