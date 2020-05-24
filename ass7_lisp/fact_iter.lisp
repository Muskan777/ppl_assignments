(setf c 1)
(defun fact (n)
	(loop for i from 1 to n
		do
			(setf c 
				(* c i)
			)
	)
	(setf n c)
)
(setq n (read))
(write 
	(fact n)
)

