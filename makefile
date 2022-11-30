all: test

test:
	python3 -m doctest getsentiment.py

test-server:
	curl -X POST -H "Content-Type:application/octet-stream" -d "I hate sandcastles" localhost:1212
	curl -X POST -H "Content-Type:application/octet-stream" -d "I like you" localhost:1212

run:
	python3 getsentiment.py "I hate sandcastles."