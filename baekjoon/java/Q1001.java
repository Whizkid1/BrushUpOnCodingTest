import java.io.*;
import java.util.StringTokenizer;

public class Q1001 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int f = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int answer = f - s;

        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}
