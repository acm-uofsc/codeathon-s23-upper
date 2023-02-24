
import java.io.*;
import java.util.*;

public class Solution {


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int cases = input.nextInt();
        input.nextLine();
        for (int i = 0; i < cases; i++) {
            solve(input);
        }

    }

    public static void solve(Scanner input) {
        int length = input.nextInt();
        Node head = new Node(-123, null, null);
        Node cur = head;
        Node[] numberToNode = new Node[length + 2];
        numberToNode[0] = head;
        for (int i = 1; i < length + 1; i++) {
            cur.next = new Node(i, null, cur);
            cur = cur.next;
            numberToNode[i] = cur;
            //            numberToNode.put(i, cur);
        }
        cur.next = new Node(-11, null, cur);
        numberToNode[length + 1] = cur.next;

        doMoves(input, numberToNode);
    }

    public static void doMoves(Scanner input, Node[] numberToNode) {
        int s, e, a;
        int moves = input.nextInt();
        for (int i = 0; i < moves; i++) {
            s = input.nextInt();
            e = input.nextInt();
            a = input.nextInt();
            Node startNode = numberToNode[s];
            Node endNode = numberToNode[e];
            Node toInsertAfter = numberToNode[a];

            Node beforeStart = startNode.prev;
            Node afterEnd = endNode.next;
            beforeStart.next = afterEnd;
            afterEnd.prev = beforeStart;

            Node afterToInsertAfter = toInsertAfter.next;
            toInsertAfter.next = startNode;
            startNode.prev = toInsertAfter;

            endNode.next = afterToInsertAfter;
            afterToInsertAfter.prev = endNode;
        }

//      purposely done naively
        int[] nodeOrder = new int[numberToNode.length];
        Node cur = numberToNode[0];
        for (int i = 0; i < numberToNode.length; i++) {
            nodeOrder[i] = cur.val;
            cur = cur.next;
        }
        for (int i = numberToNode.length - 6; i < numberToNode.length - 1; i++) {
            System.out.print(nodeOrder[i] + " ");
        }
        System.out.println();
    }
}

class Node {
    public int val;
    public Node next;
    public Node prev;

    public Node(int val, Node next, Node prev) {
        this.val = val;
        this.next = next;
        this.prev = prev;
    }
}