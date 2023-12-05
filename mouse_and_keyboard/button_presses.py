import ctypes


class MouseAndKeyboardManager():
    def __init__(self):
        self.mouse = MouseController()
        self.PUL = ctypes.POINTER(ctypes.c_ulong)
        #self.W = 0x11
        #self.A = 0x1E
        #self.S = 0x1F
        #self.D = 0x20
        self.L = 0x26

        SendInput = ctypes.windll.user32.SendInput

    def PressKey(hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


    def ReleaseKey(hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


    def unpause_game():
        mouse.move(-10000, 10000)
        mouse.move(800, -10)
        time.sleep(1)
        mouse.click(Button.left, 1)
        time.sleep(1)
        mouse.click(Button.left, 1)


    def click(x, y):
        ctypes.windll.user32.SetCursorPos(x, y)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left mouse button down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left mouse button up
