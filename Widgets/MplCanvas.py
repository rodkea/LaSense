import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

  def __init__(self, parent=None):
    fig = Figure()
    self.axes = fig.add_subplot(111)
    self.axes.set_yticks([])
    self.axes.set_xticks([])
    self.cb =  None
    super(MplCanvas, self).__init__(fig)