import board
import usb_hid
from kmk.bootcfg import bootcfg

# 1. RAW CIRCUITPYTHON OVERRIDE:
# Completely destroy the Mouse, Consumer (Media), and Gamepad endpoints at the system level.
# The OS will physically ONLY see a standard basic Keyboard.
usb_hid.enable((usb_hid.Device.KEYBOARD,))

# 2. KMK CONFIG:
bootcfg(
    nkro_dict_config=False,
    mouse_dict_config=False,
    consumer_dict_config=False,
    # Assign a fresh Product ID so Windows forgets any old, broken drivers 
    # it previously associated with this board and installs it fresh.
    usb_product_id=0x4321 
)
import storage
storage.disable_usb_drive()