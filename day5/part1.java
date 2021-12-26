import java.util.HashMap;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> field = new HashMap<>();
        Scanner scanner = new Scanner(System.in);
        Pattern pattern = Pattern.compile("(\\w+),(\\w+) -> (\\w+),(\\w+)");
        int x1 = 0, x2 = 0, y1 = 0, y2 = 0;
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
            if (x1 == x2) {
                for (int i = Math.min(y1, y2); i <= Math.max(y1, y2); i++)
                    if (field.putIfAbsent(x1 + " " + i, 1) != null)
                        field.put(x1 + " " + i, field.get(x1 + " " + i) + 1);
            }
            else if (y1==y2){
                for (int i = Math.min(x1, x2); i <= Math.max(x1, x2); i++)
                    if (field.putIfAbsent(i + " " + y1, 1) != null)
                        field.put(i + " " + y1, field.get(i + " " + y1) + 1);
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