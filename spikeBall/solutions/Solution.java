import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int cases = input.nextInt();
        input.nextLine();
        for (int i = 0; i < cases; i++) {
            System.out.println(solve(input));
        }
    }

    public static double largestDistance(Scanner input, int centerX, int centerY){
        int spikeCount = input.nextInt();

        double largestDistance = 0;
        int curX;
        int curY;
        for (int i = 0; i < spikeCount; i++) {
            curX = input.nextInt();
            curY = input.nextInt();
            int xDif = curX - centerX;
            int yDif = curY - centerY;
            largestDistance = Math.max(largestDistance, Math.sqrt(xDif*xDif + yDif*yDif));

        }
        return largestDistance;
    }

    public static boolean solve(Scanner input) {
        int center1X = input.nextInt();
        int center1Y = input.nextInt();

        int center2X = input.nextInt();
        int center2Y = input.nextInt();

        double largestSpike1 = largestDistance(input, center1X, center1Y);
        double largestSpike2 = largestDistance(input, center2X, center2Y);
        return largestSpike1 + largestSpike2 >= Math.hypot(center1X - center2X,center1Y - center2Y);

    }

}


      