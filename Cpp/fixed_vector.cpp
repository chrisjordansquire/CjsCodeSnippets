#include <iostream>
#include <cstddef>

// A simple fixed size vector class
// Written largely as an exercise.

using std::size_t;

template<typename T, size_t size>
class fixed_vector
{
    public:
        typedef T*      iterator;
        typedef const T*    const_iterator;
        iterator begin() {return v_;}
        iterator end() {return v_+size;}
        const_iterator begin() const {return v_;}
        const_iterator end() const{ return v_+size;}
        fixed_vector() {}
        fixed_vector(const fixed_vector<T, size> &);
        fixed_vector<T,size> & operator=(const fixed_vector<T, size>& );

    private:
        T v_[size];
};

template<typename T, size_t size>
fixed_vector<T, size>::fixed_vector(const fixed_vector<T,size> &input){

    iterator it_out;
    const_iterator it_in;
    it_in = input.begin();
    it_out  = this->begin();

    for(; it_in != input.end(); it_in++, it_out++){
        *it_out = *it_in;
    }
    
}

template<typename T, size_t size>
fixed_vector<T, size>& fixed_vector<T, size>::operator=(const fixed_vector<T, size> &input){
 
    iterator it_out;
    const_iterator it_in;
    it_in = input.begin();
    it_out  = this->begin();

    for(; it_in != input.end(); it_in++, it_out++){
        *it_out = *it_in;
    }
    
    return *this;
}


int main(){
    
    fixed_vector<int, 10> int_vec;
    fixed_vector<int, 10>::iterator it;
    int count=1;
    for(it = int_vec.begin(); it != int_vec.end(); it++){
        *it=count*count;
        count++;
    }

    for(it = int_vec.begin(); it != int_vec.end(); it++){
        std::cout << *it << " ";
    }
    std::cout << "\n" << std::endl;

    fixed_vector<int, 10> test_vec(int_vec);

    for(it = test_vec.begin(); it != test_vec.end(); it++){
        std::cout << *it << " ";
    }
    std::cout << "\n" << std::endl;

    it  =int_vec.begin();
    it[2]=300;

    test_vec = int_vec;

    for(it = test_vec.begin(); it != test_vec.end(); it++){
        std::cout << *it << " ";
    }
    std::cout << "\n" << std::endl;





}
