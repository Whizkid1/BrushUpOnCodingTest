import java.io.*;
import java.util.StringTokenizer;

public class Q10430 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int fa = (a + b) % c;
        int sa = ((a % c) + (b % c)) % c;
        int ta = (a * b) % c;
        int fua = ((a % c) * (b % c)) % c;

        bw.write(String.valueOf(fa));
        bw.newLine();
        bw.write(String.valueOf(sa));
        bw.newLine();
        bw.write(String.valueOf(ta));
        bw.newLine();
        bw.write(String.valueOf(fua));
        bw.newLine();
        bw.flush();
        bw.close();

    }
}
