import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Q10171 {
    public static void main(String[] args) throws IOException {

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

//        !error: text blocks are not supported in -source 11
//        bw.write("""
//                \\    /\\
//                 )  ( ')
//                (  /  )
//                 \\(__)|
//                """);
//        bw.flush();
//        bw.close();

        bw.write("\\    /\\");
        bw.newLine();	// 줄 구분자
        bw.write(" )  ( ')");
        bw.newLine();
        bw.write("(  /  )");
        bw.newLine();
        bw.write(" \\(__)|");

        bw.flush();
        bw.close();
    }
}
