#
# Minesweeper written in Python by Thomas McLean
#
import random
import os

while True:
    Line1 = []
    Line2 = []
    Line3 = []
    Line4 = []
    Line5 = []
    Line6 = []
    Line7 = []
    Line8 = []
    Line9 = []
    
    Line11 = ['#','#','#','#','#','#','#','#','#']
    Line12 = ['#','#','#','#','#','#','#','#','#']
    Line13 = ['#','#','#','#','#','#','#','#','#']
    Line14 = ['#','#','#','#','#','#','#','#','#']
    Line15 = ['#','#','#','#','#','#','#','#','#']
    Line16 = ['#','#','#','#','#','#','#','#','#']
    Line17 = ['#','#','#','#','#','#','#','#','#']
    Line18 = ['#','#','#','#','#','#','#','#','#']
    Line19 = ['#','#','#','#','#','#','#','#','#']

    Bomb_List = []
    Bomb_List.extend ((Line1, Line2, Line3, Line4, Line5, Line6, Line7, Line8, Line9))
    Board_List = []
    Board_List.extend ((Line11, Line12, Line13, Line14, Line15, Line16, Line17, Line18, Line19))

    ListNum = 0
    for i in range(9):
        for i in range(9):
            BoardStart = Bomb_List[ListNum]
            Num = random.random()
            if Num > 0.75:
                BoardStart.append(1)
            else:
                BoardStart.append(0)
        ListNum += 1

    Bomb_Amount = 0
    Hash_Amount = 0
    Counter = 0
    for Length in range(len(Bomb_List)):
        Bomb_Amount += Bomb_List[Counter].count(1)
        Counter += 1

    def Board():
        print('   +---+---+---+---+---+---+---+---+---+')
        print(' 9 | ' + ' | '.join(Line19) + ' |')
        print('   +---+---+---+---+---+---+---+---+---+')
        print(' 8 | ' + ' | '.join(Line18) + ' |')
        print('   +---+---+---+---+---+---+---+---+---+')
        print(' 7 | ' + ' | '.join(Line17) + ' |')
        print('   +---+---+---+---+---+---+---+---+---+')
        print(' 6 | ' + ' | '.join(Line16) + ' |')
        print('   +---+---+---+---+---+---+---+---+---+')
        print(' 5 | ' + ' | '.join(Line15) + ' |')
        print('   +---+---+---+---+---+---+---+---+---+')
        print(' 4 | ' + ' | '.join(Line14) + ' |')
        print('   +---+---+---+---+---+---+---+---+---+')
        print(' 3 | ' + ' | '.join(Line13) + ' |')
        print('   +---+---+---+---+---+---+---+---+---+')
        print(' 2 | ' + ' | '.join(Line12) + ' |')
        print('   +---+---+---+---+---+---+---+---+---+')
        print(' 1 | ' + ' | '.join(Line11) + ' |')
        print('   +---+---+---+---+---+---+---+---+---+')
        print('     1   2   3   4   5   6   7   8   9')
    os.system("cls")
    Board()
    while True:
        Input = input('X, Y / Flag? >> ')
        if Input not in ['Flag', 'flag', 'F', 'f']:
            Coords = Input.split()
            try:
                X = int(Coords[0]) - 1
                Y = int(Coords[1]) - 1
            except ValueError:
                print('Input Must Be A Number')
                input('Press Enter To Continue ')
            Counter = 0

            os.system("cls")
            Current = Bomb_List[Y][X]
            if int(Current) == 0:
                if X != 0:
                    if int(Bomb_List[Y][X - 1]) == 1:
                        Counter += 1
                    else:
                        pass
                else:
                    pass
                if Y != 0:
                    if int(Bomb_List[Y - 1][X]) == 1:
                        Counter += 1
                    else:
                        pass
                if Y != 0:
                    if X != 0:
                        if int(Bomb_List[Y - 1][X - 1]) == 1:
                            Counter += 1
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
                if X != 8:
                    if int(Bomb_List[Y][X + 1]) == 1:
                            Counter += 1
                    else:
                        pass
                else:
                    pass
                if Y != 8:
                    if int(Bomb_List[Y + 1][X]) == 1:
                        Counter += 1
                    else:
                        pass
                if Y != 8:
                    if X != 8:
                        if int(Bomb_List[Y + 1][X + 1]) == 1:
                            Counter += 1
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
                if Y != 0:
                    if X != 8:
                        if int(Bomb_List[Y - 1][X + 1]) == 1:
                            Counter += 1
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
                if Y != 8:
                    if X != 0:
                        if int(Bomb_List[Y + 1][X - 1]) == 1:
                            Counter += 1
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

                Add = Board_List[Y]
                Add.insert(X, str(Counter))
                del Add[X + 1]
                Board()

            else:
                Add = Board_List[Y]
                Add.insert(X, '!')
                del Add[X + 1]
                Board()
                print('!!!YOU LOSE!!!')
                print('!!!YOU LOSE!!!')
                print('!!!YOU LOSE!!!')
                Exit = input('Run Again? >> ')
                if Exit in ['Y', 'y', 'Yes', 'yes']:
                    break
                else:
                    exit()
        else:
            Input = input('X, Y? >> ')
            Coords = Input.split()
            try:
                X = int(Coords[0]) - 1
                Y = int(Coords[1]) - 1
                Add = Board_List[Y]
                Add.insert(X, '$')
                del Add[X + 1]
            except ValueError:
                print('Input Must Be A Number')
                input('Press Enter To Continue')
            os.system("cls")
            Board()
            
        Counter = 0
        for Length in range(len(Board_List)):
            Hash_Amount += Board_List[Counter].count('#')
            Hash_Amount += Board_List[Counter].count('$')
            Counter += 1
        if int(Hash_Amount) == int(Bomb_Amount):
            print('__  ______  __  __   _       ______  _   ____          ')
            print('\ \/ / __ \/ / / /  | |     / / __ \/ | / / /          ')
            print(' \  / / / / / / /   | | /| / / / / /  |/ / /           ')
            print(' / / /_/ / /_/ /    | |/ |/ / /_/ / /|  /_/            ')
            print('/_/\____/\____/____ |__/|__/\____/_/_|_(_)____       _ ')
            print('  / ____/ __ \/ __ \/ __ \       / / __ \/ __ )   _ | |')
            print(' / / __/ / / / / / / / / /  __  / / / / / __  |  (_)/ /')
            print('/ /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ / /_/ /  _  / / ')
            print('\____/\____/\____/_____/   \____/\____/_____/  (_)/_/  ')
            print('                                                /_/    ')
            Exit = input('Run Again? >> ')
            if Exit in ['Y', 'y', 'Yes', 'yes']:
                break
            else:
                exit()
        else:
            Hash_Amount = 0