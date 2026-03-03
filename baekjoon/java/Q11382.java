import java.io.*;
import java.util.StringTokenizer;

public class Q11382 {
    // 이 문제의 함정은 정수타입 범위 파악.....
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        Long f = Long.parseLong(st.nextToken());
        Long s = Long.parseLong(st.nextToken());
        Long t = Long.parseLong(st.nextToken());

        Long ans = f + s + t;

        bw.write(String.valueOf(ans));
        bw.flush();
        bw.close();

    }
}
