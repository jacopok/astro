import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from astropy import fits

data1 = fits.getdata('event2.fits')
data2 = fits.getdata('event2_2.fits')

bins=500
range=[500, 2e4]
alpha=0.5
plt.hist(data1['energy'], weights=np.ones_like(data1['energy']), bins=bins, alpha=alpha, range=range, label='data_e1*20')
plt.hist(data2['energy'], bins=bins, alpha=alpha, range=range, label='data_e2')
plt.hist(np.concatenate((data1['energy'], data2['energy'])), bins=bins, alpha=alpha, range=range, label='sum')
plt.legend()
