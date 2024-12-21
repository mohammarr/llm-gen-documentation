(ns math.utils)

(comment
  "Utility functions for working with numbers.")

(defn greet [name]
  (str "Hello, " name "!"))

(defn circle-area [radius]
  (let [pi 3.14159
        area (* pi radius radius)]
    area))

(defn is-positive? [num]
  (if (> num 0)
    "Yes"
    "No"))

(defn classify-number [num]
  (cond
    (> num 0) "Positive"
    (< num 0) "Negative"
    :else    "Zero"))

(defn factorial [n]
  (if (= n 0)
    1
    (* n (factorial (dec n)))))