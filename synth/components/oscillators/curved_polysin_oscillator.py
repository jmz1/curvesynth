# import math
from typing import Tuple
import numpy as np

from .base_oscillator import Oscillator
from .oscillators import SineOscillator
from .modulated_oscillator import ModulatedOscillator
from ..composers import WaveAdder


# works on scalars, lists, and numpy arrays
def curve_freqs(fs_in, octave=2.0, f_centre=None):
    fs_in = np.array(fs_in)
    octave = float(octave)
    if f_centre:
        return np.power(2.0, np.log2(fs_in / f_centre) * np.log2(octave)) * f_centre
    else:
        return np.power(2.0, np.log2(fs_in) * np.log2(octave))


class CurvatureController:
    def __init__(self, curvature: float = 0.0, f_centre: float = 1.0,) -> None:
        self._curvature = curvature
        self._f_centre = f_centre

    def update_curvature(self, curvature: float, f_centre: float) -> None:
        self._curvature = curvature
        self._f_centre = f_centre

    def curve_params(self) -> Tuple[float, float]:
        return (self._curvature, self._f_centre)

    # update curvature parameters
    # update


# class CurvedSineOscillator:

# do need to maintain compatibility with ASDR envelope

# curve_freqs([100, 200], octave=3, f_centre=100)

# np.arange(10)

# CurvedPolySineOscillator takes a curvature function as its frequency modulation element,
# and also passes that curvature parameter to its child oscs

# mod_val = (octave, f_centre) ?


class PolySineOscillator(Oscillator):
    def __init__(
        self, freq=440, phase=0, amp=1, sample_rate=44100, wave_range=(-1, 1)
    ) -> None:
        super().__init__(freq, phase, amp, sample_rate, wave_range)
        # will be argument in future, should be sanity-checked
        partials = {
            1: 1.0,
            2: 1.0,
            3: 1.0,
            4: 1.0,
        }
        norm_factor = sum(partials.values()) / 0.9
        self._partials = {
            index: partial_amp / norm_factor
            for (index, partial_amp) in partials.items()
        }
        self._sine_oscs = {
            SineOscillator(
                freq=freq * index,
                phase=phase,
                amp=partial_amp * amp,
                sample_rate=sample_rate,
            )
            for (index, partial_amp) in self._partials.items()
        }
        self._adder = WaveAdder(*self._sine_oscs)

    def _initialize_osc(self):
        pass

    def __iter__(self):
        # super().__iter__()
        iter(self._adder)
        return self

    def __next__(self):
        return next(self._adder)


class CurvedPolySineOscillator(PolySineOscillator):
    def __init__(
        self,
        curve_controller,
        freq=440,
        phase=0,
        amp=1,
        sample_rate=44100,
        wave_range=(-1, 1),
    ) -> None:
        super().__init__(freq, phase, amp, sample_rate, wave_range)
        self._curve_controller = curve_controller
        self._previous_curve = None

    def _check_curve_update(self) -> bool:
        latest_curve = self._curve_controller.curve_params()
        if latest_curve != self._previous_curve:
            self._previous_curve = latest_curve
            return True
        else:
            return False

    def __next__(self):
        curve_update = self._check_curve_update()
        if curve_update:
            #
            pass
        return next(self._adder)
