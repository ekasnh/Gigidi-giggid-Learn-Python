#!pip install numpy scipy scikit-dsp-comm ipywidgets PyAudio
import numpy as np
import ipywidgets as widgets
from IPython.display import display
import sk_dsp_comm.pyaudio_helper as pah 
import pyaudio # Imported separately for explicit access to constants

# --- 1. Global State Variable ---
# This variable is accessed and updated by the widget function (main thread)
# and read by the real-time DSP callback (audio thread).
global_volume_scale = 1.0

# --- 2. Interactive Widget Setup ---

def update_volume(gain):
    """Callback function for the ipywidget to update the global gain."""
    global global_volume_scale
    global_volume_scale = gain
    # Note: We skip printing here to avoid flooding the notebook output during streaming

# Create an interactive slider (range: 0.0 to 2.0)
volume_slider = widgets.FloatSlider(
    value=1.0,
    min=0.0,
    max=2.0,
    step=0.01,
    description='Volume Gain:',
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='.2f',
)

# Link the slider to the update function (Note: 'gain' must match the keyword in update_volume)
# We use interactive_output to ensure the slider updates the variable
widgets.interactive_output(update_volume, {'gain': volume_slider})


# --- 3. The Real-Time DSP Callback Function ---

def dsp_callback(in_data, frame_count, time_info, status):
    """
    The main DSP function called repeatedly by the audio thread.
    Applies the global volume_scale to the input audio frame (mono).
    """
    global global_volume_scale
    
    # 1. Convert the byte-formatted input data (int16) to a numpy array
    in_data_nda = np.frombuffer(in_data, dtype=np.int16)
    
    # 2. Convert to float32 for processing and normalize to [-1, 1]
    x = in_data_nda.astype(np.float32) / (2**15) 
    
    # **********************************************
    # DSP Operation: Apply the global gain set by the widget
    y = global_volume_scale * x
    # **********************************************

    # 4. Convert back to int16, scaling back up and clipping to prevent overflow
    y_int16 = np.clip(y * (2**15), -2**15, 2**15 - 1).astype(np.int16)

    # 5. Convert the processed numpy array back to bytes for output
    return y_int16.tobytes(), pyaudio.paContinue


# --- 4. Stream Initialization and Execution ---

# Configuration Parameters (Update these based on your system)
FS = 44100            # Sample Rate (Hz)
N_FRAME = 512         # Frame length (samples per callback)
NUM_CHANNELS = 1      # Use 1 for mono

# --- Device Index Check (Crucial Step!) ---
print("--- Available Audio Devices ---")
pah.available_devices()
print("-------------------------------")

# NOTE: You must replace 'IN_IDX' and 'OUT_IDX' with the indices 
# of your desired Microphone and Speaker/Headphone devices found above.
IN_IDX = 0  # Example: Built-in Microphone
OUT_IDX = 1 # Example: Built-in Speakers 

try:
    # 1. Create the streaming object
    DSP_IO = pah.DSP_io_stream(
        stream_callback=dsp_callback,
        in_idx=IN_IDX,
        out_idx=OUT_IDX,
        fs=FS,
        frame_length=N_FRAME,
        Tcapture=0,
        numChan=NUM_CHANNELS
    )

    # 2. Display the widget and the stream controls
    # VBox stacks the widget and the stream controls vertically
    print("Real-Time Volume Control:")
    display(volume_slider)
    
    # The interactive_stream method displays its own Start/Stop buttons.
    print("\nStream Controls:")
    DSP_IO.interactive_stream(Tsec=0, numChan=NUM_CHANNELS)
    
except Exception as e:
    print(f"\n[ERROR] Could not start stream. Check your IN_IDX and OUT_IDX settings.")
    print(f"Details: {e}")
