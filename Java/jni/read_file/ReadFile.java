import java.util.*;

/*
 * I've seen this example a few different places online, and I'm not sure of its
 * exact origin. 
 *
 * This is run w/ the following steps:
 * Compile with:
 * javac ReadFile.java
 * Generate the header file ReadFile.h with:
 * javah -jni ReadFile
 * Compile native library with:
 * gcc -shared -o libnativelib.dylib -I /System/Library/Frameworks/JavaVM.framework/Headers nativelib.c 
 * I don't know why the output has to have that form, but other forms don't seem
 * to work. 
 */

class ReadFile{
	native byte[] loadFile(String name);

	public static void main(String args[]){
		byte buf[];
            
        System.out.println("java.library.path: " + System.getProperty("java.library.path"));

		ReadFile mappedFile = new ReadFile();
        
        // Originally loading was done in a static initializer block
        // (http://stackoverflow.com/questions/335311/static-initializer-in-java)
        // But this made path debugging difficult so I moved it here
        // Apparently loadLibrary("FOO") will look for libraries named
        // libFOO.jnilib or, on mac's, libFOO.dylib
        System.loadLibrary("nativelib");
		buf = mappedFile.loadFile("ReadFile.java");
		for(int i=0; i<buf.length; i++){
			System.out.print((char)buf[i]);
		}
	}
}
