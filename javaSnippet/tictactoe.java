package proj;
import java.util.Scanner;

public class tictactoe {
    private char[][] grid;
    private boolean isGameOver;
    private boolean turnPlayer;

    public tictactoe() {
        grid = new char[3][3];
        isGameOver = false;
        turnPlayer = true;
        for (int i = 0; i<3; i++) {
            for (int j = 0; j<3; j++) {
                grid[i][j] = '-';
            }
        }
    }

    public boolean isBoardFull() {
        for (int i = 0; i<3; i++) {
            for (int j = 0; j<3; j++) {
                if (grid[i][j] == '-') {
                    return false;
                }
            }
        }
        return true;
    }

    public void assignSquare(char c,int row, int col) {
        if (row < 0 || row >= 3 || col < 0 || col >= 3) {
            System.out.println("invalid coordinates");
            return;
        }
        if (grid[row][col] != '-') {
            System.out.println("cell is occupied");
        } else if (c == 'X' || c == 'O') {
            grid[row][col] = c;
            if (c == 'X') {
                aiMove();
            }
        } else {
            System.out.println("invalid input");
        }
    }

    public void aiMove() {
        for (int i = 0; i<3; i++) {
            for (int j = 0; j<3; j++) {
                if (grid[i][j] == '-') {
                    assignSquare('O',i,j);
                    return;
                }
            }
        }
        throw new java.lang.Error("AI cannot make any valid move");
    }

    public void printBoard() {
        String row;
        for (int i = 0; i<3; i++) {
            row = "";
            for (int j = 0; j<3; j++) {
                row += grid[i][j];
                if (j != 2) {
                    row += "|";
                }
            }
            System.out.println(row);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // game.assignSquare('X',0,1);
        // game.aiMove();
        // game.aiMove();
        // game.printBoard();
        String row;
        String col;
        int r;
        int c;
        while (true) {
            tictactoe game = new tictactoe();
            while (!game.isBoardFull()) {
                game.printBoard();
                System.out.println("row?");
                row = sc.next();
                System.out.println("col?");
                col = sc.next();
                try {
                    r = Integer.parseInt(row);
                    c = Integer.parseInt(col);
                    game.assignSquare('X',r,c);
                } catch (Exception e) {
                    System.out.println("invalid input");
                }

            }
        }
    }
}