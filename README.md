Bambudraw allows you to draw images using your Bambulabs 3D printer!

**Connection Guide**
1. Enable LAN mode on your 3D-printer (you may need to restart it after)
2. Find your hostname by looking at the IP in the LAN mode toggle page (settings > WLAN > IP)
3. Find your access code (settings > WLAN > Access Code)
4. Follow this guide to find your serial number (https://wiki.bambulab.com/en/general/find-sn)
5. Set the hostname, accesscode, and serial number in `draw.py` (ln 8-10)

**Drawing your first image**<br>
You can draw your first image by going to `line.py` and putting the image path into ln 5. This will output into `latext.txt` and `gcode.txt`. `latex.txt` is for double checking, it puts it into a format you can graph on Desmos to see if it fits within your printers constraints or to see what it will look like. 
After that, run draw.py! To double check the pendown position of the printer, just run `draw.pendown()` to get the min distance. This distance can also be configured manually in `gcode.py`

**Drawing programatically**<br>
Creating the draw client
```py
from gcode import GCode
from bambu_connect import BambuClient

client = BambuClient(hostname, accesscode, serial)
draw = GCode(client)
```

- `draw.penup()`: Lifts the pen up
- `draw.pendown()`: Puts the pen down
- `draw.point(x, y, size)`: Draws a point at x, y coordinates with certain size (default is 0.5)
- `draw.line(c1, c2)`: c1 and c2 are points, just pass in 2 points and it will draw a line between them. Ex: `draw.line((5, 5), (10, 10))`
