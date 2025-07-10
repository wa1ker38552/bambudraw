from bambu_connect import BambuClient
from gcode import GCode
import os

# G28

# Replace these with your actual details
hostname = '192.168.68.161'
access_code = '30683704'
serial = '0309CA460600268'

def execute_code(path):
    with open(path, 'r') as file:
        for line in file.read().split('\n'):
            client.send_gcode(line.strip())

client = BambuClient(hostname, access_code, serial)
# execute_code('gcode.txt')
draw = GCode(client)

'''draw.point(80, 120)
draw.point(100, 120)
draw.line((80, 115), (80, 110))
draw.line((80, 110), (100, 110))
draw.line((100, 110), (100, 115))'''

data = open('output.txt', 'r').read().split('\n')
for ln in data:
    points = [int(i.strip()) for i in ln.split(',')]
    draw.line((points[0], points[1]), (points[2], points[3]))

# draw.pendown()
draw.execute()