package code;
import java.util.HashMap;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> field = new HashMap<>();
        Scanner scanner = new Scanner(System.in);
        Pattern pattern = Pattern.compile("(\\w+),(\\w+) -> (\\w+),(\\w+)");
        int x1 = 0, x2 = 0, y1 = 0, y2 = 0, delta_X = 0, delta_Y = 0;
        while (true) {
            String line = scanner.nextLine();
            if (line.equals("-1"))
                break;
            Matcher matcher = pattern.matcher(line);
            if (matcher.find()) {
                x1 = Integer.parseInt(matcher.group(1));
                y1 = Integer.parseInt(matcher.group(2));
                x2 = Integer.parseInt(matcher.group(3));
                y2 = Integer.parseInt(matcher.group(4));
            }
            if (x2 - x1 == 0) {
                delta_X = 0;
            }
            else {
                delta_X = (x2 - x1)/Math.abs(x2 - x1);
            }
            if (y2 - y1 == 0) {
                delta_Y = 0;
            }
            else {
                delta_Y = (y2 - y1) / Math.abs(y2 - y1);
            }
            int x = x1;
            int y = y1;
            for (int i = 0; i <= Math.max(Math.abs(x2 - x1), Math.abs(y2 - y1)); i++) {
                if (field.putIfAbsent(x + " " + y,1) != null) {
                    field.put(x + " " + y, field.get(x + " " + y) + 1);
                }
                x += delta_X;
                y += delta_Y;
            }

        }
        int res = 0;
        for (int value : field.values()) {
            if (value > 1)
                res += 1;
        }
        System.out.println(res);
    }

}