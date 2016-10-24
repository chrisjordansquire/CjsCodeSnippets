#include "iostream"
#include "sstream"
#include "stack"
#include "vector"

// Basic data structure and classic interview problem
// Also a great simple learning exercise for C++

template<typename T>
class MaxStack {

 public:
  MaxStack() = default;

  ~MaxStack() = default;

  bool empty() const { return stack.empty(); }

  size_t size() const { return stack.size(); }

  void push(const T x);

  void pop();

  const T &top() const { return stack.top(); }

  const T &max() const { return maxes.top(); }

 private:
  std::stack<T> stack;
  std::stack<T> maxes;
};

template<typename T>
void MaxStack<T>::push(const T x) {
  stack.push(x);
  if (maxes.empty() || maxes.top() <= x) {
    maxes.push(x);
  }
}

template<typename T>
void MaxStack<T>::pop() {
  T top = stack.top();
  if (maxes.top() == top) {
    maxes.pop();
  }
  stack.pop();
}

int main() {
  std::vector<double> v{2.0, 5.0, -1.0, 7.0, -10.0};
  std::stringstream stringstream;
  std::for_each(v.begin(), v.end(), [&](double &x) { stringstream << x << ", "; });
  std::cout << stringstream.str() << std::endl;
  std::for_each(v.begin(), v.end() - 1, [](double &x) { x++; });
  stringstream.str("");
  std::for_each(v.begin(), v.end(), [&](double &x) { stringstream << x << ", "; });
  std::cout << stringstream.str() << std::endl;

  MaxStack<double> maxStack;
  std::for_each(v.begin(), v.end(), [&](double &x) { maxStack.push(x); });
  while (!maxStack.empty()) {
    std::cout << maxStack.top() << ", " << maxStack.max() << ", " << maxStack.size() << ", " << maxStack.empty() <<
        std::endl;
    maxStack.pop();
  }
  std::cout << maxStack.size() << ", " << maxStack.empty() << std::endl;
}


