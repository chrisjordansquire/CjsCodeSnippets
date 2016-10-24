import std.stdio;
import file = std.file;
import std.conv;
import std.algorithm;

void main(){
    
    string numbers;

    numbers = file.readText("s.txt");
    
    int maxProd=0;
    int currSet[5]=[0,0,0,0,0];

    foreach(int i, char c ; numbers){
        int num = to!int(c) - to!int('0');
        currSet[i%5] = num;
        int prod = reduce!((a,b)=>a*b)(currSet);
        maxProd = prod > maxProd ? prod : maxProd;
    }

    writeln("The max prod is ", maxProd);

}
