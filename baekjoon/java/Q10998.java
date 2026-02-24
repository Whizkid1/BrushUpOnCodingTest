import java.io.*;
import java.util.StringTokenizer;

public class Q10998 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int f = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int ans = f * s;

        bw.write(String.valueOf(ans));
        bw.flush();
        bw.close();
    }
}
