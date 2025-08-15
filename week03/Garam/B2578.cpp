#include <iostream>

using namespace std;

int bingo(int (&arr)[25][25]) {
    int h_count = 0;
    int v_count = 0;
    int d_count = 0;

    for (int i = 0; i < 5; i++) {
        int h = 0;
        int v = 0;
        int d = 0;

        for (int j = 0; j < 5; j++) {
            if (arr[i][j] == 0) h++;
            if (arr[j][i] == 0) v++;
        }

        if (h == 5) h_count++;
        if (v == 5) v_count++;
    }

    int d_1 = 0;
    int d_2 = 0;


    for (int i = 0; i < 5; i++) {
        if (arr[i][i] == 0) d_1++;
        if (arr[i][4-i] == 0) d_2++;
    }
    d_count += int(d_1 == 5) + int(d_2 == 5);

    return h_count + v_count + d_count;
}

int main()
{
    int board[25][25];
    pair<int, int> idx[26];

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            int num;
            cin >> num;
            board[i][j] = num;
            idx[num] = {i, j};
        }
    }

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            int num;
            cin >> num;
            pair<int, int> curr = idx[num];
            board[curr.first][curr.second] = 0;
            if (bingo(board) >= 3) {
                cout << (i * 5) + j + 1 << endl;
                return 0;
            }
        }
    }
}