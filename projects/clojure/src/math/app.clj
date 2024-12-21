(ns math.app
  (:require
   [math.utils :as utils]))

(defn main
  "Main function for the application."
  [& args]
  (println (utils/greet "World"))
  (println (utils/circle-area 5))
  (println (utils/is-positive? -2))
  (println (utils/classify-number 0)))