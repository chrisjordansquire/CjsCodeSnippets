(def argv *command-line-args*)
(def integers (iterate inc 1))

(if (= 0 (count argv))
  (def number 50)
  (def number (Integer. (first argv))))

(defn max-pfac [x]
  (loop [n x
         i 2
         max_fac 1]
    (if (zero? (- n 1)) 
      max_fac
      (if (zero? (mod n i))
        (recur (/ n i) i i)
        (recur n (inc i) max_fac)))))

(println (max-pfac number))
