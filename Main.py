from Plyg import *

Wind = Window(700, 700)
Wind.ScaleMatrix(0.5, 0.5)

f = 8

#генерация 7 черытехугольников
if f == 0:
    Pol = GenerateNewPolygonSeq(4, 7, 0.4, 0) #Генерация последовательности из 7ми правильных четырехугольников
    Pol = RotateFigureDegSeq(Pol, 45, 4) #Поворот каждого чертырехугольника из последовательности на 45 градусов
    Pol = ScalePolygonSeq(Pol, 4, 0.2, 0.2) #Масштабирование каждого четырехугольника из последовательности на (0.2 по x, 0.2 по y)
    Pol = TranslatePolygon(Pol, -(4 / 3.5), 0) #Перемещение полигонов на (-(4 / 3.5) по x, 0 по y)
    while 1: #бесконечный цикл
        for e in pygame.event.get(): #отлов сообщений окну
            if e.type == pygame.QUIT: #Поиск сообщения о выходе из приложения
                exit() #Выход
        Wind.ClearScreen() #Очистка экрана

        Wind.DrawUnfilledFigureSeq(Pol, 4) #Отрисовка последовательности незакрашенных четырехугольников

        Wind.UpdateImage() #Отрисовка буффера пикселей на экран
#генерация 7 треугольников
if f == 1:
    Pol = GenerateNewPolygonSeq(3, 7, 0.4, 0) #Генерация последовательности из 7ми правильных треугольников
    Pol = RotateFigureDegSeq(Pol, 45, 3) #Поворот каждого треугольника из последовательности на 45 градусов
    Pol = ScalePolygonSeq(Pol, 3, 0.2, 0.2) #Масштабирование каждого треугольника из последовательности на (0.2 по x, 0.2 по y)
    Pol = TranslatePolygon(Pol, -(4 / 3.5), 0) #Перемещение полигонов на (-(4 / 3.5) по x, 0 по y)
    while 1: #бесконечный цикл
        for e in pygame.event.get(): #отлов сообщений окну
            if e.type == pygame.QUIT: #Поиск сообщения о выходе из приложения
                exit() #Выход
        Wind.ClearScreen() #Очистка экрана

        Wind.DrawUnfilledFigureSeq(Pol, 3) #Отрисовка последовательности незакрашенных треугольников

        Wind.UpdateImage() #Отрисовка буффера пикселей на экран
#генерация 7 шестиугольников
if f == 2:
    Pol = GenerateNewPolygonSeq(6, 7, 0.4, 0) #Генерация последовательности из 7ми правильных шестиугольников
    Pol = RotateFigureDegSeq(Pol, 45, 6) #Поворот каждого шестиугольника из последовательности на 45 градусов
    Pol = ScalePolygonSeq(Pol, 6, 0.2, 0.2) #Масштабирование каждого шестиугольника из последовательности на (0.2 по x, 0.2 по y)
    Pol = TranslatePolygon(Pol, -(4 / 3.5), 0) #Перемещение полигонов на (-(4 / 3.5) по x, 0 по y)
    while 1: #бесконечный цикл
        for e in pygame.event.get(): #отлов сообщений окну
            if e.type == pygame.QUIT: #Поиск сообщения о выходе из приложения
                exit() #Выход
        Wind.ClearScreen() #Очистка экрана

        Wind.DrawUnfilledFigureSeq(Pol, 6) #Отрисовка последовательности незакрашенных шестиугольниклв

        Wind.UpdateImage() #Отрисовка буффера пикселей на экран
#генерация 3 последовательных ленты из последовательности четырехугольников
if f == 3:
    Pol = GenerateNewPolygonSeq(4, 7, 0.4, 0) #Генерация последовательности из 7ми правильных четырехугольников
    Pol = RotateFigureDegSeq(Pol, 45, 4) #Поворот каждого чертырехугольника из последовательности на 45 градусов
    Pol = ScalePolygonSeq(Pol, 4, 0.2, 0.2) #Масштабирование каждого четырехугольника из последовательности на (0.2 по x, 0.2 по y)
    Pol = TranslatePolygon(Pol, -(4 / 3.5), 0) #Перемещение полигонов на (-(4 / 3.5) по x, 0 по y)
    Pol += GetSymmetry(Pol, (0, -0.3)) + GetSymmetry(Pol, (0, 0.3)) #Создание двух симметричных лент относительно точек (0 по x, +-0.3 по y)
    while 1: #бесконечный цикл
        for e in pygame.event.get(): #отлов сообщений окну
            if e.type == pygame.QUIT: #Поиск сообщения о выходе из приложения
                exit() #Выход
        Wind.ClearScreen() #Очистка экрана

        Wind.SetRotateMatrixDeg(20) #Поворот матрицы экрана под острым углом на 20 градусов
        Wind.DrawUnfilledFigureSeq(Pol, 4) #Отрисовка последовательности незакрашенных четырехугольников

        Wind.UpdateImage()
#генерация 2х пересекающихся лент из последовательности четырехугольников
if f == 4:
    Pol = GenerateNewPolygonSeq(4, 7, 0.4, 0) #Генерация последовательности из 7ми правильных четырехугольников
    Pol = RotateFigureDegSeq(Pol, 45, 4) #Поворот каждого чертырехугольника из последовательности на 45 градусов
    Pol = ScalePolygonSeq(Pol, 4, 0.2, 0.2) #Масштабирование каждого четырехугольника из последовательности на (0.2 по x, 0.2 по y)
    Pol = TranslatePolygon(Pol, -(4 / 3.5), 0) #Перемещение полигонов на (-(4 / 3.5) по x, 0 по y)
    Pol2 = GetSymmetry(Pol, (0.3, -0.3)) #Создание симметричной ленты относительно точки (0.3 по x, -0.3 по y)
    Pol2 = TranslatePolygon(Pol, -0.2, -0.1) #Перемещение полигонов на (-0.2 по x, 0.1 по y)
    while 1: #бесконечный цикл
        for e in pygame.event.get(): #отлов сообщений окну
            if e.type == pygame.QUIT: #Поиск сообщения о выходе из приложения
                exit() #Выход
        Wind.ClearScreen() #Очистка экрана

        Wind.SetRotateMatrixDeg(20) #Поворот матрицы экрана под острым углом на 20 градусов
        Wind.DrawUnfilledFigureSeq(Pol, 4) #Отрисовка последовательности незакрашенных четырехугольников
        Wind.SetRotateMatrixDeg(-20) #Поворот матрицы экрана под острым углом на -20 градусов
        Wind.DrawUnfilledFigureSeq(Pol2, 4) #Отрисовка последовательности незакрашенных четырехугольников

        Wind.UpdateImage()
#2 парралельные линии треугольников
if f == 5:
    Pol = GenerateNewPolygonSeq(3, 7, 0.4, 0) #Генерация последовательности из 7ми правильных треугольников
    Pol = RotateFigureDegSeq(Pol, 270, 3) #Поворот каждого треугольника из последовательности на 270 градусов
    Pol = ScalePolygonSeq(Pol, 3, 0.2, 0.2) #Масштабирование каждого треугольника из последовательности на (0.2 по x, 0.2 по y)
    Pol = TranslatePolygon(Pol, -(4 / 3.5), 0.3) #Перемещение полигонов на (-(4 / 3.5) по x, 0.3 по y)
    Pol += GetSymmetry(Pol, (0, 0)) #Получение линии симметричных треугольников относительно точки (0, 0)
    while 1: #бесконечный цикл
        for e in pygame.event.get(): #отлов сообщений окну
            if e.type == pygame.QUIT: #Поиск сообщения о выходе из приложения
                exit() #Выход
        Wind.ClearScreen() #Очистка экрана

        Wind.DrawUnfilledFigureSeq(Pol, 3) #Отрисовка последовательности незакрашенных треугольников

        Wind.UpdateImage() #Отрисовка буффера пикселей на экран
#Фильтрация 15 фигур имеющих различный масштаба
if f == 6:
    Pol = GenerateNewPolygonSeq(4, 4, 0.4, 0) #Генерация последовательности из четырех правильных четырехугольников
    Pol = ScalePolygonSeq(Pol, 4, 0.2, 0.2) #Масштабирование последовательности правильных четырехугольников
    Pol[:4] = ScalePolygon(Pol[:4], 1.7, 1.7) #Масштабирование одного правильного четырехугольника
    Pol2 = GenerateNewPolygonSeq(5, 3, 0.4, 0.2) #Генерация последовательности из трех правильных пятиугольников
    Pol2 = ScalePolygonSeq(Pol2, 5, 0.2, 0.2) #Масштабирование последовательности правильных пятиугольников
    Pol2 = TranslatePolygon(Pol2, -(1.0), 0.5) #перемещение последовательности правильных пятиугольников
    Pol3 = GenerateNewPolygonSeq(3, 8, 0.2, -0.2) #Генерация последовательности из восьми правильных треугольников
    Pol3 = ScalePolygonSeq(Pol3, 3, 0.2, 0.2) #Масштабирование последовательности правильных треугольников
    Pol3 = TranslatePolygon(Pol3, -(0.7), -0.5) #перемещение последовательности правильных треугольников
    Pol = MinSqarFilt(Pol, 4, 0.17) #Фильтрация четырехугольников чья площадь меньше 0.16
    Pol2 = MinSqarFilt(Pol2, 5, 0.17) #Фильтрация пятиугольников чья площадь меньше 0.16
    Pol3 = MinSqarFilt(Pol3, 3, 0.17) #Фильтрация треугольников чья площадь меньше 0.16
    while 1: #бесконечный цикл
        for e in pygame.event.get(): #отлов сообщений окну
            if e.type == pygame.QUIT: #Поиск сообщения о выходе из приложения
                exit() #Выход
        Wind.ClearScreen() #Очистка экрана

        Wind.DrawUnfilledFigureSeq(Pol, 4) #Отрисовка последовательности незакрашенных четырехугольников
        Wind.DrawUnfilledFigureSeq(Pol2, 5) #Отрисовка последовательности незакрашенных Пятиугольников
        Wind.DrawUnfilledFigureSeq(Pol3, 3) #Отрисовка последовательности незакрашенных Треугольников

        Wind.UpdateImage() #Отрисовка буффера пикселей на экран
#Фильтрация многоугольников по площади
if f == 7:
    Pol = GenerateNewPolygonSeq(3, 7, 0.4, 0) #Генерация последовательности из 7ми правильных треугольников
    Pol = RotateFigureDegSeq(Pol, 330, 3) #Поворот каждого треугольника из последовательности на 330 градусов
    Pol = ScalePolygonSeq(Pol, 3, 0.2, 0.2) #Масштабирование каждого треугольника из последовательности на (0.2 по x, 0.2 по y)
    Pol = TranslatePolygon(Pol, -(4 / 3.5), 0.3) #Перемещение полигонов на (-(4 / 3.5) по x, 0.3 по y)
    Pol2 = GetSymmetry(Pol, (0, 0)) #Получение линии симметричных треугольников относительно точки (0, 0)
    Pol2 = TranslatePolygon(Pol2, -0.2, 0) #Перемещение многоугольников на (-0.2, 0)
    Pol2 = ScalePolygon(Pol2, -1, 1) #Масштабирование многоугольников на (-1, 1)
    Pol2 = ScalePolygonSeq(Pol2, 3, -1, 1) #Мастштабирование последовательности многоугольников на (-1, 1)
    Pol = ZipPolygonsSeq(Pol, Pol2, 3, 3) #Объелинение двух последовательностей треугольников
    while 1: #бесконечный цикл
        for e in pygame.event.get(): #отлов сообщений окну
            if e.type == pygame.QUIT: #Поиск сообщения о выходе из приложения
                exit() #Выход
        Wind.ClearScreen() #Очистка экрана

        Wind.DrawUnfilledFigureSeq(Pol, 6) #Отрисовка последовательности незакрашенных Шестиугольников

        Wind.UpdateImage() #Отрисовка буффера пикселей на экран
#Фильтрация всех пересекающихся фигур
if f == 8:
    Pol = GenerateNewPolygonSeq(4, 7, 0.4, 0) #Генерация последовательности из 7ми правильных четырехугольников
    Pol = RotateFigureDegSeq(Pol, 45, 4) #Поворот каждого чертырехугольника из последовательности на 45 градусов
    Pol = ScalePolygonSeq(Pol, 4, 0.2, 0.2) #Масштабирование каждого четырехугольника из последовательности на (0.2 по x, 0.2 по y)
    Pol = TranslatePolygon(Pol, -(4 / 3.5), 0) #Перемещение полигонов на (-(4 / 3.5) по x, 0 по y)
    Pol2 = GetSymmetry(Pol, (0.3, -0.3)) #Создание симметричной ленты относительно точки (0.3 по x, -0.3 по y)
    Pol2 = TranslatePolygon(Pol, -0.2, -0.1) #Перемещение полигонов на (-0.2 по x, 0.1 по y)
    Pol2 = RotateFigureDeg(Pol2, 45) #Пороворот всей последовательности на 45 градусов
    Pol3 = GenerateNewPolygonSeq(3, 4, 0.5, 0.1) #Генерация последовательности правильных треугольников
    Pol3 = ScalePolygonSeq(Pol3, 3, 0.4, 0.4) #Масштабирование последовательности полигонов
    for i in range(0, len(Pol2), 4): #Фильтрация пересечений двух последовательностей
        Pol = FiltPolygonsFigure(Pol, 4, Pol2[i: i + 4])
    for i in range(0, len(Pol3), 3): #Фильтрация пересечений двух последовательностей
        Pol = FiltPolygonsFigure(Pol, 4, Pol3[i: i + 3])
    for i in range(0, len(Pol3), 3): #Фильтрация пересечений двух последовательностей
        Pol2 = FiltPolygonsFigure(Pol2, 4, Pol3[i: i + 3])
    for i in range(0, len(Pol2), 4): #Фильтрация пересечений двух последовательностей
        Pol3 = FiltPolygonsFigure(Pol3, 3, Pol2[i: i + 4])
    while 1: #бесконечный цикл
        for e in pygame.event.get(): #отлов сообщений окну
            if e.type == pygame.QUIT: #Поиск сообщения о выходе из приложения
                exit() #Выход
        Wind.ClearScreen() #Очистка экрана

        Wind.DrawUnfilledFigureSeq(Pol, 4) #Отрисовка последовательности незакрашенных четырехугольников
        Wind.DrawUnfilledFigureSeq(Pol2, 4) #Отрисовка последовательности незакрашенных четырехугольников
        Wind.DrawUnfilledFigureSeq(Pol3, 3) #Отрисовка последовательности незакрашенных четырехугольников

        Wind.UpdateImage()
#Вращение отдельных фигур и целой последовательности
if f == 9:
    Pol = GenerateNewPolygonSeq(4, 5, 0.4, 0.0);
    Pol = TranslatePolygon(Pol, -1, 0.6)
    Pol = ScalePolygonSeq(Pol, 4, 0.2, 0.2)
    Pol += GetSymmetry(Pol, (0, 0))
    #поворот всей нижней последовательности на 45 градусов
    Pol[0:24] = RotateFigureDeg(Pol[0:24], 45)
    #поворот верхней последовательности на 45 градусов по элементам
    Pol[24:] = RotateFigureDegSeq(Pol[24:], 45, 4)
    while 1: #бесконечный цикл
        for e in pygame.event.get(): #отлов сообщений окну
            if e.type == pygame.QUIT: #Поиск сообщения о выходе из приложения
                exit() #Выход
        Wind.ClearScreen() #Очистка экрана

        Wind.DrawUnfilledFigureSeq(Pol, 4) #Отрисовка последовательности незакрашенных четырехугольников

        Wind.UpdateImage()
