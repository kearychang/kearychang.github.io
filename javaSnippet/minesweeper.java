package proj;
import java.util.Random;
import java.util.Scanner; 

class minesweeper {
    private int row;
    private int col;
    private int[][] grid;
    private int[][] gridPlay;
    private boolean alive;
    
    public minesweeper(int row, int col, int percent) {
        this.row = row;
        this.col = col;
        this.grid = new int[row][col];
        this.gridPlay = new int[row][col];
        this.alive = true;
        Random r = new Random();

        //Initialize grid with mines with percent chance
        for (int i = 0; i<row; i++) {
            for (int j = 0; j<col; j++) {
                this.gridPlay[i][j] = 0;
                if ((r.nextInt(100)+1) <= percent) {
                    this.grid[i][j] = -1;
                } else {
                    this.grid[i][j] = 0;
                }
            }
        }

        //Assign flags to grid
        for (int i = 0; i<row; i++) {
            for (int j = 0; j<col; j++) {
                if (this.grid[i][j] != -1) {
                    this.grid[i][j] = assignFlag(i,j);
                }
            }
        }
        System.out.println("");
    }

    private boolean isInGrid(int xCoord, int yCoord) {
        return xCoord >= 0 && yCoord >=0 && xCoord < this.row && yCoord < this.col;
    }

    private int assignFlag(int x, int y) {
        int flagCount = 0;
        for (int i = -1; i<=1; i++) {
            for (int j = -1; j<=1; j++) {
                if ((i !=0 || j != 0) && isInGrid(x + i, y + j) && this.grid[x + i][y + j] == -1) {
                    flagCount++;
                }
            }
        }
        return flagCount;
    }

    private void recurCheck(int x, int y) {
        if (!isInGrid(x,y) || this.grid[x][y] != 0 || this.gridPlay[x][y] == 1) {
            return;
        } else {
            this.gridPlay[x][y] = 1;
            System.out.println("Pos x = " + x + ", Pos y = " + y + " is clear");
            recurCheck(x - 1, y - 1);
            recurCheck(x - 1, y);
            recurCheck(x - 1, y + 1);
            recurCheck(x, y - 1);
            recurCheck(x, y + 1);
            recurCheck(x + 1, y - 1);
            recurCheck(x + 1, y);
            recurCheck(x + 1, y + 1);
        }
    }

    private void checkGame() {
        for (int i = 0; i<this.row; i++) {
            for (int j = 0; j<this.col; j++) {
                if (this.gridPlay[i][j] == 0 && this.grid[i][j] != -1) {
                    return;
                }
            }
        }
        this.alive = false;
        System.out.println("You win!");
    }

    private void checkCoord(int x, int y) {
        if (!isInGrid(x,y)) {
            System.out.println("That location isn't in the map boundaries");
        } else if (this.gridPlay[x][y] == 1) {
            System.out.println("You already checked this location for mines");
            System.out.println("There are " + this.grid[x][y] + " mines nearby");
        } else if (this.grid[x][y] == -1) {
            this.alive = false;
            System.out.println("You stepped on a mine, GAME OVER");
        } else if (this.grid[x][y] > 0) {
            this.gridPlay[x][y] = 1;
            System.out.println("You stepped close to a mine, there are " + this.grid[x][y] + " mines nearby");
        } else {
            recurCheck(x,y);
        }
        checkGame();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        minesweeper m;
        int x;
        int y;
        int row;
        int col;
        int percent;
        while (true) {
            System.out.println("New game of Minesweepers");
            System.out.println("How many rows?");
            row = scan.nextInt();
            System.out.println("How many cols?");
            col = scan.nextInt();
            System.out.println("What's the chance each cell is a mine?");
            percent = scan.nextInt();
            m = new minesweeper(row, col, percent);
            while (m.alive) {
                System.out.println("Enter x coordinates separated by space where 0 is leftmost row");
                x = scan.nextInt();
                System.out.println("Enter y coordinates separated by space where 0 is topmost col");
                y = scan.nextInt();
                m.checkCoord(x,y);
            }
        }
    }
}