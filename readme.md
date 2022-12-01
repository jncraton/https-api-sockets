HTTPS API Sockets
=================

This project connects to a very simple HTTPS API endpoint, sends a POST request, and displays the infromation from the response body.

Note that this project intentionally uses Python's socket interface and low-level response parsing. In a real-world application, you would likely use the `requests` library, or something else even higher-level, to interact with an HTTPS API. These libaries are much easier to use and provide much greater robustness and error handling. An example implementation of this program using `requests` is available in `requests-example.py`.

Assignment
----------

The code in `getsentiment.py` is incomplete. Fill in the missing sections (denoted using `TODO` comments) to complete the program. When you are finished, all tests should pass, and the program should be able to be run from a terminal as follows:

```sh
> python3 getsentiment.py I love sockets.
positive
```

The heavy lifting of determining whether an input text is positive or negative is managed by a server handling requests over HTTPS. The API endpoint is `https://joncraton.com/sentiment`. It accepts input text as an HTTP POST request body. It then responds with either the text `positive` or `negative` as an HTTP response body.

Testing
-------

You can run the tests as follows:

```sh
python3 -m doctest getsentiment.py
```

You may also use the `test` task in the include makefile.

Useful docs
-----------

- Python
    - [socket](https://docs.python.org/3/library/socket.html)
    - [ssl](https://docs.python.org/3/library/ssl.html)
- HTTP
    - [Request Messages](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#HTTP/1.1_request_messages)
    - [Response Messages](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#HTTP/1.1_response_messages)
    - [Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
