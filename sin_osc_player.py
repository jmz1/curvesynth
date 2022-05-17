import math
import pyaudio
import itertools
import numpy as np
import matplotlib.pyplot as plt
from pygame import midi

# import seaborn as sns
# from IPython.display import Audio
# from scipy.io import wavfile

from synth.components.envelopes import ADSREnvelope
from synth.components.composers import WaveAdder, Chain
from synth.components.modifiers import Panner, ModulatedPanner, ModulatedVolume
from synth.components.oscillators import ModulatedOscillator, SawtoothOscillator
from synth.components.oscillators import (
    TriangleOscillator,
    SineOscillator,
    SquareOscillator,
)
from synth.player import PolySynth


# -- CONSTANTS --
BUFFER_SIZE = 64
SAMPLE_RATE = 44100
AMP_SCALE = 0.3
MAX_AMP = 0.8


# -- INITIALIZION --
testsynth = PolySynth(
    amp_scale=0.3, max_amp=0.8, sample_rate=SAMPLE_RATE, num_samples=BUFFER_SIZE
)

# def osc_function(freq, amp, sample_rate):
#     return iter(
#         Chain(
#             TriangleOscillator(freq=freq,
#                     amp=amp, sample_rate=sample_rate),
#             ModulatedPanner(
#                 SineOscillator(freq/100,
#                     phase=90, sample_rate=sample_rate)
#             ),
#             ModulatedVolume(
#                 ADSREnvelope(0.01,
#                     release_duration=0.001, sample_rate=sample_rate)
#             )
#         )
#     )


def osc_function(freq, amp, sample_rate):
    return iter(TriangleOscillator(freq=freq, amp=amp, sample_rate=sample_rate))


testsynth.play(osc_function=osc_function)

# midi.init()
# default_id = midi.get_default_input_id()
# midi_input = midi.Input(device_id=default_id)

# soundObj = pyaudio.PyAudio()

# # Learn what your OS+Hardware can do
# defaultCapability = soundObj.get_default_host_api_info()
# print(defaultCapability)

# # See if you can make it do what you want
# isSupported = soundObj.is_format_supported(
#     output_format=pyaudio.paInt16, output_channels=1, rate=44100, output_device=2
# )
# print(isSupported)

# stream = pyaudio.PyAudio().open(
#     rate=SAMPLE_RATE,
#     channels=1,
#     format=pyaudio.paInt16,
#     output=True,
#     frames_per_buffer=BUFFER_SIZE,
# )

# stream.close()

pass
