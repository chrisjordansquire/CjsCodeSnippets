#include <iostream>
#include <string>
#include "stdlib.h"
#include "stdio.h"

// I can never remember how to write class printers in C++
// Deriving everything from Object which has toString in Java
// is cleaner, though it definitely has an overhead. 

class A{
    public:
        int i;
        std::string toString() const;
        A(int i_, int j_): i(i_), j(j_){};
        friend std::ostream& operator<<(std::ostream&, const A&);
    private:
        int j;
};

//This was just a definition of a toString function. If it was used in
//the ostream << operator for A then the operator << could be a free-standing
//class rather than a friend class. The below also uses snprintf since
//iota is a nonstandard function not found in glibc. 
std::string A::toString() const{
    const int MAX = 20;
    char i_[MAX], j_[MAX];
    snprintf(i_, MAX, "%d", i);
    snprintf(j_, MAX, "%d", j);
    return std::string(i_) + ", " + std::string(j_);
}

//If the ostream << operator requires access to private members of the
//class then it must be declared as a friend function
std::ostream& operator<<(std::ostream &strm, const A &a){
    return strm << "A(" << a.i << a.j << ")";
}

class B : public A{
    public:
        int k;
        B(int i_, int j_, int k_): A(i_, j_), k(k_){};
};

//If the print operator doesn't require the private members of the class
//then it can be delcared as a free-standing operator overload
//rather than a friend class
std::ostream& operator<<(std::ostream &strm, const B &b){
    return strm << "B(" << b.toString() << ", " <<  b.k << ")";
}

int main(){
	int a,b;
    
    A *pA = new A(1,2);
    B *pB = new B(5,6, 10);
    pB->i = 5;
    pB->k = 12;

    std::cout << pA->toString() << std::endl;
    std::cout << *pA << std::endl;
    std::cout << *pB << std::endl;

	try{
        std::cout << "Loops while typing in two sequences of digits that "
            "can be converted to int" << std::endl;
		while(std::cin >> a >> b){
			std::cout << "a: " << a << " b: " << b << std::endl;
		}
	}
	catch(std::exception &e){
		std::cout << "exception caught: " << e.what() << std::endl;
	}
}
