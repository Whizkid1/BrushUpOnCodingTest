import java.io.*;

public class Q18108 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int budd = Integer.parseInt(br.readLine());

        // 숫자 출력 (write는 String값으로만 출력이 가능해서 String.valueOf() 문으로 변환해주어야 한다.)
        bw.write(String.valueOf(budd - 543));
        bw.flush();
        bw.close();
    }
}
