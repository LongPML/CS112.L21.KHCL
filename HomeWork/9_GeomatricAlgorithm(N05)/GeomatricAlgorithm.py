#nhập lần lượt từng điểm
x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))

val = (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)
#so sánh
if val > 0: 
  print('Clockwise')
elif val < 0:
  print('Couterclockwise')
else:
  print('Colinear')