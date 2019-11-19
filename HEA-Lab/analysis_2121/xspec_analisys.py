from xspec import *

Spectrum("../2121_e1/spectra/rebinned20.pi")
Model("phabs*pow")
Fit.perform()
Plot.device = "/xs"
Plot("data")