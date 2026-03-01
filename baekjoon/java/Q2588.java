import java.io.*;

public class Q2588 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int f = Integer.parseInt(br.readLine());
//        int s = Integer.parseInt(br.readLine());
        String s = br.readLine();

        int sf = Integer.parseInt(s.substring(2, 3));
        int ss = Integer.parseInt(s.substring(1, 2));
        int st = Integer.parseInt(s.substring(0, 1));
        int si = Integer.parseInt(s);

        bw.write(String.valueOf(f * sf));
        bw.newLine();
        bw.write(String.valueOf(f * ss));
        bw.newLine();
        bw.write(String.valueOf(f * st));
        bw.newLine();
        bw.write(String.valueOf(f * si));
        bw.newLine();

        bw.flush();
        bw.close();
    }
}
