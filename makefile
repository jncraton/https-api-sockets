all: test

test:
	python3 -m doctest getsentiment.py

test-server:
	curl -X POST -H "Content-Type:application/octet-stream" -d "I hate sandcastles" localhost:1212/sentiment
	curl -X POST -H "Content-Type:application/octet-stream" -d "I like you" localhost:1212/sentiment
	curl -X POST -H "Content-Type:application/octet-stream" -d "Pizza is tasty" localhost:1212/sentiment
	curl -X POST -H "Content-Type:application/octet-stream" -d "Cold weather is the worst" localhost:1212/sentiment

run:
	python3 getsentiment.py "I hate sandcastles."

clean:
	rm -rf __pycache__
