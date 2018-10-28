import numpy as np

def mag2flux(magnitude, ABwave):
  """Convert ABmagnitude to flux in erg/s/cm^2/A 
  Oke, and Gunn, 1983, ApJ, 266, 173"""
  return 10 ** (-0.4 * (magnitude + 2.406 + 5*np.log10(ABwave)))

def flux2mag(flux, ABwave):
  """Convert flux in erg/s/cm^2/A to ABmagnitude
  Oke, and Gunn, 1983, ApJ, 266, 173"""
  return -2.5 * np.log10(flux) - 5. * np.log10(ABwave) - 2.406