import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import Button


class letter:
  '''
  Class to create a circle with a letter 
  You can set the central coordinates, the letter, 
  the radius of the circle and the color (b by default)
  '''
  def __init__(self, x, y, label, size=0.1, color='b', radius=1):
    self.x = x
    self.y = y
    self.label = label
    self.size = size
    self.color = color
    self.basecolor = color
    self.selectColor = 'y'
    self.greenColor = 'g'
    self.redColor = 'r'
    #self.tempax = plt.axes([-1.2*radius, -1.2*radius, 2*radius, 2*radius])
    #self.CreateButton()

  def SetSize(self, size):
    self.size = size

  def SetColor(self, color):
    self.color = color

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

  def ChangeColor(self):
    nextcolor = self.basecolor
    if   self.color == self.basecolor: nextcolor = self.greenColor
    elif self.color == self.greenColor: nextcolor = self.redColor
    print('[%s] Moving color from %s to %s'%(self.label, self.color, nextcolor))
    self.SetColor(nextcolor)

  def Draw(self,ax):
    # Create the circle and plot it...
    circle = Circle(xy=(self.x,self.y),radius=self.size,color=self.color)
    ax.add_patch(circle)
    ax.text(self.x,self.y,self.label,horizontalalignment='center',verticalalignment='center',fontsize=15,color='white')

