(defun calc (n)
   (loop for i from 1 below n 
         when (or (= (mod i 3) 0) (= (mod i 5) 0)) 
         sum i))

(defun mathy (n)
   (let* ((num-mult (lambda (b) (floor (/ (- n 1) b))))
          (mult-sum (lambda (b) (* (/ b 2) 
                                   (+ (expt (funcall num-mult b) 2) 
                                      (funcall num-mult b))))))
      (- (+ (funcall mult-sum 3) (funcall mult-sum 5)) (funcall mult-sum 15))))

(defun main ()
   (princ (mathy 1000)))
