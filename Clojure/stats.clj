 (ns stats)

; A few statistics-related functions for fun.

(defn poisson-sample
 "Sample from Poisson with input rate"
 [rate]
 (let [rand-stream (repeatedly rand)
       stopping-condition #(when (> (Math/exp (- rate)) %2) %1)]
  (- (first (keep-indexed stopping-condition
                       (reductions * 1.0 rand-stream))))
  1))

(defn exponential-sample
  "Sample from Exponential distribution with given rate"
  [rate]
  (/ (- (Math/log (- 1 (rand)))) rate))

(defn mean
  [coll]
  (/ (reduce + coll) (count coll)))

(defn variance
  [coll]
  (- (mean (map #(Math/pow % 2) coll))
     (Math/pow (mean coll) 2)))

; Starting function to create an M/M/1 queue

(defrecord QueueTimes [arrival-times service-times])
(defn create-queue
  [samples arrival-rate service-rate]
  (QueueTimes. (repeatedly samples #(exponential-sample arrival-rate))
               (repeatedly samples #(exponential-sample service-rate))))

(defn queue-starting-times
  [arrival-times
   service-times]
  (if (< (+ (first arrival-times) (first service-times))
         (second arrival-times))
    (cons (first arrival-times) (queue-starting-times (next arrival-times)
                                                      (next service-times)))
    (cons (

(defn arrivals-at-t
  [arrival-times t]
  (first (keep-indexed #(if (< %2 t) %1)
                       (reductions + arrival-times))))

