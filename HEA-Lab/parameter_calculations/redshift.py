from astropy.cosmology import FlatLambdaCDM
from astropy.coordinates import SkyCoord
import astropy.units as u
import astropy.uncertainty as aun
import astropy.constants as ac
from uncertainties import ufloat

coords = SkyCoord('09h47m40.156s -30d56m55.44s', frame='fk5')

# from page 64 of
# https://ui.adsabs.harvard.edu/abs/2003AJ....126.2268W/abstract
z = ((2544 * u.km / u.s ) / ac.c).to('')
deltaz = ((12 * u.km / u.s) / ac.c).to('')

# from 
# http://simbad.u-strasbg.fr/simbad/sim-id?Ident=MCG-5-23-16
z2 = ((2466.09 * u.km / u.s ) / ac.c).to('')
deltaz2 = ((47.97 * u.km / u.s) / ac.c).to('')

compat = ufloat(z, deltaz) - ufloat(z, deltaz2)

cosmo = FlatLambdaCDM(H0=67.8, Om0=.308)

z_pdf = aun.normal(z.value, std=deltaz.value, n_samples = 10_000)

dist = aun.Distribution(cosmo.comoving_distance(z_pdf.distribution))
