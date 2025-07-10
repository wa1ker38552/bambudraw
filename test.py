import cv2
import numpy as np
import math

img = cv2.imread('minion.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (round(72 * 1.1), round(125 * 1.1)))
img = cv2.rotate(img, cv2.ROTATE_180)
edges = cv2.Canny(img, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
epsilon = 0.01
contours = [cv2.approxPolyDP(cnt, epsilon, True) for cnt in contours]

m = 30
latex = []

def angle_between(p, center):
    return math.atan2(p[1] - center[1], p[0] - center[0])

def format_num(n):
    return f"{n:.6f}".rstrip('0').rstrip('.') if '.' in f"{n:.6f}" else str(n)

for contour in contours:
    contour = contour.reshape(-1, 2)
    for i in range(0, len(contour) - 5, 5):
        segment = contour[i:i + 5]
        if len(segment) < 5:
            continue
        try:
            ellipse = cv2.fitEllipse(segment)
            (cx, cy), (ma, ma2), angle = ellipse
            if not np.isfinite([cx, cy, ma, ma2]).all():
                continue
        except:
            continue

        cx += m
        cy += m
        start = segment[0] + m
        end = segment[-1] + m
        start = start.astype(float)
        end = end.astype(float)

        r = (ma + ma2) / 4
        if r < 1:  # avoid tiny radius/noisy arcs
            continue

        theta1 = angle_between(start, (cx, cy))
        theta2 = angle_between(end, (cx, cy))
        if theta2 < theta1:
            theta2 += 2 * math.pi

        h = format_num(cx)
        k = format_num(cy)
        r = format_num(r)
        t1 = format_num(theta1)
        t2 = format_num(theta2)

        param_eq = fr"x = {h} + {r} \cos\left(t\right)\ny = {k} + {r} \sin\left(t\right)\n{t1} \le t \le {t2}"
        latex.append(param_eq)

with open('latext.txt', 'w') as file:
    file.write('\n\n'.join(latex))
