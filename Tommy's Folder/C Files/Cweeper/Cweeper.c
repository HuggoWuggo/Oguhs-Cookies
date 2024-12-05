#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <windows.h>

int get_board_size()
{
    int board_size;
    printf("Board Size: ");
    scanf("%d", &board_size);
    return board_size;
}

bool create_board_state(int board_size, bool board_state[board_size + 2][board_size + 2])
{
    srand(time(0));

    for (int i = 0; i < board_size; i++)
    {
        for (int j = 0; j < board_size; j++)
        {
            int random_num = rand() % 10;
            if (random_num <= 2)
            {
                board_state[i + 1][j + 1] = 1;
            }
        }
    }
}

void print_board(int board_size, char board[board_size][board_size])
{
    system("cls");
    for (int i = board_size - 1; i >= 0; i--)
    {
        printf("\n   -");
        for (int j = 0; j < board_size; j++)
        {
            printf("----");
        }
        printf("\n");
        printf("%2d |", i + 1);
        for (int j = 0; j < board_size; j++)
        {
            printf(" %c |", board[i][j]);
        }
    }
    printf("\n   -");
    for (int j = 0; j < board_size; j++)
    {
        printf("----");
    }
    printf("\n     ");
    for (int j = 1; j <= board_size; j++)
    {
        printf("%-2d  ", j);
    }
    printf("\n\n");
}

int safe_check(int board_size, bool board_state[board_size + 2][board_size + 2], int x, int y)
{
    int bombs;

    if (board_state[y - 1][x - 1] == 1)
    {
        bombs++;
    }
    if (board_state[y - 1][x] == 1)
    {
        bombs++;
    }
    if (board_state[y - 1][x + 1] == 1)
    {
        bombs++;
    }
    if (board_state[y][x - 1] == 1)
    {
        bombs++;
    }
    if (board_state[y][x + 1] == 1)
    {
        bombs++;
    }
    if (board_state[y + 1][x - 1] == 1)
    {
        bombs++;
    }
    if (board_state[y + 1][x] == 1)
    {
        bombs++;
    }
    if (board_state[y + 1][x + 1] == 1)
    {
        bombs++;
    }

    return bombs;
}

bool check_win(int board_size, char board[board_size][board_size], int bomb_amount)
{
    int available_squares = 0;
    for (int i = 0; i < board_size; i++)
    {
        for (int j = 0; j < board_size; j++)
        {
            if (board[i][j] == '#' || board[i][j] == '?')
            {
                available_squares++;
            }
        }
    }
    if (available_squares == bomb_amount)
    {
        printf("\nYou Win!");
        getchar();
        getchar();
        return false;
    }
    else
    {
        return true;
    }
}

int main()
{
    int board_size = get_board_size();

    bool board_state[board_size + 2][board_size + 2];

    for (int i = 0; i < board_size + 2; i++)
    {
        for (int j = 0; j < board_size + 2; j++)
        {
            board_state[i][j] = 0;
        }
    }

    create_board_state(board_size, board_state);

    char board[board_size][board_size];

    for (int i = 0; i < board_size; i++)
    {
        for (int j = 0; j < board_size; j++)
        {
            board[i][j] = '#';
        }
    }

    int bomb_amount;
    for (int i = 0; i < board_size + 2; i++)
    {
        for (int j = 0; j < board_size + 2; j++)
        {
            if (board_state[i][j] == 1)
            {
                bomb_amount++;
            }
        }
    }

    bool run = true;

    int x = 99;
    int y;
    char flag;

    while (run)
    {
        print_board(board_size, board);
        //scanf(" %c", &flag);
        if (x != 99) 
        {
            printf("Flag? ");
            getchar();
            flag = getchar();
        }
        printf("X: ");
        scanf("%d", &x);
        printf("Y: ");
        scanf("%d", &y);

        if (x < 1 || y < 1 || x >= sizeof(board) / sizeof(board[0]) + 1 || y >= sizeof(board) / sizeof(board[0]) + 1)
        {
            printf("Coordinates Out Of Range");
            Sleep(1000);
        }
        else if (flag == 'f')
        {
            board[y - 1][x - 1] = '?';
            print_board(board_size, board);
        }
        else if (board_state[y][x] == 1)
        {
            board[y - 1][x - 1] = '*';
            print_board(board_size, board);
            printf("\nYou Lose!");
            run = false;
            getchar();
            getchar();
        }
        else
        {
            int bombs = safe_check(board_size, board_state, x, y);
            board[y - 1][x - 1] = bombs + 48;
            print_board(board_size, board);
            run = check_win(board_size, board, bomb_amount);
        }
    }

    return 0;
}