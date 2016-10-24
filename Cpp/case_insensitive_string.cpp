#include <string>
#include <cctype>
#include <iostream>
#include <assert.h>
#include <string.h>

//Ultimately this doesn't seem to work
//For the rather banal reason that I'm inheriting from string
//But also trying to override functions. Only way for this to 
//truly work is if I use composition and then rewrite everything. 
//Which would, of course, be a giant pain. 
//
// Code came from trying to solve this gotw problem: http://www.gotw.ca/gotw/029.htm
// Some links on why inheriting from string isn't possible:
// http://stackoverflow.com/questions/6006860/why-should-one-not-derive-from-c-std-string-class
// http://stackoverflow.com/questions/4205050/inheriting-and-overriding-functions-of-a-stdstring

class ci_string : public std::string {

    private:
        std::string lower;

    public:
        ci_string(std::string s): std::string(s), lower(s){
            std::string::iterator c;
            for(c = lower.begin(); c != lower.end(); c++){
                *c = tolower(*c);
            }
        }
        int operator==(const std::string s);

        virtual void printOn (std::ostream &strm) const;

};

int ci_string::operator==(const std::string s){
    std::string s_local(s);
    std::string::iterator c;
    for( c = s_local.begin(); c!=s_local.end(); c++){
        *c = tolower(*c);
    }

    return lower == s_local;
}

void ci_string::printOn(std::ostream &strm) const{
    strm << "lower case: " << lower << "\n true: " << *this;
}

std::ostream & operator << (std::ostream &strm, const ci_string &s){
    s.printOn(strm);
    return strm;
}


int main(){

    ci_string s("AbCdE");

    std::cout << s << std::endl;

    assert( s == "abcde" );
    assert( s == "ABCDE" );
    
    assert( strcmp(s.c_str(), "AbCdE") == 0);
    assert( strcmp(s.c_str(), "abcde") != 0);

}
