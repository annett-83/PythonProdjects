# игра в крестики нолики
#создаем поле для игры на pygame
import pygame # устанавливаем программу на питоне
import sys
#функция для проверки победителя
def check_win(mas,sing):
    zeroes= 0 # определяем ничью(для это нужно определить 0 в массиве)
    # по вертикали и горизонтали
    for row in mas:
        zeroes+= row.count(0)
        if row.count(sing)==3:
            return sing # показывает кто выйграл х или 0 вертикали и горизонтали
    for col in range(3):
        if mas [0] [col]==sing and mas[1] [col]== sing and mas[2] [col]==sing:
            return sing
    # показывает кто выйграл х или 0 диаганили
        if mas[0][0] == sing and mas[1][1] == sing and mas[2][2] == sing:
            return sing
        if mas[0][2] == sing and mas[1][1] == sing and mas[2][0] == sing:
            return sing
        if zeroes == 0:
            return " ничья"
    return False
# задаем все необходимые параметры
pygame.init()
size_block = (100) #задаем размер игравого окна в пиксилях 
margin = 15 # ширина одой колонки 15 пикселей
width= heigth = size_block*3 + margin *4 #размеры ячеек в игровом поле
size_window = (width, heigth)
screen= pygame.display.set_mode(size_window) # передаем значения рамеры окна
pygame.display.set_caption("крестики-нолики") # задаем название игры в игровом окне
# выбираем цвета для нашего игравого поля
red = (255,0,0) # цвет для объявления результат игры
yellow = (255, 255, 0) # цвет для 0
white = (255,250,250)  # цвет для чистого поля
green = (0, 255, 0)  # цвет для х
black = (0, 0, 0) # заливка экрана в конце игры
# создаем массив, который будет отображать значения в игровом поле сначала
#создаем гениратор списка
mas =[[0] * 3 for i in range(3)] # ячейки еще пустые
query = 0 #постепенно увеличиваем на 1, получаем множество целых чисел
game_over = False # игра должна продолжаться
while True: # команда открыть, зарыть окно в pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            # описание условий открытия и закрытия окон
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # получаем координаты как картэж со значениями переменных (х,у)
            x_mouse, y_mouse = pygame.mouse.get_pos()
            #print(f"x={x_mouse} y= {y_mouse}")
            col = x_mouse//(size_block + margin)
            row = y_mouse//(size_block + margin)
            # что бы понимать какой игрок ходит, числа будут четные и нечетные
            # чтобы поставленный символ нельзя было менять, нужно сделать проверку
            if mas[row][col] == 0:
                if query % 2==0:
                    mas[row][col] = "x" # будет другой цвет, если нажать на ячейку в игровом поле
                else:
                    mas[row][col] = "o"
                query += 1
                # что бы начать игру заново нужно нажать пробел
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                game_over = False
                mas = [[0] * 3 for i in range(3)]
                query = 0
                screen.fill(black)

    if not game_over:
        for row in range(3):  # число рядов с ячейами
            for col in range(3): # число ячеек по оси х в игровом поле
        # устанавливаем символы и цвет
                if mas[row][col] == "x":
                    color = yellow
                elif mas[row][col] == "o":
                    color = green
                else:
                    color = white
                x = col * size_block + (col +1 ) * margin # расширяем нашу колонку по оси х по шрине игравого поля и делим на ячейки
                y = row * size_block + (row + 1) * margin
        # параметры ячеек
                pygame.draw.rect(screen,color, (x, y, size_block, size_block))
            # создаем символ для ячеек х
                if color == yellow:
                # рисуем х белым цветом, выравниваем (-5) по центру и задаем толщину линии (3)
                    pygame.draw.line(screen, white, (x+5, y+5), (x+size_block-5, y+ size_block-5),3)
                    pygame.draw.line(screen, white, (x + size_block-5, y+5), (x+5, y+ size_block-5), 3)
            # создаем символ для ячеек 0
                elif color == green:
            # для 0 используем готовую функцию circle, вычисляем радиус для 0       
                    pygame.draw.circle(screen,white, (x+size_block//2, y + size_block//2), size_block//2-3,3)
        if (query-1)%2==0: # для х
            game_over = check_win(mas, "x")
        else: # для 0
            game_over = check_win(mas, "o")
        if game_over: #если проиграл
            screen.fill(black) # закрашиваем экран черным
            font = pygame.font.SysFont("arial", 80) # шрифт и его размер
            text1 = font.render(game_over, True, red) #содержит текст game over
            text_rect = text1.get_rect() #узнаем его координаты
            text_x = screen.get_width()/2-text_rect.width/2 # находит центр экрана
            text_y = screen.get_width()/2- text_rect.height/2 # находит центр экрана
            screen.blit(text1, [text_x, text_y]) # прикрепляет текст по найденным координатам
        pygame.display.update()
