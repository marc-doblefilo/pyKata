step 1: build the container image ->

	docker build -t pykata .

step 2: run the container image ->

	
	docker run --rm -it -v ${PWD}:/app pykata:latest /bin/sh
