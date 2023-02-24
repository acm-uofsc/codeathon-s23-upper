import java.util.*;

public class Solution {
    static int xDim, yDim;
    static String[] board;
    static HashMap<Character, int[]> arrowToDirection = new HashMap<>();
    static HashMap<String, Integer> everSeen = new HashMap<>();
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        xDim = input.nextInt();
        yDim = input.nextInt();
        input.nextLine(); // consume the newline character
        
        board = new String[yDim];
        for (int i = 0; i < yDim; i++) {
            board[i] = input.nextLine();
        }
        
        arrowToDirection.put('^', new int[]{-1, 0});
        arrowToDirection.put('>', new int[]{0, 1});
        arrowToDirection.put('v', new int[]{1, 0});
        arrowToDirection.put('<', new int[]{0, -1});
        
        int pathLength;
        HashMap<String, Integer> curPathSeen;
        for (int y = 0; y < yDim; y++) {
            for (int x = 0; x < xDim; x++) {
                curPathSeen = new HashMap<>();
                pathLength = dfs(x, y, 0, curPathSeen);
            }
        }
        
        int maxEverSeen = 0;
        for (int y = 0; y < yDim; y++) {
            for (int x = 0; x < xDim; x++) {
                String pos = y + "," + x;
                // System.out.print(everSeen.get(pos) + "\t");
                maxEverSeen = Math.max(maxEverSeen, everSeen.get(pos));
            }
            // System.out.println();
        }
        System.out.println(maxEverSeen);
    }
    
    static int dfs(int x, int y, int pathLength, HashMap<String, Integer> curPathSeen) {
        /* returns how many tiles were reachable from this (x, y) */
        String curPos = y + "," + x;
        if (x < 0 || x >= xDim || y < 0 || y >= yDim) {
            return pathLength;
        }
        if (curPathSeen.containsKey(curPos)) {
            for (Map.Entry<String, Integer> entry : curPathSeen.entrySet()) {
                String spot = entry.getKey();
                int value = entry.getValue();
                if (value >= curPathSeen.get(curPos)) {
                    everSeen.put(spot, pathLength - curPathSeen.get(curPos));
                }
            }
            return pathLength;
        }
        curPathSeen.put(curPos, pathLength);
        // if (everSeen.containsKey(curPos)) {
        //     return pathLength + everSeen.get(curPos);
        // }
        int[] direction = arrowToDirection.get(board[y].charAt(x));
        int dy = direction[0];
        int dx = direction[1];
        x += dx;
        y += dy;
        int totalPathLength = dfs(x, y, pathLength + 1, curPathSeen);
        everSeen.put(curPos, Math.max(everSeen.getOrDefault(curPos, 0), totalPathLength - pathLength));
        return totalPathLength;
    }
}
