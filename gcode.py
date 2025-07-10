from tqdm import tqdm
import time

class GCode:
    def __init__(self, client):
        # G28 homing
        self.stack = ['G91', 'G1 Z5.0 F600', 'G90'] # for safety
        self.zdist = '2.0'
        self.zspeed = 600
        self.speed = 3000
        self.client = client

    def execute(self):
        print(f'Executing {len(self.stack)} lines of gcode')
        for code in tqdm(self.stack):
            self.client.send_gcode(code)
            time.sleep(.1)

    def append(self, value):
        self.stack.append(value) # too lazy to write self.stack haha

    def penup(self):
        self.append(f'G1 Z{self.zdist} F{self.zspeed}')

    def pendown(self):
        self.append(f'G1 Z0.1 F{self.zspeed}')

    def moveto(self, x, y):
        self.append(f'G1 X{x} Y{y} F{self.speed}')

    def point(self, x, y, size=0.5):
        self.moveto(round(x-(size/2), 2), round(y+(size/2), 2))
        self.pendown()
        self.moveto(round(x+(size/2), 2), round(y+(size/2), 2))
        self.moveto(round(x+(size/2), 2), round(y-(size/2), 2))
        self.moveto(round(x-(size/2), 2), round(y-(size/2), 2))
        self.moveto(round(x-(size/2), 2), round(y+(size/2), 2))
        self.penup()

    def line(self, c1, c2):
        self.moveto(c1[0], c1[1])
        self.pendown()
        self.moveto(c2[0], c2[1])
        self.penup()