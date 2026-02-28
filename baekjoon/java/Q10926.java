import java.io.*;
import java.util.StringTokenizer;

public class Q10926 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String id = br.readLine();

        String ans = id + "??!";

        bw.write(ans);
        bw.flush();
        bw.close();
    }
}
