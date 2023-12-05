import ctypes


class GameCommands():
    def __init__(self):
        self.mouse = Mouse()

    def unpause_game(self):
        mouse.set_position(-10000, 10000)
        mouse.set_position(800, -10)
        time.sleep(1)
        mouse.left_click()
        time.sleep(1)
        mouse.click()


    def shoot_at_position(self, x, y):
        self.mouse.set_position(x, y)
        self.mouse.left_click()

class Mouse:
    def set_position(self, x, y):
        ctypes.windll.user32.SetCursorPos(x, y)

    def left_click(self):
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left mouse button down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left mouse button up