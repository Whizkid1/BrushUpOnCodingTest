import java.io.*;
// 공백을 기준으로 한 줄을 나눠서 받고 싶을 때
import java.util.StringTokenizer;

public class Q1000 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int f = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int answer = f + s;

        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}
