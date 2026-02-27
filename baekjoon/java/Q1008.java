import java.io.*;
import java.util.StringTokenizer;

public class Q1008 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        // -> int / int 는 자동 반올림 결과... 답을 받는 변수가 double 형이어도 안됨
        double f = Double.parseDouble(st.nextToken());
        double s = Double.parseDouble(st.nextToken());
        double ans = f / s;

        bw.write(String.valueOf(ans));
        bw.flush();
        bw.close();
    }
}
