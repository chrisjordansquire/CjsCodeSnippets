#include <iostream>
#include <sstream>

// Testing out writing a template container in C++
// Still needs a copy constructor and an assignment operator

template<typename T>
struct Node {
  T value;
  Node<T> *prev;
  Node<T> *next;

  Node(T v, Node<T> *p, Node<T> *n) {
    this->value = v;
    this->prev = p;
    this->next = n;
  }

};

template<typename T>
class LinkedList {
 private:
  Node<T> *head;

 public:

  LinkedList() : head(NULL) { }

  void add(T n) {
    if (head == NULL) {
      head = new Node<T>(n, NULL, NULL);
    } else {
      Node<T> *a = head;
      while (a->next != NULL) {
        a = a->next;
      }
      a->next = new Node<T>(n, a, NULL);
    }
  }

  ~LinkedList() {
    Node<T> *a = head;
    while (a->next != NULL) {
      a = a->next;
      delete a->prev;
    }
    if (a != NULL) {
      delete a;
    }
  }

  LinkedList &operator+(T n) {
    this->add(n);
    return *this;
  }


  std::string toString() const {
    std::ostringstream s;
    Node<T> *a = head;
    while (a != NULL) {
      s << a->value;
      if (a->next != NULL) {
        s << ", ";
      }
      a = a->next;
    }
    return s.str();
  }

  bool remove(T n) {
    Node<T> *a = head;
    if (a == NULL) {
      return false;
    } else if (a->value == n) {
      a->next->prev = NULL;
      head = a->next;
      delete a;
      return true;
    }

    while (a->next != NULL) {
      if (a->value == n) {
        a->prev->next = a->next;
        a->next->prev = a->prev;
        delete a;
        return true;
      }
      a = a->next;
    }
    if (a->value == n) {
      a->prev->next = NULL;
      delete a;
      return true;
    }
    return false;
  }
};

template<typename T>
std::ostream &operator<<(std::ostream &strm, const LinkedList<T> &L) {
  return strm << L.toString();
}

int run_linkedlist() {

  LinkedList<int> x;
  for (int i = 0; i < 10; i++) {
    x.add(i);
  }
  std::cout << x << std::endl;
  int remove[] = {5, 9, 0};
  int N = 3;
  for (int i = 0; i < N; i++) {
    x.remove(remove[i]);
    std::cout << x << std::endl;
  }
  (x + 4) + 20;
  std::cout << x << std::endl;

  LinkedList<std::string> y;
  for (int i = 0; i < 10; i++) {
    char tmp = (char) ('a' + i);
    y.add(std::string(&tmp));
  }
  std::cout << y << std::endl;
  y.remove("b");
  std::cout << y << std::endl;

  return 0;
}

