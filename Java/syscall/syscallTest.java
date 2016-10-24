import java.lang.*;
import java.util.*;
import java.io.*;

public class syscallTest{
    // A silly small example of writing a function out to a file,
    // compiling it, and running it from within a java program.
    // I wrote it to better understand file io and interactin with
    // a shell from a java program.

    public static void main(String args[]){
        
        String sourceFileName = "Script.java";
        String source = "import java.lang.*;\nimport java.util.*;\n"
            + "\npublic class Script{\n"
            + "    public static void main(String args[]){\n"
            + "        System.out.println(\"Hello!\");\n"
            + "    }\n}";

        try{
            FileWriter sourceFile = new FileWriter(sourceFileName);
            BufferedWriter out = new BufferedWriter(sourceFile);

            out.write(source);
            out.flush();
            out.close();

            ProcessBuilder pb = new ProcessBuilder("javac", "Script.java");
            Process proc = pb.start();
            proc.waitFor();


            pb = new ProcessBuilder("java", "Script");
            proc = pb.start();

            InputStream is = proc.getInputStream();
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader br = new BufferedReader(isr);

            String line;

            System.out.println("The output of the script was:");
            while((line = br.readLine()) != null){
                System.out.println(line);
            }

        }catch(Exception e){
            System.out.println("Error "+e.getMessage());
            e.printStackTrace();
            System.exit(-1);
        }
    }
}
