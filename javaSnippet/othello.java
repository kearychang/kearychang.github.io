package proj;
import java.util.Random;
import java.util.Scanner;

public class othello {
    private char[][] grid;
    private int countEmpty;
    private int countP1;
    private int countP2;
    private boolean turnPlayer;
    private char winner;

    public othello() {
        //grid has value 'x' for player 1 and value 'o' for player 2, otherwise '_'
        Random r = new Random();
        this.countP1 = 2;
        this.countP2 = 2;
        this.countEmpty = 64;
        this.turnPlayer = (r.nextInt(2) == 0) ? true: false;
        this.grid = new char[8][8];
        for (int i = 0; i<8; i++) {
            for (int j = 0; j<8; j++) {
                this.grid[i][j] = '_';
            }
        }
        this.grid[3][3] = 'x';
        this.grid[3][4] = 'o';
        this.grid[4][3] = 'o';
        this.grid[4][4] = 'x';
        System.out.println("Let's play Othello");
        printGameState();
    }

    public char getTurnPlayer() {
        return (this.turnPlayer) ? 'x': 'o';
    }

    public void printGameState() {
        //first row is " _ _ _ _ _ _ _ _ "
        //second to last row is "|_|_|_|_|_|_|_|_|"
        //underscores are replaced with 'x' or 'o' if occupied
        String rowOutput;
        System.out.println("Board State:");
        System.out.println("  0 1 2 3 4 5 6 7 ");
        for (int i = 0; i < 8; i++) {
            rowOutput = "" + i;
            for (int j = 0; j < 8; j++) {
                rowOutput += "|" + String.valueOf(this.grid[i][j]);
            }
            rowOutput += "|";
            System.out.println(rowOutput);
        }
    }

    public boolean isGameOver() {
        //checks board state to determine winner
        //game is over if 
        //      1) a player possesses no tiles and it is after their 1st turn 
        //      2) no empty tiles left
        if (this.countEmpty == 0) {
            if (this.countP1 > this.countP2) {
                this.winner = 'x';
            } else if (this.countP1 < this.countP2) {
                this.winner = 'o';
            } else {
                this.winner = '.';
            }
            return true;
        } else if (this.countP1 <= 0) {
            this.winner = 'o';
            return true;
        } else if (this.countP2 <= 0) {
            this.winner = 'x';
            return true;
        }
        return false;
    }

    private boolean isCellIngame(int x, int y) {
        return x>=0 && y>=0 && x<8 && y<8;
    }

    private boolean isCellVacant(int x, int y) {
        return this.grid[x][y] == '_';
    }

    private void changeTurn(char player) {
        //turn changes only if there is an available vacant square on board that is adjacent to enemy
        this.turnPlayer = !this.turnPlayer;
    }

    private void propagateChange(char player, int dirX, int dirY, int x, int y) {
        int newX = x + dirX;
        int newY = y + dirY;
        while (isCellIngame(newX,newY) && !isCellVacant(newX,newY)) {
            if (this.grid[newX][newY] == player) {
                x += dirX;
                y += dirY;
                while (x!=newX || y!=newY) {
                    if (player == 'x') {
                        this.countP1++;
                        this.countP2--;
                    } else {
                        this.countP1--;
                        this.countP2++;
                    }
                    this.grid[x][y] = player;
                    x += dirX;
                    y += dirY;
                }
                return;
            }
            newX += dirX;
            newY += dirY;
        }
    }

    private void assignCell(char player, int x, int y) {
        //propagates changes by flipping tiles
        //check adjacent tiles to see if they belong to opposite player
        //then check in that direction to see if it "encloses" that player
        //if it does, flip all tiles and recurse
        for (int i = -1; i<=1; i++) {
            for (int j = -1; j<=1; j++) {
                if (!(i==0 && j==0) && isCellIngame(x+i,y+j) && this.grid[x+i][y+j] != player && this.grid[x+i][y+j] != '_') {
                    propagateChange(player,i,j,x,y);
                }
            }
        }
    }

    private boolean isNeighbourEnemy(char player, int x, int y) {
        int newX;
        int newY;
        for (int i = -1; i<=1; i++) {
            for (int j = -1; j<=1; j++) {
                newX = x;
                newY = y;
                if (!(i==0 && j==0) && isCellIngame(x+i,y+j) && this.grid[x+i][y+j] != player && this.grid[x+i][y+j] != '_') {
                    newX += i;
                    newY += j;
                    while (isCellIngame(newX,newY) && !isCellVacant(newX,newY)) {
                        if (this.grid[newX][newY] == player) {
                            return true;
                        }
                        newX += i;
                        newY += j;
                    }
                }
            }
        }
        return false;
    }

    public void makeMove(char player, int x, int y) {
        //places x/o on square (x,y)
        if (!isCellIngame(x,y)) {
            System.out.println("Invalid coordinates.\n");
            return;
        } else if (!isCellVacant(x, y)) {
            System.out.println("Cell is not empty.\n");
            return;
        } else if (!isNeighbourEnemy(player,x,y)) {
            System.out.println("Can't play there. It wouldn't flip any tiles.\n");
            return;
        }
        if (player == 'x') {
            this.countP1++;
        } else {
            this.countP2++;
        }
        this.grid[x][y] = player;
        assignCell(player,x,y);
        changeTurn(player);
        printGameState();
        if (isGameOver()) {
            System.out.println("Game is over.");
            if (this.winner == '.') {
                System.out.println("Draw");
            } else {
                System.out.println("Player " + String.valueOf(this.winner) + " wins!\n");
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char turnPlayer;
        int row;
        int col;
        othello newGame;
        while (true) {
            newGame = new othello();
            while (!newGame.isGameOver()) {
                turnPlayer = newGame.getTurnPlayer();
                System.out.println("It is Player " + String.valueOf(turnPlayer) + " turn");
                System.out.println("What row? (0 is leftmost)");
                row = sc.nextInt();
                System.out.println("What col? (0 is topmist)");
                col = sc.nextInt();
                newGame.makeMove(turnPlayer, row, col);
            }
        }
    }
}