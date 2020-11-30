# Definitions
def show():
    print()
    print(f"   0   1  2  ")
    print("--------------")
    for i, row in enumerate(field):
        row_str = f"{i}| " + " | ".join(row) + " |"
        print(row_str)
        print("__")
    print()

#---------------------------
# Делаем ход
def ask():
    while True:
        try:
            x, y = map(int, input("       ваш ход: ").split())
            if 0 > x or x > 2 or 0 > y or y > 2:  # <=2 and 0<= y<=2:
                print("Координаты вне диапозона!")
            elif field[x][y] != " ":
                print("ячейка не доступна.")
            else:
                return x, y
        except:
            print("ошибка при обработке.")

#---------------------------
def chek_win():
    winner=" "
    for i in range(3):
        if field[0][i]!=" "and field[0][i]==field[1][i]==field[2][i]:
            winner=field[0][i]
    for i in range(3):
        if field[i][0]!=" "and field[i][0]==field[i][1]==field[i][2]:
            winner=field[i][0]
    if field[0][0]!=" "and field[0][0]==field[1][1]==field[2][2]:
        winner=field[0][0]
    if field[2][0]!=" "and field[2][0]==field[1][1]==field[0][2]:
        winner=field[2][0]
    if winner!=" ":
        show()
        print(f" Ура {winner} победа!")
        return True# игра крестики нолики
# создаем поле
# =============================================================================================

while True:
    field = [[" "] * 3 for i in range(3)]
    step = 0
    while True:
        step += 1
        show()
        if step % 2 == 1:
            print("Ходит x")
        else:
            print("Ходит o")
        x, y = ask()
        if step % 2 == 1:
            field[x][y] = "x"
        else:
            field[x][y] = "o"
            # если ничья
        if chek_win():
            break
        if step == 9:
            print("НИЧЬЯ")
            break
    if str(input("Хотитите сыграть еще раз? Нажмите Y, если Да.")).lower!="y":
       break