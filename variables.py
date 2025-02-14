"""
This module defines and preallocates memory to all variables that are used between all the files
"""
# Organization modules
from collections import deque
from numpy import zeros
from threading import Event, Lock

# -----------------------------------------------DEFINE DEQUE SIZE-----------------------------------------------------#

deque_size = 24  # set deque size (6 = 1 min of data)
sci_deque_size = 60  # set science deque size (1 = 1 second of data)

# -------------------------------------SERIAL PORT INITIALIZATION/FUNCTIONALITY----------------------------------------#

serial_port = []  # store the serial port
port_flag = [False]  # flag to request current configuration of board when connecting to new port

exit_set = [Event()]
lock = [Lock()]
power = [True]

# ----------------------------------------VOLTAGE AND CURRENT PREALLOCATION--------------------------------------------#

""" Housekeeping x-axis """
HK_x_values = deque([x for x in range(0, deque_size)])  # Initialize housekeeping x values for plotting (0 - deque size)

""" Data points """
HK_data_points = deque(zeros(deque_size))  # Initialize the data point deque

"""+5V Analog Board Graph"""
AB_voltage = deque(zeros(deque_size))  # Initialize analog board voltage
AB_current = deque(zeros(deque_size))  # Initialize analog board current

"""12V Digital Board Graph"""
DB_voltage = deque(zeros(deque_size))  # Initialize digital board voltage
DB_current = deque(zeros(deque_size))  # Initialize digital board current

"""3.3V Housekeeping Sensors Graph"""
HK_voltage = deque(zeros(deque_size))  # Initialize housekeeping sensors voltage
HK_current = deque(zeros(deque_size))  # Initialize housekeeping sensors current

"""5VST Star Trackers Graph"""
ST_voltage = deque(zeros(deque_size))  # Initialize star trackers voltage
ST_current = deque(zeros(deque_size))  # Initialize star trackers current

"""12VS Rail for Scalar Boards Graph"""
SB_voltage = deque(zeros(deque_size))  # Initialize 12VS rail scalar boards voltage
SB_current = deque(zeros(deque_size))  # Initialize 12VS rail scalar boards current

"""Scalar Boards No.1 Ch.1 Graph"""
SBN1C1_voltage = deque(zeros(deque_size))  # Initialize scalar board No.1 Ch.1 voltage
SBN1C1_current = deque(zeros(deque_size))  # Initialize scalar board No.1 Ch.1 current

"""Scalar Boards No.1 Ch.2 Graph"""
SBN1C2_voltage = deque(zeros(deque_size))  # Initialize scalar board No.1 Ch.2 voltage
SBN1C2_current = deque(zeros(deque_size))  # Initialize scalar board No.1 Ch.2 current

"""Scalar Boards No.1 Ch.3 Graph"""
SBN1C3_voltage = deque(zeros(deque_size))  # Initialize scalar board No.1 Ch.3 voltage
SBN1C3_current = deque(zeros(deque_size))  # Initialize scalar board No.1 Ch.3 current

"""Scalar Boards No.2 Ch.1 Graph"""
SBN2C1_voltage = deque(zeros(deque_size))  # Initialize scalar board No.2 Ch.1 voltage
SBN2C1_current = deque(zeros(deque_size))  # Initialize scalar board No.2 Ch.1 current

"""Scalar Boards No.2 Ch.2 Graph"""
SBN2C2_voltage = deque(zeros(deque_size))  # Initialize scalar board No.2 Ch.2 voltage
SBN2C2_current = deque(zeros(deque_size))  # Initialize scalar board No.2 Ch.2 current

"""Scalar Boards No.2 Ch.3 Graph"""
SBN2C3_voltage = deque(zeros(deque_size))  # Initialize scalar board No.2 Ch.3 voltage
SBN2C3_current = deque(zeros(deque_size))  # Initialize scalar board No.2 Ch.3 current

# ------------------------------------TEMPERATURE VISUALIZATION PREALLOCATION------------------------------------------#

"""+/-5V Regulator"""
REG5V_temp = deque(zeros(deque_size))  # Initialize 5V regulator temperature

"""3.3V Regulator"""
REG3V3_temp = deque(zeros(deque_size))  # Initialize 3.3V regulator temperature

"""Scalar Board 1"""
SB1_temp = deque(zeros(deque_size))  # Initialize scalar board 1 temperature

"""Scalar Board 2"""
SB2_temp = deque(zeros(deque_size))  # Initialize scalar board 2 temperature

# ------------------------------------------CALIBRATION PREALLOCATION--------------------------------------------------#

""" Coil 1 Offset and Amplitude """
COIL1_AMP = deque(zeros(deque_size))  # Initialize coil 1 calibration amplitude
COIL1_OFFSET = deque(zeros(deque_size))  # Initialize coil 1 calibration dc offset

""" Coil 2 Offset and Amplitude """
COIL2_AMP = deque(zeros(deque_size))  # Initialize coil 2 calibration amplitude
COIL2_OFFSET = deque(zeros(deque_size))  # Initialize coil 2 calibration dc offset

""" Coil 3 Offset and Amplitude """
COIL3_AMP = deque(zeros(deque_size))  # Initialize coil 3 calibration amplitude
COIL3_OFFSET = deque(zeros(deque_size))  # Initialize coil 3 calibration dc offset

""" VRuM Temperatures """
VRUM_TEMP_1 = deque(zeros(deque_size))  # Initialize VRuM temperature 1
VRUM_TEMP_2 = deque(zeros(deque_size))  # Initialize VRuM temperature 2
VRUM_TEMP_3 = deque(zeros(deque_size))  # Initialize VRuM temperature 3
VRUM_TEMP_4 = deque(zeros(deque_size))  # Initialize VRuM temperature 4

# -----------------------------------------FIGURE & AXES PREALLOCATION-------------------------------------------------#

""" Housekeeping Page Plots """
fig = []  # All housekeeping figures

axes = []  # Left axes for housekeeping plots
axes_background = []  # Saved background of left housekeeping axes

axes_twins = []  # Right axes for housekeeping plots
axes_twins_background = []  # Saved background of right housekeeping axes

plot_names = ["+5V Rail Analog Board", "12V Rail Digital Board", "3.3V Rail HK Sensors",
              "5VST Rail Star Trackers", "12VS Rail Scalar Boards", "Scalar Board No.1 Ch.1",
              "Scalar Board No.1 Ch.2", "Scalar Board No.1 Ch.3", "Scalar Board No.2 Ch.1",
              "Scalar Board No.2 Ch.2", "Scalar Board No.2 Ch.3", "Temperature at ±5V Regulator",
              "Temperature at 3.3V Regulator", "Temperature at Scalar Board No.1",
              "Temperature at Scalar Board No.2", "Coil 1", "Coil 2", "Coil 3"]

artist_1 = []  # Artist for left axes
artist_2 = []  # Artist for right axes

""" Science Plots """
sci_fig = []  # All science figures

sci_axes = []  # All science axes
sci_axes_background = []  # Saved background of science plots

sci_plot_names = ["Magnetometer Data Time Domain", "Magnetometer Data Frequency Domain",
                  "Magnetometer Spectrogram", "State Plot"]

artist_3 = []  # Artist for science axes

""" NST Plots """
tracker_fig = []  # All star tracker figures

tracker_axes = []  # NST 1 axes
tracker_axes_background = []  # Saved background of NST 1 plots

tracker_axes_twins = []  # NST 2 axes
tracker_axes_twins_background = []  # Saved background of NST 2 plots

artist_4 = []  # Artist for star tracker axes

# ---------------------------------------------SCALE LIMITS VARIABLES--------------------------------------------------#

""" Housekeeping Plots Limits """
voltage_limits = [[0, 5.5], [0, 12.5], [0, 3.8], [0, 5.5], [0, 12.5], [0, 12.5], [0, 12.5], [0, 12.5],
                  [0, 12.5], [0, 12.5], [0, 12.5]]
current_limits = [[0, 275], [0, 275], [0, 275], [0, 275], [0, 275], [0, 275], [0, 275], [0, 275], [0, 275],
                  [0, 275], [0, 275]]
temp_limits = [[0, 35], [0, 35], [0, 35], [0, 35]]

""" Calibration Plots Limits """
offset_limits = [[0, 1], [0, 1], [0, 1]]
amplitude_limits = [[0, 1], [0, 1], [0, 1]]

""" Science Plots Limits """
magnetometer_limits = [0, 10]
fft_limits = [0, 10]

mag_x_limits = [0, 60]
fft_x_limits = [0, 60]

""" Star Tracker Plots Limits """
NST1_limits = [[0, 1], [0, 1], [0, 1], [0, 1]]
NST2_limits = [[0, 1], [0, 1], [0, 1], [0, 1]]

# ------------------------------------------------ERROR VARIABLES------------------------------------------------------#

""" General Error Flags """
ERROR_REGISTER_0 = deque(zeros(deque_size))
ERROR_REGISTER_1 = deque(zeros(deque_size))

ERROR_LIST = []

""" Attitude Quality Error Flags """
Attitude_Quality_NST1 = []
Attitude_Quality_NST2 = []

# ---------------------------------------SCIENCE DATA/STATE PREALLOCATION----------------------------------------------#

Science_Time = deque(zeros(sci_deque_size))  # Initialize GPS time
Science_x_values = deque(zeros(sci_deque_size))

NST_1 = deque(zeros(sci_deque_size))  # Star Tracker 1 data
NST_2 = deque(zeros(sci_deque_size))  # Star Tracker 2 data

Raw_Scalar_Magnetometer_Data = deque(zeros(1025))  # Raw scalar data (size = 1025 for spectrogram)
Scalar_Magnetometer_Data = deque(zeros(sci_deque_size))  # Average of last 100 magnetometer data

Magnetometer_Status = deque(zeros(100))  # State of the magnetometer
Magnetometer_Status.popleft()
Magnetometer_Status.append(1)
Magnetometer_State = deque(zeros(100))  # Shows the state of the magnetometer at the end of a science packet
State_Change = deque(zeros(sci_deque_size))  # Did the magnetometer change state in the last scalar packet
Mod8_Counter = deque(zeros(100))  # Packet counter to ensure no packets are skipped
CRC_Flag = deque(zeros(100))  # CRC flag for scalar packets

PSD = deque(zeros(sci_deque_size))  # Power spectral density of magnetometer data
Freq = deque(zeros(sci_deque_size))  # Frequencies of magnetometer data

# ---------------------------------------------DISPLAY WINDOWS & FRAMES------------------------------------------------#
housekeeping_display = [False]  # flag to determine if the window is open
science_display = [False]  # flag to determine if the window is open

hk_display_window = []  # housekeeping display window
sci_display_window = []  # science display window

# --------------------------------------------------GUI OBJECTS--------------------------------------------------------#

""" Housekeeping Page """
error_grid = []  # Grid of buttons that display error flags
hk_csvwriter = []  # save to file writer that enables the creation of a csv file (used in save_file() func)

""" Commands Page """
current_scalar_sample_rate = []  # sample rate used for frequency domain representation of magnetometer data
current_scalar_baud_rate = []  # baud rate of the scalar magnetometer
current_frequencies = []  # current frequencies of the coils on the analog board (3 values)
current_amplitudes = []  # current amplitudes of the coils on the analog board (3 values)
amplitude_bars = []  # display of the current amplitude as a percentage on progress bar (3 progress bars)

frequencies = []  # string variables that the user inputs (3 strings)
amplitudes = []  # int variables that the user inputs (3 ints)
user_amplitudes = []  # slider objects on the commands page (3 sliders)
amplitude_labels = []  # amplitude label object on commands page
scalar_values = []  # scalar baud and sample rates

stream_science_checkbox = []  # checkbox to indicate when to stream science data

board_led = []  # all the board led indicators (5 leds)

gain = []  # string variables that the user inputs for gain (1 string)

""" Science Page """
led_image = []  # magnetometer state light indicator (used in update_state() func)
state_label = []  # magnetometer state label (used in update_state() func)
sci_CRC_image = []  # light indicator to ensure CRC passes
sci_CRC_label = []  # CRC label

write_checkbox = []  # save to file checkbox (used in save_to_file() func)
points_saved = []  # save to file label (used in save_to_file() func)
num_saved = []  # text variable of points saved (used in save_to_file() func)
sci_csvwriter = []  # save to file writer that enables the creation of a csv file (used in save_to_file() func)
write_to_sci = []  # provides allow user to take their time when choosing a directory for their csv file
