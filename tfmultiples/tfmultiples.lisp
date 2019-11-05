(defun brute (n)
   (loop for i from 1 below n 
         when (or (= (mod i 3) 0) (= (mod i 5) 0)) 
         sum i))

(defun mathy (n)
   (labels ((num-mult (b) 
               (floor (/ (- n 1) b)))
            (mult-sum (b)
               (* (/ b 2)
                  (+ (expt (num-mult b) 2) 
                     (num-mult b)))))
      (- (+ (mult-sum 3) (mult-sum 5)) (mult-sum 15))))

(defun main (args)
   (princ (mathy 1000)))
