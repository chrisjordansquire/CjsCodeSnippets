(def argv *command-line-args*)
(def integers (iterate inc 1))

(if (= 0 (count argv))
  (def in 2)
  (def in (Integer. (first argv))))

(defn palindrome [in]
  (loop [x in y 0]
    (if (zero? x)
      y
      (recur (/ (- x (mod x 10)) 10) (+ (* 10 y) (mod x 10))))))

(defn is-palindrome? [x] (= (palindrome x) x))

(def upper (Math/pow 10 in))

(def pseq (for [i (range 1 upper)
                j (range 1 i)
                :let [prod (* i j)]
                :when (is-palindrome? prod)] prod))

(println (apply max pseq))
