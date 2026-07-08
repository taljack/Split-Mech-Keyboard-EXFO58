# Split-Mech-Keyboard-EXFO58
Custom RP2040 Split Keyboard (KMK Firmware)

This repository/folder contains the KMK (CircuitPython) firmware for a hand-wired, custom split mechanical keyboard powered by dual RP2040 microcontrollers.

Hardware Specifications :
Microcontrollers: 2x RP2040 (e.g., Raspberry Pi Pico or similar)
Firmware: KMK (CircuitPython)
Matrix: 5 Rows x 6 Columns per half (60 keys total places in which 2 are ghost keys)
Diodes: 1N4148 (Column-to-Row orientation)
RGB: 29 WS2812 (NeoPixel) LEDs per half

Split Communication: Single-wire UART over TRRS cable

![image](https://github.com/taljack/Split-Mech-Keyboard-EXFO58/blob/943ddf6567a21251062ceee2df21902cd5e3655d/brave_screenshot_config.qmk.fm%20(4).png)
📍 Pinout & Wiring Guide
RP2040 Pin config :
Rows:
GP1, GP2, GP3, GP4, GP5
Columns:
GP11, GP10, GP9, GP6, GP7, GP8

RGB Data: GP29
Connected to DIN of the first LED.

Split Data: GP12
TRRS Tip/Ring. Requires a Pull-up resistor!

Handedness: GP0
Left side = unconnected. Right side = Grounded.

🛠️ The Data Line Pull-Up Resistor:

To prevent the single-wire split communication from dropping packets or freezing, a 4.7kΩ pull-up resistor (SMD code 472) is installed between the data line and power.(also works fine without a pullup resistor but may leed to freezing of keyboard sometimes)

Connect: One end to GP12, the other end to 3V3 (3.3V).

Location: Only required on one half (usually the Left/Master), as the TRRS cable physically bridges the pins.

Warning: Do NOT connect this resistor to 5V (VBUS), as RP2040 data logic operates strictly at 3.3V.


💻 Firmware Features

Dynamic Handedness Detection

The firmware uses a single main.py file for both halves. It determines which side it is on by reading GP0. If GP0 is pulled to Ground, the board knows it is the Right half.

Hardware PIO Split Sync

The split module uses use_pio=True and split_side=SplitSide.LEFT. This utilizes the RP2040's hardware PIO to allow lightning-fast communication across the halves, ensuring that keystrokes and RGB animation changes sync perfectly without lagging the matrix.

Low-Bandwidth RGB:
Because split keyboards power two microcontrollers and 58 LEDs off a single USB port, the RGB module is highly optimized:

Brightness Cap: val_limit=50 prevents the keyboard from drawing too much current and crashing the USB port.

Default Boot: Boots into a pure white static color (sat_default=0).

🗺️ Keymap & Layers

The keyboard features a standard QWERTY layout with an ergonomic LCTL position and 3 layers.
![image](https://github.com/taljack/Split-Mech-Keyboard-EXFO58/blob/943ddf6567a21251062ceee2df21902cd5e3655d/layer0.png)
Layer 0 (Base): Standard typing layer.
![image](https://github.com/taljack/Split-Mech-Keyboard-EXFO58/blob/943ddf6567a21251062ceee2df21902cd5e3655d/layer1.png)
Layer 1 (Momentary - MO): Accessed by holding the left thumb key. Contains Function keys (F1-F12), Symbols, and RGB adjustment controls on the right half.
![image](https://github.com/taljack/Split-Mech-Keyboard-EXFO58/blob/943ddf6567a21251062ceee2df21902cd5e3655d/layer2.png)
Layer 2 (Toggle - TG): Toggled on/off via the right thumb key. Contains Navigation, Numpad symbols, and specific RGB Animation mode selections.

🌈 RGB Control Deck (Right Half)

On Layer 1 (Settings):

+ : Toggle Power

) : Brightness Down

( : Brightness Up

* : Speed Down

& : Speed Up

On Layer 2 (Animations):

+ : Static Solid (Pure White default)

) : Breathing Solid

( : Breathing Rainbow

* : Rainbow Cycle

& : Knight Rider (Bouncing Ladder)

^ : Swirl (Flowing Gradient)

🩺 Troubleshooting

Right Side LEDs are frozen / not changing with the left side:

Unplug the USB cable from the PC.

Unplug the TRRS cable connecting the halves.

Plug the TRRS cable back in firmly.

Plug the USB cable into the Left half.
(This ensures the Hardware PIO clock synchronizes correctly on boot).

Keyboard types wrong characters (Left side types QWERTY on the Right side):
The TRRS cable isn't sending data. Check the GP12 wiring, ensure the TRRS jack is fully seated, and verify the 4.7kΩ pull-up resistor is properly soldered to 3V3.
