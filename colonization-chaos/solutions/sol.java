import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] resources = new int[n];
        for (int i = 0; i < n; i++) {
            resources[i] = sc.nextInt();
        }

        int[] planets = new int[m];
        for (int i = 0; i < m; i++) {
            planets[i] = sc.nextInt();
        }

        Set<Integer> dp = new HashSet<>();
        dp.add(0);
        int highest_in_planets = Arrays.stream(planets).max().getAsInt();
        for (int value : resources) {
            Set<Integer> dp_copy = new HashSet<>(dp);
            for (int existing : dp_copy) {
                if (existing + value <= highest_in_planets) {
                    dp.add(existing + value);
                }
            }
        }
        int count = 0;
        for (int total : planets) {
            if (dp.contains(total)) {
                count++;
            }
        }
        System.out.println(count);
    }
}