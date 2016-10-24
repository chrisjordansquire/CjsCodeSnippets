/*
 *      A class that implements a polynomial.  It allows
 *      for evaluation using a cache to speed evaluation
 *      at repeated points, and can print the polynomial
 *      with its coefficients.
 */

#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <vector>


class Polynomial {

 private:
  /*! Vector of coefficients, in order of decreasing powers*/
  const std::vector<double> _coef;
  /*! Cache of evaluated (point, value) pairs*/
  std::map<double, double> _cache;

 public:
  /*! \param coef The polynomial coefficients in order of
   * decreasing powers */
  Polynomial(std::vector<double> coef) : _coef(coef) { }

  ~Polynomial() { std::cout << "Polynomial Destructing" << std::endl; }

  /*! Evaluate polynomial P
   * \param x Point to evaluate the polynomial P
   * \return The value P(x) */
  double evaluate(double x);

  /*! Print polynomia to a stream.
   * \param strm Stream to print polynomial to.
   * */
  std::string toString() const;
};

std::string Polynomial::toString() const {
  std::ostringstream ostringstream;

  unsigned long p = _coef.size();

  for (int i = 0; i < (p - 1); i++) {
    ostringstream << _coef[i] << " x^" << p - i << " + ";
  }
  ostringstream << _coef[p - 1];
  return ostringstream.str();
}


/*! Operator << to print polynomial.
 * \param strm ostream to print polynomial to.
 * \param p The polynomial to print to strm
 * \return The strm with polynomial appended. */
std::ostream &operator<<(std::ostream &strm, const Polynomial &p) {
  strm << p.toString();
  return strm;
}

double Polynomial::evaluate(const double x) {
  std::map<double, double>::iterator it = _cache.find(x);
  if (it != _cache.end()) {
    std::cout << "Cache Hit!" << std::endl;
    return it->second;
  }

  double result = 0;
  double xp = 1;
  unsigned long n = _coef.size();
  for (int i = 0; i < n; i++) {
    result += _coef[i] * xp;
    xp *= x;
  }

  _cache[x] = result;
  return result;
}

int run_polynomial() {
  double my_coef[] = {5, 4, 3, 2, 1};

  std::vector<double> vec(my_coef, my_coef + sizeof(my_coef) / sizeof(double));
  {
    Polynomial poly(vec);
    std::cout << "The polynomial is: " << poly << std::endl;
    std::cout << poly.evaluate(0) << std::endl;
    std::cout << poly.evaluate(1) << std::endl;
    std::cout << poly.evaluate(0) << std::endl;
    std::cout << poly.evaluate(1) << std::endl;
    std::cout << poly.evaluate(2) << std::endl;
  }
  std::cout << "About to exit!" << std::endl;
  return 0;
}
