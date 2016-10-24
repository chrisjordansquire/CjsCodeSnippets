(def argv *command-line-args*)

(defn modTest [x,y] 
  (= 0 (mod x y)))

(defn modTest35 [x]
  (or (modTest x 3) (modTest x 5)))

(if (= 0 (count argv))
  (def upper 1000)
  (def upper (Integer. (first argv))))

(println 
  (reduce + (filter modTest35 (range upper))))
