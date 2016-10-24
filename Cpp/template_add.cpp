#include <cstdlib>
#include <iostream>

using namespace std;

// Toy example of a template function

template <typename T>
const T add(T a, T& b){
    std::cout << "\n entering add" << std::endl;
    return a+b;
}

class my_float{
        float f;
    public:
        my_float(float in_f) : f(in_f) {
            std::cout << "Constructing: "<<in_f <<std::endl;
        };
        float data() const{return f;}; 
        const my_float operator + (my_float&);
        ~my_float(){ std::cout << "Deconstructing: " << f << std::endl;};
        my_float(const my_float &in_f) : f(in_f.data()) {
            std::cout << "Copy Condsturcting: " << f << std::endl;
        };
};

const my_float my_float::operator +(my_float &rside){
    std::cout << "\n enterting operator +" << std::endl;
    float temp_float = f + rside.data();
    
    my_float temp_my_float(temp_float), tmp2(20);
    std::cout << " exiting operator +\n" << std::endl;
    return temp_my_float; 
    //I this this only works in my code because (named) RVO is done
    //Otherwise i'd be returning something that would be immediately 
    //de-allocated from the stack
    //However, I'm unsure if that's really what's going on
}

int main(){
    int a=1, b=3;
    my_float fa(1.0), fb(3.0);
    
    std::cout << "CHECK 1" << std::endl;
    cout << add(a,b) << endl; //Notice this is only for int a,b

    std::cout << "CHECK 1.5" << std::endl;
    my_float fc = add(a,b); //This constructs my_float from an int
    std::cout << "CHECK 1.75" << std::endl;
    cout << fc.data() << endl;

    std::cout << "CHECK 2" << std::endl;
    cout << fa.data() << "," << fb.data() << std::endl;
    
    std::cout << "CHECK 3" << std::endl;
    cout << add(fa, fc).data() << endl; //This is actually for my_float
    //Note the above will use a copy constructor to pass fa into add
    //This is not done for fb because fb is passed by reference
    //
    //Also, the deconstruction of 1 (from going into add) and 4 (the temporary
    //object) appear to be sommething that can happen in differing orders. 
    //It may be printed to stdout after add(fa, fc) is printed by the above line

    std::cout << "CHECK 4" << std::endl;
    return 0;
}

