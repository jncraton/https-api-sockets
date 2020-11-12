all: test

test:
	python3 -m doctest getsentiment.py

run:
	python3 getsentiment.py "I hate sandcastles."