import numpy as np

def bb_lambda(wavelength, temperature, scale=1.):
  """f_lambda (unit: ?) from blackbody SED"""
  # wavelength in A
  # temperature in K
  kb = 1.380648e-16 # erg/K
  c = 299792458e2 # cm/s
  hc = 1.986445e-16 # erg cm
  A_to_cm = 1e-8
  return scale / wavelength**5 * 1. / (np.exp(hc / (wavelength * A_to_cm * temperature * kb)) - 1.)

def bb_lambda_mag(wavelength, temperature, shift=0.):
  f = bb_lambda(wavelength, temperature)
  return -2.5 * np.log10(f) - 5. * np.log10(wavelength) + shift

