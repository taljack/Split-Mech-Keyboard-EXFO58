import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers
from kmk.extensions.RGB import RGB, AnimationModes 

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
is_right_half = True

# ==========================================
# 🌈 RGB MATRIX CONFIGURATION (For 2D Ripple Effects)
# ==========================================
# We upgraded from basic 'RGB' to 'Rgb_matrix' to unlock reactive 2D effects!
rgb = RGB(
    pixel_pin=board.GP29,
    num_pixels=29,             # Exactly 29 physical LEDs per half
    val_limit=100,              # Safe brightness limit for USB power (max 255)
    val_default=100,            
    hue_default=200,           # 130 is a nice Cyan/Teal color
    sat_default=255,
    animation_mode=AnimationModes.KNIGHT,  # Smooth, simple fade in and out!
    animation_speed=3
    
)
keyboard.extensions.append(rgb)
# ==========================================
# 🧠 DYNAMIC HANDEDNESS DETECTION
# ==========================================


# ==========================================
# 🔗 WORKING SPLIT CONFIGURATION
# ==========================================
# This is the exact configuration you requested that successfully
# got the UART communication working across the two halves!
split = Split(
    split_side=SplitSide.RIGHT if is_right_half else SplitSide.LEFT,
    split_type=SplitType.UART,
    split_flip=False,
    data_pin=board.GP12,
    # REMOVED data_pin2=board.GP12 to fix "GP12 in use" crash
    use_pio=True,            
    uart_flip=True           
)
keyboard.modules.append(split)

# ==========================================
# ⌨️ MATRIX SETUP
# ==========================================
keyboard.row_pins = (board.GP5, board.GP4, board.GP3, board.GP2, board.GP1)
keyboard.col_pins = (board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ==========================================
# 🗺️ COORDINATE MAPPING
# ==========================================
keyboard.coord_mapping = [
     0,  1,  2,  3,  4,  5,           35, 34, 33, 32, 31, 30,
     6,  7,  8,  9, 10, 11,           41, 40, 39, 38, 37, 36,
    12, 13, 14, 15, 16, 17,           47, 46, 45, 44, 43, 42,
    18, 19, 20, 21, 22, 23, 29,       59, 53, 52, 51, 50, 49, 48,
            25, 26, 27, 28,           58, 57, 56, 55
]

_ = KC.TRNS
X = KC.NO

# ==========================================
# ⌨️ KEYMAP DEFINITIONS
# ==========================================
LAYER_0 = [
    KC.ESC,  KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,           KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.EQL, 
    KC.TAB,  KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,            KC.Y,  KC.U,  KC.I,  KC.O,  KC.P,  KC.MINS,
    KC.LCTL, KC.A,  KC.S,  KC.D,  KC.F,  KC.G,            KC.H,  KC.J,  KC.K,  KC.L,  KC.SCLN, KC.QUOT,
    KC.LSFT, KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,  KC.LBRC,  KC.RBRC, KC.N,  KC.M,  KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
                           KC.LALT, KC.LGUI, KC.MO(1), KC.ENT,  KC.SPC, KC.MO(2), KC.BSPC, KC.SCLN
]

LAYER_1 = [
    KC.RGB_TOG, KC.RGB_ANI, KC.RGB_AND, KC.RGB_VAI, KC.RGB_VAD, X,                                     _, _, _, _, _, _,
    KC.RGB_M_K, KC.RGB_M_R, KC.RGB_M_BR, KC.RGB_M_B, KC.RGB_M_P, KC.RGB_M_S,             KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12,
    _, KC.EXLM, KC.AT, KC.HASH, KC.DLR, KC.PERC,          _, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,
    _, _, _, _, _, _, _,                                  _, X, KC.MINS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE,
                      _, _, _, _,                         _, _, X, _
]

LAYER_2 = [
    _, _, _, _, _, _,                                     _, _, _, _, _, _,
    KC.TILD, KC.EXLM, KC.AT, KC.HASH, KC.DLR, KC.PERC,    KC.CIRC, KC.AMPR, KC.UP, KC.LPRN, KC.RPRN, _,
    KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6,             X, KC.LEFT, KC.DOWN, KC.RIGHT, KC.ASTR, X,
    KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, _,       _, KC.PLUS, KC.MINS, KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,
                      _, _, X, _,                         _, _, _, _
]

keyboard.keymap = [LAYER_0, LAYER_1, LAYER_2]

if __name__ == '__main__':
    keyboard.debug_enabled = True 
    keyboard.go()