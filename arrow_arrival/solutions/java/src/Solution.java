
import java.util.*;

public class Solution {

    public static String[] board;
    public static int[][] depthAtSpot;
    public static boolean[][] everSeenSpot;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int xDim = input.nextInt();
        int yDim = input.nextInt();
        input.nextLine();
        board = new String[yDim];
        for (int y = 0; y < yDim; y++) {
            board[y] = input.nextLine();
        }

        depthAtSpot = new int[yDim][xDim];
        int highest = 0;

        everSeenSpot = new boolean[yDim][xDim];
        for (int y = 0; y < yDim; y++) {
            for (int x = 0; x < xDim; x++) {
                int[][] curPath = new int[yDim][xDim];
                highest = Math.max(highest, dfs(0, y, x, curPath));
                System.out.print(depthAtSpot[y][x] + "   ");
            }
            System.out.println();
        }
        System.out.println(highest);

    }

    public static boolean inBoard(int x, int y, String[] board) {
        return y >= 0 && y < board.length && x >= 0 && x < board[0].length();
    }

    public static void fillInLoopedPath(int y, int x, int value) {
        if (depthAtSpot[y][x] == value) {
            return;
        }
        depthAtSpot[y][x] = value;
        int newX = x;
        int newY = y;
        if (board[y].charAt(x) == '^') {
            newY -= 1;
            fillInLoopedPath(newY, newX, value);
        } else if (board[y].charAt(x) == 'v') {
            newY += 1;
            fillInLoopedPath(newY, newX, value);
        } else if (board[y].charAt(x) == '>') {
            newX += 1;
            fillInLoopedPath(newY, newX, value);
        } else if (board[y].charAt(x) == '<') {
            newX -= 1;
            fillInLoopedPath(newY, newX, value);
        }
    }

    public static int dfs(int currentDepth, int y, int x, int[][] curPath) {
//        System.out.println(y + " " + x + " " + currentDepth);
        if (everSeenSpot[y][x]) {
            if (curPath[y][x] > 0) {
                fillInLoopedPath(y, x, currentDepth - curPath[y][x]);

            }
//            if (depthAtSpot[y][x] == 0)
//                depthAtSpot[y][x] = currentDepth + depthAtSpot[y][x];
            return depthAtSpot[y][x] + currentDepth - 1;
        }
        everSeenSpot[y][x] = true;
        curPath[y][x] = currentDepth;
        int endingDepth = 1;
        int newX = x;
        int newY = y;

        boolean deadEnd = false;
        if (board[y].charAt(x) == '^') {
            newY -= 1;
            if (inBoard(newX, newY, board))
                endingDepth += dfs(currentDepth + 1, newY, newX, curPath);
            else {
                deadEnd = true;
            }
        } else if (board[y].charAt(x) == 'v') {
            newY += 1;
            if (inBoard(newX, newY, board))
                endingDepth += dfs(currentDepth + 1, newY, newX, curPath);
            else {
                deadEnd = true;
            }
        } else if (board[y].charAt(x) == '>') {
            newX += 1;
            if (inBoard(newX, newY, board))
                endingDepth += dfs(currentDepth + 1, newY, newX, curPath);
            else {
                deadEnd = true;
            }
        } else if (board[y].charAt(x) == '<') {
            newX -= 1;
            if (inBoard(newX, newY, board))
                endingDepth += dfs(currentDepth + 1, newY, newX, curPath);
            else {
                deadEnd = true;
            }
        } else {
            System.out.println("WAS NOT AN ARROW");
            System.exit(1);
        }
//        if (deadEnd)
//            depthAtSpot[y][x] = 1;
//        else
//        if(endingDepth)

        depthAtSpot[y][x] = Math.max(depthAtSpot[y][x], endingDepth);
        return depthAtSpot[y][x];
    }
}