(def argv *command-line-args*)
(def integers (iterate inc 1))

(if (= 0 (count argv))
  (def upper 4e6)
  (def upper (Integer. (first argv)))
)

(def fib (memoize (fn [x] (if (< x 2) x (+ (fib (- x 1)) (fib (- x 2)))))))

(def fib_num (filter even? (map fib integers)))
(def out (reduce + (take-while 
                    (fn [x] (< x upper)) fib_num)))

(println out)


