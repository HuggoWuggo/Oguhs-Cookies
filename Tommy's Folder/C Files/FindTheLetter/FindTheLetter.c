#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <windows.h>

struct Tuple
{
    unsigned char background;
    unsigned char random;
    int x;
    int y;
};

struct Tuple get_random(int board_size)
{
    srand(time(0));
    struct Tuple random_items;
    do 
    {
        random_items.background = rand() % 255;
        printf("%d\n", random_items.background);
    }
    while (random_items.background <= 32 || random_items.background == 127);
    printf("%d\n", random_items.background);

    do {random_items.random = rand() % 255;}
    while (random_items.random == random_items.background || random_items.random <= 32 || random_items.random == 127);
    random_items.x = rand() % board_size;
    random_items.y = rand() % board_size;
    printf("%c\n", random_items.background);
    printf("%c\n", random_items.random);
    printf("%d\n", random_items.x);
    printf("%d\n", random_items.y);
    return random_items;
}

void create_board(int board_size, char board[board_size][board_size], struct Tuple random_items)
{
    for (int i = 0; i < board_size; i++)
    {
        for (int j = 0; j < board_size; j++)
        {
            board[i][j] = random_items.background;
        }
    }
    board[random_items.y][random_items.x] = random_items.random;

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
}

int main()
{
    
    int board_size = 3;
    int score;
    int seconds = 10;
    bool run = true;

    while (run)
    {
        int end_time = clock() + 1000 * seconds;
        char board[board_size][board_size];
        int guess_x;
        int guess_y;

        struct Tuple random_items = get_random(board_size);
        create_board(board_size, board, random_items);

        printf("\nX: ");
        scanf("%d", &guess_x);
        printf("\nY: ");
        scanf("%d", &guess_y);
        guess_x--;
        guess_y--;

        if (clock() > end_time)
        {
            printf("Too Slow!\nScore = %d", score);
            run = false;
            getchar();
            getchar();
        }
        else if (random_items.x == guess_x && random_items.y == guess_y)
        {
            score++;
            board_size++;
        }
        else
        {
            printf("Wrong!\nScore = %d", score);
            run = false;
            getchar();
            getchar();
        }
    }
    return 0;
}