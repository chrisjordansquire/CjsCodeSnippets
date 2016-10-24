#First use javac HelloWorld.java to create class file
javac HelloWorld.java
#Then use javah to create the header file for HelloWorld.cpp
javah -jni HelloWorld
g++ -I /System/Library/Frameworks/JavaVM.framework/Headers -c HelloWorld.cpp 
g++ -dynamiclib -o libhelloworld.jnilib HelloWorld.o
