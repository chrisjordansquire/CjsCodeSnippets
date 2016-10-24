(def argv *command-line-args*)

(if (= 0 (count argv))
  (def in 10001)
  (def in (Integer. (first argv))))

(def x (euler7/primesUpToNth in))

(println (last x))
