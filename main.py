import usb_hid
from rgbkeypad import RGBKeypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from random import randint

KEYBOARD_MAP = {
    (0,0): (Keycode.LEFT_CONTROL, Keycode.KEYPAD_ONE,),   # 0
    (1,0): (Keycode.LEFT_CONTROL, Keycode.KEYPAD_TWO,),   # 1
    (2,0): (Keycode.LEFT_CONTROL, Keycode.KEYPAD_THREE,), # 2
    (3,0): (Keycode.LEFT_CONTROL, Keycode.KEYPAD_FOUR,),  # 3
    
    (0,1): (Keycode.LEFT_CONTROL, Keycode.KEYPAD_FIVE,),  # 4
    (1,1): (Keycode.LEFT_CONTROL, Keycode.KEYPAD_SIX,),   # 5
    (2,1): (Keycode.LEFT_CONTROL, Keycode.KEYPAD_SEVEN,), # 6
    (3,1): (Keycode.LEFT_CONTROL, Keycode.KEYPAD_EIGHT,), # 7
    
    (0,2): (Keycode.LEFT_CONTROL, Keycode.KEYPAD_NINE,),  # 8
    (1,2): (Keycode.LEFT_CONTROL, Keycode.KEYPAD_ZERO,),  # 9
    (2,2): (Keycode.LEFT_ALT, Keycode.KEYPAD_ONE,),       # A
    (3,2): (Keycode.LEFT_ALT, Keycode.KEYPAD_TWO,),       # B
    
    (0,3): (Keycode.LEFT_ALT, Keycode.KEYPAD_THREE,),     # C
    (1,3): (Keycode.LEFT_ALT, Keycode.KEYPAD_FOUR,),      # D
    (2,3): (Keycode.LEFT_ALT, Keycode.KEYPAD_FIVE,),      # E
    (3,3): (Keycode.LEFT_ALT, Keycode.KEYPAD_SIX,)        # F
}

INVALID_KEY_COLOR = (255, 0, 0)
DEFAULT_BRIGHTNESS = 0.1

keypad = RGBKeypad()
kbd = Keyboard(usb_hid.devices)

def resetBrightness():
    for key in keypad.keys:
        key.brightness = DEFAULT_BRIGHTNESS
    
for key in keypad.keys:
    key.color = (randint(0,255), randint(0,255), randint(0,255))
    key.brightness = DEFAULT_BRIGHTNESS

while True:
    for key in keypad.keys:
        if key.is_pressed():
            resetBrightness();
            key.brightness = 1
            
            if (key.x, key.y) in KEYBOARD_MAP.keys():
                kbd.send(*KEYBOARD_MAP[(key.x, key.y)]) 
            else:
                key.color = INVALID_KEY_COLOR
            
            while key.is_pressed():
                pass
