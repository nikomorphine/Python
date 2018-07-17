print('Введите количество пар данных, затем, нажав Enter, начните вводить данные попарно(т.е. сначала первое число из пары, затем второе). После оконания ввода Вы получите коэффициенты a и b, необходимые для использования метода наименших квадратов, sigma a и sigma b.')

quantity = int(input())
data = [[0]*2 for i in range(quantity)]

for i in range(quantity):
    for j in range(2):
        data[i][j] = float(input())

xy = []
for i in range(quantity):
    xy.append(data[i][0]*data[i][1])

XY = 0
for i in range(quantity):
    XY += xy[i]
XY /= quantity

X = 0
for i in range(quantity):
    X += data[i][0]
X /= quantity

Y = 0
for i in range(quantity):
    Y += data[i][1]
Y /= quantity

XX = 0
for i in range(quantity):
    XX += data[i][0]**2
XX /= quantity

YY = 0
for i in range(quantity):
    YY += data[i][1]**2
YY /= quantity

XandX = X**2
YandY = Y**2

b = (XY - X * Y)/(XX - XandX)
a = Y - b*X
print('коэффициент b = ', b)
print('коэффициент a = ', a)

sigmaB = (1/quantity**(1/2))*((YY - YandY)/(XX -XandX) - b**2)**(1/2)
sigmaA = sigmaB*(XX - XandX)**(1/2)

print('погрешность b = ', sigmaB)
print('погрешность a = ', sigmaA)
