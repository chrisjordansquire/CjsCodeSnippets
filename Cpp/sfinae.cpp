#include <algorithm>
#include <iostream>
#include <iterator>
#include <type_traits>
#include <vector>

// Trying out the example here:
// https://debugfailure.wordpress.com/2009/10/06/understanding-sfinae/

template <typename T>
class is_container{
    typedef char true_type;
    struct false_type{ true_type _[2]; };
    template <typename U>
        static true_type has_iterator_checker(
                typename U::iterator *);
    template <typename U>
        static false_type has_iterator_checker(...);

    public:
        enum {value = (sizeof(has_iterator_checker<T>(0)) ==
                sizeof(true_type)) };
};

template <typename T>
typename std::enable_if<!is_container<T>::value>::type
    super_print(T const &t){
       std::cout << t << std::endl;
    }

template <typename T>
typename std::enable_if<is_container<T>::value>::type
    super_print(T const &t){
        typedef typename T::value_type value_type;
        std::copy(t.begin(),
                t.end(),
                std::ostream_iterator<value_type>(std::cout, ", "));
        std::cout << std::endl;
}


int main(){
    super_print(10);
    std::vector<int> b;
    for(int i=1; i<5; i++){
       b.push_back(i);
    }

    super_print(b);
}

        
        
       


