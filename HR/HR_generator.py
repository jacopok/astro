import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath}
          \usepackage{physics}
          \usepackage{siunitx}
          ''')

data = pd.read_excel('near star lst.xls')

AM = np.array(data['Abs Mag'])
CI = np.array(data['ColorIndex B-V'])
d = np.stack((CI, AM)).T

nd = np.array(list(filter(lambda i: not (type(i[0]) is str or type(i[1]) is str), d)))

plt.hist2d(nd[:, 0], nd[:, 1], bins=500)
plt.ylim((15, -10))
plt.xlim((-.4, 2))
plt.colorbar()
plt.xlabel('Color Index: $B-V$')
plt.ylabel('Absolute Magnitude')

plt.show()