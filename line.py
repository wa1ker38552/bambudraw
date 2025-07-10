import cv2
import numpy as np

sm = 0.2
img = cv2.imread('stormtrooper.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (round(400*sm), round(400*sm)))
img = cv2.rotate(img, cv2.ROTATE_180)
edges = cv2.Canny(img, 93.3, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
epsilon = 0.3  # tweak this value
contours = [cv2.approxPolyDP(cnt, epsilon, True) for cnt in contours]

canvas = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

a = 0
ox = 50
oy = 50
lines = []
latex = []
for contour in contours:
    for i in range(len(contour) - 1):
        p1 = tuple(contour[i][0])
        p2 = tuple(contour[i + 1][0])
        cv2.line(canvas, p1, p2, (0, 255, 0), 1)
        dat = [p1[0]+ox, p1[1]+oy, p2[0]+ox, p2[1]+oy]
        dat = [int(i) for i in dat]
        lines.append([str(j) for j in dat])
        latex.append(f"((1-t){dat[0]}+t{dat[2]},(1-t){dat[1]}+t{dat[3]})")
        a += 1
        

'''cv2.imshow('Lines', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
with open('output.txt', 'w') as file:
    file.write('\n'.join([', '.join(i) for i in lines]))

with open('latext.txt', 'w') as file:
    file.write('\n'.join(latex))

