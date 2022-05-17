import math
import numpy as np

from .oscillators import SineOscillator

# works on scalars, lists, and numpy arrays
def curve_freqs(fs_in, octave=2.0, f_centre=None):
    fs_in = np.array(fs_in)
    octave = float(octave)
    if f_centre:
        return np.power(2.0, np.log2(fs_in / f_centre) * np.log2(octave)) * f_centre
    else:
        return np.power(2.0, np.log2(fs_in) * np.log2(octave))


# curve_freqs([100, 200], octave=3, f_centre=100)

# np.arange(10)
