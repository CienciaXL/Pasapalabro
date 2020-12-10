import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.backend_bases import MouseButton
from letter import letter


class counter:

  def __init__(self, radius=1, color='b', bkgcolor='k', numberColor='w', name='Marcador', maxPoints=25):
    self.bkgcolor=bkgcolor
    self.fig, self.ax = plt.subplots(facecolor=self.bkgcolor)
    self.fig.set_size_inches(4,4) 
    self.fig.canvas.set_window_title(name) 
    self.margin = 1.2
    plt.xlim(-radius*self.margin, radius*self.margin)
    plt.ylim(-radius*self.margin, radius*self.margin)
    self.radius = radius
    self.letter = letter(0,0,0, size=radius/2, color=color, textsize=30)
    self.letter.Draw(self.ax)
    self.plots=[]
    self.initAx()
    self.run = False
    self.points = 0
    self.maxPoints = maxPoints

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
    if self.run:
      dt = self.lastdt + (time.time() - self.t0)
      self.letter.SetLabel('%1.0f'%(self.itime-dt))
    self.letter.Update(self.ax)
    return []

  def runtime(self, event):
    if event.button == MouseButton.RIGHT:
      self.points -= 1
    else:
      self.points += 1
    if self.points > self.maxPoints: self.points = 0
    self.letter.SetLabel(str(self.points))
    self.letter.Update(self.ax)
    self.fig.canvas.draw()

  def draw(self):
    #ani = animation.FuncAnimation(self.fig, self.update, init_func=self.init, frames=(10), interval=80, blit=True)
    self.update(0)
    self.fig.canvas.mpl_connect('button_press_event', self.runtime)
    self.fig.show()
    #plt.show()
    #return ani

if __name__ == '__main__':
  p = counter()
  p.draw()

