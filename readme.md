step 1: build the container image

	docker build -t pykata .
	

step 2: run the container image
	
	docker run --rm -it -v ${PWD}:/app pykata:latest /bin/sh
	
	
step 3: funny one; write some code


step 4: test your code!
	
	pytest
	
And btw, remember to leave it cleaner than you found it. Use docker stop !!
