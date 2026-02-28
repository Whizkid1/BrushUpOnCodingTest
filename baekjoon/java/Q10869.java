import java.io.*;
import java.util.StringTokenizer;

public class Q10869 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int f = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());

        int plus = f + s;
        int minus = f - s;
        int multiple = f * s;
        // double divi = (double) f / (double) s;
        int quotient = f / s;
        int remainder = f % s;

        // 숫자 출력 (write는 String값으로만 출력이 가능해서 String.valueOf() 문으로 변환해주어야 한다.)
        bw.write(String.valueOf(plus));
        bw.newLine();
        bw.write(String.valueOf(minus));
        bw.newLine();
        bw.write(String.valueOf(multiple));
        bw.newLine();
        bw.write(String.valueOf(quotient));
        bw.newLine();
        bw.write(String.valueOf(remainder));
        bw.flush();
        bw.close();
    }
}
