import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import Button
from matplotlib.backend_bases import MouseButton


class letter:
  '''
  Class to create a circle with a letter 
  You can set the central coordinates, the letter, 
  the radius of the circle and the color (b by default)
  '''
  def __init__(self, x, y, label, size=0.1, color='b', radius=1, textsize=18):
    self.x = x
    self.y = y
    self.label = label
    self.size = size
    self.color = color
    self.basecolor = color
    self.selectColor = 'darkviolet'
    self.greenColor = 'g'
    self.redColor = 'r'
    self.textsize=textsize
    #self.tempax = plt.axes([-1.2*radius, -1.2*radius, 2*radius, 2*radius])
    #self.CreateButton()

  def SetSize(self, size):
    self.size = size

  def SetColor(self, color):
    self.color  = color

  def SetLabel(self, label):
    self.label = label

  def CreateButton(self, ax):
    #figx, figy = ax.transAxes.transform((self.x, self.y))
    k = self.size/2
    rect = [(self.x+1.2)/2.4, (self.y+1.2)/2.4]
    mytrans = ax.transAxes + ax.figure.transFigure.inverted()
    infig_position = mytrans.transform(rect[0:2])
    figx, figy = infig_position
    tempax = plt.axes([figx-k/2, figy-k/2, k, k], facecolor='r')
    self.button = Button(tempax, '', color='w', hovercolor=self.selectColor)
    self.button.on_clicked(self.ChangeColor)

  def ChangeColor(self, button):
    nextcolor = self.basecolor
    colors = [self.basecolor, self.selectColor, self.greenColor, self.redColor]
    if   button == MouseButton.MIDDLE: 
      nextcolor = self.basecolor
    elif button == MouseButton.LEFT  :
      if   self.color == self.basecolor  : nextcolor = self.selectColor
      elif self.color == self.selectColor: nextcolor = self.greenColor
      elif self.color == self.greenColor : nextcolor = self.redColor
      elif self.color == self.redColor   : nextcolor = self.basecolor
    elif button == MouseButton.RIGHT :
      if   self.color == self.basecolor  : nextcolor = self.redColor
      elif self.color == self.redColor   : nextcolor = self.greenColor
      elif self.color == self.greenColor : nextcolor = self.selectColor
      elif self.color == self.selectColor: nextcolor = self.basecolor
    print('[%s] Moving color from %s to %s'%(self.label, self.color, nextcolor))
    self.SetColor(nextcolor)

  def Draw(self,ax):
    # Create the circle and plot it...
    self.circle = Circle(xy=(self.x,self.y),radius=self.size,color=self.color)
    ax.add_patch(self.circle)
    self.text = ax.text(self.x,self.y,self.label,horizontalalignment='center',verticalalignment='center',fontsize=self.textsize,color='white',weight='bold')

  def Update(self, ax):
    self.text.remove()
    self.Draw(ax)
