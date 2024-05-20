import pygame
from math import*
#MAIN POLYGON FORMS
def GeneratePolygons(NumSides): #Генерирует правильные многоугольники, принимает (Количество сторон), возвращает полигоны готового многоугольника
    Pols = []
    Deg = 0
    for i in range(NumSides):
        Pols.append((cos(radians(Deg)), sin(radians(Deg))))
        Deg += 360 / NumSides
    return Pols
def GenerateNewPolygonSeq(NumSides, NumCopy, XRast, YRast): #Генерирует последовательность правильных многоугольников, принимает (Количество сторон, Колиство фигур, Расстояние по X между фигурами, Расстояние по Y между фигурами), возвращает полигоны многоугольников
    Pols = []
    Deg = 0
    for i in range(NumSides):
        Pols.append((cos(radians(Deg)), sin(radians(Deg))))
        Deg += 360 / NumSides
    RMn = 0
    for i in range(NumCopy):
        for x, y in Pols[:NumSides]:
            Pols.append((x + XRast * RMn, y + YRast * RMn))
        RMn += 1
    return Pols
def GeneratePolygonSeq(Polygon, NumCopy, XRast, YRast): #Создает последовательность из уже имеющихся многоугольников, принимает (Полигоны многоугольника, Количество копий, Расстояние по X между фигурами, Расстояние по Y между фигурами), возвращает полигоны многоугольников
    Pols = []
    RMn = 0
    for i in range(NumCopy):
        for x, y in Polygon:
            Pols.append((x + XRast * RMn, y + YRast * RMn))
        RMn += 1
    return Pols
#POLYGONS TRANSFORMATE FUNCTIONS
def ScalePolygon(Polygon, XSc, YSc): #Масштабирует фигуру, принимает (Полигоны многоугольника, Множитель для X, Множитель для Y), возпращает полигоны многоугольника
    Pols = []
    Centr = [0, 0]
    for x, y in Polygon:
        Centr[0] += x
        Centr[1] += y
    Centr[0] /= len(Polygon)
    Centr[1] /= len(Polygon)
    for x, y in Polygon:
        Pols.append((Centr[0] + (x - Centr[0]) * XSc, Centr[1] + (y - Centr[1]) * YSc))
    return Pols
def ScalePolygonSeq(Polygons, NumPolsInFig, XSc, YSc): #Масштабирует последовательность фигур, принимает (Полигоны многоугольника, Количество сторон у многоульника, Множитель для X, Множитель для Y), возпращает полигоны многоугольников
    Pols = []
    for i in range(0, len(Polygons), NumPolsInFig):
        Pols += ScalePolygon(Polygons[i:i + NumPolsInFig], XSc, YSc)
    return Pols
def TranslatePolygon(Polygon, XTr, YTr): #Перемещает полигоны, принимает (Массив полигонов, перемещение по X, перемещение по Y), Возвращает последовательность полигонов
    return [(x + XTr, y + YTr) for x, y in Polygon]
def RotateFigureDeg(Polygon, Deg): #Поворот фигуры по градусам, принимает (Полигоны многоугольника, Градусы на которые надо повернуть), возвращает полигоны многоугольника
    Pols = []
    Centr = [0, 0]
    for x, y in Polygon:
        Centr[0] += x
        Centr[1] += y
    Centr[0] /= len(Polygon)
    Centr[1] /= len(Polygon)
    for x, y in Polygon:
        Pols.append((Centr[0] + (x - Centr[0]) * cos(radians(Deg)) + (y - Centr[1]) * -sin(radians(Deg)), Centr[1] + (x - Centr[0]) * sin(radians(Deg)) + (y - Centr[1]) * cos(radians(Deg))))
    return Pols
def RotateFigureRad(Polygon, Rad): #Поворот фигуры по радианам, принимает (Полигоны многоугольника, Радианы на которые надо повернуть), возвращает полигоны многоугольника
    Pols = []
    Centr = [0, 0]
    for x, y in Polygon:
        Centr[0] += x
        Centr[1] += y
    Centr[0] /= len(Polygon)
    Centr[1] /= len(Polygon)
    for x, y in Polygon:
        Pols.append((Centr[0] + (x - Centr[0]) * cos(Rad) + (y - Centr[1]) * -sin(Rad), Centr[1] + (x - Centr[0]) * sin(Rad) + (y - Centr[1]) * cos(Rad)))
    return Pols
def RotateFigureDegSeq(Polygons, Deg, NumPolsInFig): #Поворот последовательности фигур по градусам, принимает (Полигоны многоугольников, Градусы на которые надо повернуть, Количество сторон фигуры), возвращает полигоны многоугольников
    Pol = []
    for i in range(0, len(Polygons), NumPolsInFig):
        Pol += RotateFigureDeg(Polygons[i:i + NumPolsInFig], Deg)
    return Pol
def RotateFigureRadSeq(Polygons, Rad, NumPolsInFig): #Поворот последовательности фигур по радианам, принимает (Полигоны многоугольников, Радианы на которые надо повернуть, Количество сторон фигуры), возвращает полигоны многоугольников
    Pol = []
    for i in range(0, len(Polygons), NumPolsInFig):
        Pol += RotateFigureRad(Polygons[i:i + NumPolsInFig], Rad)
    return Pol
def GetSymmetry(Polygons, PointSym): #Получение симметрии отностительно точки, принимает (Полигоны многоугольника(ов), точку относительно которой производится симметрия), возвращает полигоны симметричных многоугольников
    Pols = []
    for x, y in Polygons:
        Pols.append((PointSym[0] + (PointSym[0] - x), PointSym[1] + (PointSym[1] - y)))
    return Pols
def ZipPolygonsSeq(Pol1, Pol2, NumPolsInFig1, NumPolsInFig2):
    Pols = []
    for i in range(0, len(Pol1) // NumPolsInFig1):
        Pols += Pol1[i * NumPolsInFig1: (i + 1) * NumPolsInFig1] + Pol2[i * NumPolsInFig2: (i + 1) * NumPolsInFig2]
    return Pols

#FILTER FUNCTIONS
def MinSqarFilt(Polygons, NumPolsInFig, MinFilt): #Фильтрует последовательность многоугольников по минимальной площади, принимает (Полигоны последовательности, Колисчетство сторон в многоугольнике, Минимальная площадь), возвращает отфильтрованную последовательность
    Pols = []
    for i in range(0, len(Polygons), NumPolsInFig):
        S = 0
        for j in range(NumPolsInFig):
            S += Polygons[i + j][0] * Polygons[i + ((j + 1) % NumPolsInFig)][1]
        for j in range(NumPolsInFig):
            S -= Polygons[i + j][1] * Polygons[i + ((j + 1) % NumPolsInFig)][0]
        if S > MinFilt:
            Pols += Polygons[i:i + NumPolsInFig]
    return Pols
def MaxSqarFilt(Polygons, NumPolsInFig, MaxFilt): #Фильтрует последовательность многоугольников по максимальной площади, принимает (Полигоны последовательности, Колисчетство сторон в многоугольнике, максимальная площадь), возвращает отфильтрованную последовательность
    Pols = []
    for i in range(0, len(Polygons), NumPolsInFig):
        S = 0
        for j in range(NumPolsInFig):
            S += Polygons[i + j][0] * Polygons[i + ((j + 1) % NumPolsInFig)][1]
        for j in range(NumPolsInFig):
            S -= Polygons[i + j][1] * Polygons[i + ((j + 1) % NumPolsInFig)][0]
        if S < MaxFilt:
            Pols += Polygons[i:i + NumPolsInFig]
            S = MaxFilt
    return Pols
def ShortSideFilt(Polygons, NumPolsInFig, MinFilt): #Фильтрует последовательность многоугольников по короткой стороне, принимает (Полигоны последовательности, Колисчетство сторон в многоугольнике, кратчайшая сторона), возвращает отфильтрованную последовательность
    Pols = []
    for i in range(0, len(Polygons), NumPolsInFig):
        ShortSid = sqrt((Polygons[i][0] - Polygons[i + NumPolsInFig - 1][0]) ** 2 + (Polygons[i][1] - Polygons[i + NumPolsInFig - 1][1]) ** 2)
        Lx = Polygons[i][0]
        Ly = Polygons[i][1]
        for x, y in Polygons[i + 1: i + NumPolsInFig]:
            ShortSid = min(ShortSid, sqrt((x - Lx) ** 2 + (y - Ly) ** 2))
        if ShortSid > MinFilt:
            Pols += Polygons[i: i + NumPolsInFig]
    return Pols
def PointFil(Polygons, NumPolsInFig, Point): #Фильтрует многоугольники у которых хоть одна точка совпадает с заданной точкой, принимает (Последовательность многоугольников, Количество сторон в многоугольнике, Точку для фильтрации), возвращает отфильрованную последовательность
    Pols = []
    for i in range(0, len(Polygons), NumPolsInFig):
        f = 1
        for x, y in Polygons[i: i + NumPolsInFig]:
            if x == Point[0] and y == Point[1]:
                f = 0
                break
        if f:
            Pols += Polygons[i: i + NumPolsInFig]
    return Pols
def InsidePolygon(Polygons, x, y): #Ищет находится ли точка внутри выпуклого многоугольника, принимает (Полигоны многоугольника, X точки, У точки), возвращает 1 если находится и 0 если нет
    c = 0
    for i in range(len(Polygons)):
        if (((Polygons[i][1]<=y and y<Polygons[i-1][1]) or (Polygons[i-1][1]<=y and y<Polygons[i][1])) and (x > (Polygons[i-1][0] - Polygons[i][0]) * (y - Polygons[i][1]) / (Polygons[i-1][1] - Polygons[i][1]) + Polygons[i][0])): c = 1 - c    
    return c
def FiltPolygonsInsidSeq(Polygons, NumPolsInFig, Point): #Фильтрует многоугольники содержащие определенную точку, принимает (Последовательность многоугольников, Количество сторон в многоугольнике, Точка), возвращает отфильтрованную последовательность
    Pols = []
    for i in range(0, len(Polygons), NumPolsInFig):
        if (not InsidePolygon(Polygons[i: i + NumPolsInFig], Point[0], Point[1])):
            Pols += Polygons[i: i + NumPolsInFig]
    return Pols
def FiltPolygonsFigure(Polygons, NumPolsInFig, Figure): #Фильтрует последовательность полигонов содержащих хоть одну точку заданного многоугольника, принимает (Последовательность многоугольников, Количество сторон в многоугольнике, Фигуру), возвращает отфильтрованную последовательность
    Pols = []
    for i in range(0, len(Polygons), NumPolsInFig):
        f = 1
        for x, y in Figure:
            if (InsidePolygon(Polygons[i: i + NumPolsInFig], x, y)):
                f = 0
                break
        if f:
            Pols += Polygons[i: i + NumPolsInFig]
    return Pols
#OTHER FUNCTIONS
def FindMinArea(Polygons, NumPolsInFig): #Находит минимальную площадь фигуры, принимает (Последовательность многоугольников, количество сторон в многоугольнике), возвращает фигуру с минимальной площадью
    Pols = Polygons[:NumPolsInFig]
    MinArr = 0
    for j in range(NumPolsInFig):
        MinArr += Polygons[j][0] * Polygons[((j + 1) % NumPolsInFig)][1]
    for j in range(NumPolsInFig):
        MinArr -= Polygons[j][1] * Polygons[((j + 1) % NumPolsInFig)][0]
    for i in range(NumPolsInFig, len(Polygons), NumPolsInFig):
        S = 0
        for j in range(NumPolsInFig):
            S += Polygons[i + j][0] * Polygons[i + ((j + 1) % NumPolsInFig)][1]
        for j in range(NumPolsInFig):
            S -= Polygons[i + j][1] * Polygons[i + ((j + 1) % NumPolsInFig)][0]
        if S < MinArr:
            MinArr = S 
            Pols = Polygons[i: NumPolsInFig + i]
    return Pols
def SumArea(Polygons, NumPolsInFig): #Находит сумму всех площадей последовательности, принимает (Последовательность многоугольников, количество сторон в многоугольнике), возвращает сумму
    Arr = 0
    for i in range(0, len(Polygons), NumPolsInFig):
        S = 0
        for j in range(NumPolsInFig):
            S += Polygons[i + j][0] * Polygons[i + ((j + 1) % NumPolsInFig)][1]
        for j in range(NumPolsInFig):
            S -= Polygons[i + j][1] * Polygons[i + ((j + 1) % NumPolsInFig)][0]
        Arr += S
    return Arr
def SumPerimeter(Polygons, NumPolsInFig): #Находит сумму всех периметров последовательности, принимает (Последовательность многоугольников, количество сторон в многоугольнике), возвращает сумму
    Per = 0
    for i in range(0, len(Polygons), NumPolsInFig):
        Per += sqrt((Polygons[i][0] - Polygons[i + NumPolsInFig - 1][0]) ** 2 + (Polygons[i][1] - Polygons[i + NumPolsInFig - 1][1]) ** 2)
        Lx = Polygons[i][0]
        Ly = Polygons[i][1]
        for x, y in Polygons[i + 1: i + NumPolsInFig]:
            Per += sqrt((x - Lx) ** 2 + (y - Ly) ** 2)
    return Per
def FindMaxSide(Polygons, NumPolsInFig): #Находит самую длинную сторону в последовательности многоугольников, принимает (Последовательность полигонов, количество сторон в многоугольнике), возвращает длинну максимальной стороны
    MaxP = 0
    for i in range(0, len(Polygons), NumPolsInFig):
        MaxP = max(sqrt((Polygons[i][0] - Polygons[i + NumPolsInFig - 1][0]) ** 2 + (Polygons[i][1] - Polygons[i + NumPolsInFig - 1][1]) ** 2), MaxP)
        Lx = Polygons[i][0]
        Ly = Polygons[i][1]
        for x, y in Polygons[i + 1: i + NumPolsInFig]:
            MaxP = max(((x - Lx) ** 2 + (y - Ly) ** 2), MaxP)
    return MaxP
def FindNearToNull(Polygons): #Находит ближайшую точку к центру координат, принимает (Последовательность полигонов), Возвращает точку ближайшую к центру координат
    Pol = (Polygons[0][0], Polygons[0][1])
    Rast = sqrt(Polygons[0][0] * Polygons[0][0] + Polygons[0][1] * Polygons[0][1])
    for x, y in Polygons[1::]:
        if sqrt(x * x + y * y) < Rast:
            Rast = sqrt(x * x + y * y)
            Pol = (x, y)
    return Pol
#VECTOR FUNCTIONS
def VecLen(Vector): return sqrt(Vector[0] * Vector[0] + Vector[1] * Vector[1]) #Находит длинну вектора
def VecSum(Vec1, Vec2): return (Vec1[0] + Vec2[0], Vec1[1] + Vec2[1]) #Cуммирует два вектора
def VecSub(Vec1, Vec2): return (Vec1[0] - Vec2[0], Vec1[1] - Vec2[1]) #Отнимает два вектора
def VecMul(Vec1, Vec2): return (Vec1[0] * Vec2[0], Vec1[1] * Vec2[1]) #Умножает два вектора
def VecDiv(Vec1, Vec2): return (Vec1[0] / Vec2[0], Vec1[1] / Vec2[1]) #Делит два вектора
def VecNorm(Vector): return (Vector[0] / VecLen(Vector), Vector[1] / VecLen(Vector)) #Нормализует вектор
#WINDOW CLASS
class Window:
    def __init__(self, XSize, YSize):
        self.XSize = XSize
        self.YSize = YSize
        self.sc = pygame.display.set_mode((XSize, YSize))
        self.BaseVectorX = (1, 0)
        self.BaseVectorY = (0, 1)
        self.TranslateVector = (0, 0)
        self.ColorDraw = (255, 255, 255)
        self.ColorClear = (0, 0, 0)
        self.FrameRate = 60
        self.clock = pygame.time.Clock()
        pygame.init()
    def SetDefaultMatrix(self): #Устанавливает стандартную матрицу
        self.BaseVectorX = (1, 0)
        self.BaseVectorY = (0, 1)
    def SetTranslateMatrix(self, XTrans, YTrans): #Устанавливает центр координат, принимает (Перемещение по X, перемещение по Y)
        self.TranslateVector[0] = XTrans
        self.TranslateVector[1] = YTrans
    def TraslateMatrix(self, XTrans, YTrans): #Перемещает центр координат, принимает (Перемещение по X, перемещение по Y)
        self.TranslateVector[0] += XTrans
        self.TranslateVector[1] += YTrans
    def SetRotateMatrixDeg(self, Deg): #Поворачивает координатную плоскость по градусам, принимает (Градусы)
        self.BaseVectorX = (cos(radians(Deg)) * VecLen(self.BaseVectorX), sin(radians(Deg)) * VecLen(self.BaseVectorX))
        self.BaseVectorY = (-sin(radians(Deg)) * VecLen(self.BaseVectorY), cos(radians(Deg)) * VecLen(self.BaseVectorY))
    def SetRotateMatrixRad(self, Rad): #Поворачивает координатную плоскость по радианам, принимает (радианы)
        self.BaseVectorX = (cos(Rad) * VecLen(self.BaseVectorX), sin(Rad) * VecLen(self.BaseVectorX))
        self.BaseVectorY = (-sin(Rad) * VecLen(self.BaseVectorY), cos(Rad) * VecLen(self.BaseVectorY))
    def SetBaseVectors(self, NewBaseVectorX, NewBaseVectorY): #Устанавливает базовые векторы (Базовый вектор X, Базовый вектор Y)
        self.BaseVectorX = NewBaseVectorX
        self.BaseVectorY = NewBaseVectorY
    def ScaleMatrix(self, XMnoj, YMnoj): #Масштабирует матрицу, принимает (Множитель по X, Множитель по Y)
        self.BaseVectorX = (self.BaseVectorX[0] * XMnoj, self.BaseVectorX[1] * XMnoj)
        self.BaseVectorY = (self.BaseVectorY[0] * YMnoj, self.BaseVectorY[1] * YMnoj)
    def SetClearColor(self, Color): #Устанавливает цвет для очистки экрана, принимает (Цвет очистки формата (R, G, B))
        self.ColorClear = Color
    def SetDrawColor(self, Color): #Устанавливает цвет для отрисовки полигонов, принимает (Цвет отрисовки формата (R, G, B))
        self.ColorDraw = Color
    def ClearScreen(self): #Очищает экран
        self.clock.tick(self.FrameRate)
        self.sc.fill(self.ColorClear)
    def UpdateImage(self): #Обновляет буффер
        pygame.display.flip()
    def DrawUnfilledFigure(self, Polygons, SizeMnojX = 1, SizeMnojY = 1, DrawPoints = True, DrawLines = True): #Рисует незакрашенную фигуру, принимает (Полигоны многоугольника, Множитель размеров по X, множитель размеров по Y, Флаг отрисоки точек, флаг отрисовки прямых)
        X = self.TranslateVector[0] + Polygons[0][0] * self.BaseVectorX[0] * SizeMnojX + Polygons[0][1] * self.BaseVectorY[0] * SizeMnojY
        Y = self.TranslateVector[1] + Polygons[0][0] * self.BaseVectorX[1] * SizeMnojX + Polygons[0][1] * self.BaseVectorY[1] * SizeMnojY
        if DrawPoints:
            pygame.draw.circle(self.sc, self.ColorDraw, (self.XSize // 2 + X * (self.XSize // 2), self.YSize // 2 + Y * (self.YSize // 2)), 5)
        if DrawLines:
            LX = self.TranslateVector[0] + Polygons[-1][0] * self.BaseVectorX[0] * SizeMnojX + Polygons[-1][1] * self.BaseVectorY[0] * SizeMnojX
            LY = self.TranslateVector[1] + Polygons[-1][0] * self.BaseVectorX[1] * SizeMnojY + Polygons[-1][1] * self.BaseVectorY[1] * SizeMnojY
            pygame.draw.line(self.sc, self.ColorDraw, (self.XSize // 2 + X * (self.XSize // 2), self.YSize // 2 + Y * (self.YSize // 2)), (self.XSize // 2 + LX * (self.XSize // 2), self.YSize // 2 + LY * (self.YSize // 2)), 2)
            LX = X;
            LY = Y;
        for x, y in Polygons[1::]:
            X = self.TranslateVector[0] + x * self.BaseVectorX[0] * SizeMnojX + y * self.BaseVectorY[0] * SizeMnojY
            Y = self.TranslateVector[1] + x * self.BaseVectorX[1] * SizeMnojX + y * self.BaseVectorY[1] * SizeMnojY
            if DrawPoints:
                pygame.draw.circle(self.sc, self.ColorDraw, (self.XSize // 2 + X * (self.XSize // 2), self.YSize // 2 + Y * (self.YSize // 2)), 5)
            if DrawLines:
                pygame.draw.line(self.sc, self.ColorDraw, (self.XSize // 2 + X * (self.XSize // 2), self.YSize // 2 + Y * (self.YSize // 2)), (self.XSize // 2 + LX * (self.XSize // 2), self.YSize // 2 + LY * (self.YSize // 2)), 2)
                LX = X
                LY = Y
    def DrawFilledFigure(self, Polygons, SizeMnojX = 1, SizeMnojY = 1): #Рисует закрашенную фигуру, принимает (Полигоны многоугольника, Множитель по X, ножитель по Y)
        Pols = []
        for x, y in Polygons:
            X = self.TranslateVector[0] + x * self.BaseVectorX[0] * SizeMnojX + y * self.BaseVectorY[0] * SizeMnojY
            Y = self.TranslateVector[1] + x * self.BaseVectorX[1] * SizeMnojX + y * self.BaseVectorY[1] * SizeMnojY
            Pols.append([self.XSize // 2 + X * (self.XSize // 2), self.YSize // 2 + Y * (self.YSize // 2)])
        pygame.draw.polygon(self.sc, self.ColorDraw, Pols)
    def DrawUnfilledFigureSeq(self, Polygons, NumPolsInFig, SizeMnojX = 1, SizeMnojY = 1, DrawPoints = True, DrawLines = True): #Рисует последовательность незакрашенных фигур, принимает (Полигоны многоугольников, Количество сторон в многоугольнике, Множитель размеров по X, множитель размеров по Y, Флаг отрисоки точек, флаг отрисовки прямых)
        for i in range(0, len(Polygons), NumPolsInFig):
            self.DrawUnfilledFigure(Polygons[i:i + NumPolsInFig], SizeMnojX, SizeMnojY, DrawPoints, DrawLines)
    def DrawFilledFigureSeq(self, Polygons, NumPolsInFig, SizeMnojX = 1, SizeMnojY = 1): #Рисует следовательность закрашенных фигур, принимает (Полигоны многоугольников, Количество сторон в многоугольнике, Множитель по X, ножитель по Y)
        for i in range(0, len(Polygons), NumPolsInFig):
            self.DrawFilledFigure(Polygons[i: i + NumPolsInFig], SizeMnojX, SizeMnojY)