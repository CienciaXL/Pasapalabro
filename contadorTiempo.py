import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons
from letter import letter


class timeCounter:

  def __init__(self, totalTime=300, radius=1, color='b', bkgcolor='k', numberColor='w', name='Tiempo'):
    self.bkgcolor=bkgcolor
    self.fig, self.ax = plt.subplots(facecolor=self.bkgcolor)
    self.fig.set_size_inches(4,4) 
    self.fig.canvas.set_window_title(name) 
    self.margin = 1.2
    plt.xlim(-radius*self.margin, radius*self.margin)
    plt.ylim(-radius*self.margin, radius*self.margin)
    self.radius = radius
    self.letter = letter(0,0,totalTime, size=radius/2, color=color, textsize=30)
    self.letter.Draw(self.ax)
    self.plots=[]
    self.initAx()
    self.run = False
    self.lastdt = 0
    self.itime = totalTime

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
    self.run = not self.run
    if self.run:
      self.t0 = time.time()
    else:
      self.lastdt = self.lastdt + (time.time() - self.t0)
    #self.sec = self.sec-1
    #self.letter.SetLabel(str(self.sec-1))

  def draw(self):
    ani = animation.FuncAnimation(self.fig, self.update, init_func=self.init, frames=(10), interval=80, blit=True)
    #self.update(0)
    self.fig.canvas.mpl_connect('button_press_event', self.runtime)
    self.fig.show()
    #return ani

if __name__ == '__main__':
  p = timeCounter()
  p.draw()

