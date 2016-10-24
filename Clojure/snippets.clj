; Collection of short snippets doing things I often wany to do

; in the below, s was a string w/ some financial data
(require '[clojure.string :as string])
(require '[clojure.pprint :as pprint])
(def numbers (map #(Float/parseFloat (string/replace % #"\$" ""))
                  (re-seq #"\$\d+\.\d\d" s)))
(defn round-to-n [n] 
  (fn [s] Float/parseFloat (format (string/join "%." (str n) "f"))))
(def reverse-sorted (reverse (sort numbers)))
(map vector
  reverse-sorted
  (map (round-to-n 2) (reductions + reverse-sorted))
  (map #((round-to-n 2) 
         (/ % (applreverse-sorted + reverse-sorted))) 
       (reductions + reverse-sorted)))
(pprint/pprint reverse-sorted)

;example creating Java 8 datetime
(import java.time.LocalDateTime 
        java.time.format.DateTimeFormatter)
(def dt-string "2015-10-30T15:24:55")
(def dt-formatter DateTimeFormatter/ISO_LOCAL_DATE_TIME)
(def dt (LocalDateTime/parse dt-string dt-formatter))

;print the methods of a java object
; http://stackoverflow.com/questions/5821286/how-can-i-get-the-methods-of-a-java-class-from-clojure
;Returns a set of clojure.reflect.Method types, which appears to be a record with
;fields including :return-type and :parameter-types
;Actually, the return set can also include Fields and Constructors
(require '[clojure.reflect :as r])
(defn object-dir 
  [obj]
  (:members (r/reflect obj)))

;get name of current namespace
;http://stackoverflow.com/questions/3763812/clojure-referring-to-the-name-of-the-namespace
(ns-name *ns*)

;functions in a namespace
;http://stackoverflow.com/questions/2747294/how-to-list-the-functions-of-a-namespace
(dir clojure.string)
