import socket
import ssl
import sys
import re


def build_api_request(body, host="joncraton.com", path="/sentiment"):
    """
    Builds the text of an HTTP POST request

    Here is a high-level description of an HTTP request:

    https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#HTTP/1.1_request_messages

    >>> build_api_request("test").splitlines()[0]
    'POST /sentiment HTTP/1.1'

    >>> build_api_request("test", path='/index.html').splitlines()[0]
    'POST /index.html HTTP/1.1'

    >>> build_api_request("test").split("Host:")[1].strip()[:13]
    'joncraton.com'

    >>> build_api_request("test", host='example.com').split("Host:")[1].strip()[:11]
    'example.com'

    >>> build_api_request("").split("Content-Length:")[1].strip()[:1]
    '0'

    >>> build_api_request("test").split("Content-Length:")[1].strip()[:1]
    '4'

    >>> build_api_request("test body")[-13:-4]
    'test body'

    >>> build_api_request("test body")[-4:]
    '\\r\\n\\r\\n'
    """

    return (
        # Send request line
        # TODO: Set the path properly
        f"POST /hardcoded-path HTTP/1.1\r\n"
        # Add host HTTP header using `host` variable
        f"Host:\r\n"
        # TODO: Set the content length to the length of our body content
        f"Content-Length:\r\n"
        # TODO: Append the request body terminated by two newlines
        f"\r\nBody\r\n\r\n"
    )


def get_response_body(response):
    """
    Returns just the body of a successful HTTP response

    The response will look something like this:

        HTTP/1.1 200 OK
        Content-Length: 5

        Hello

    The response body in this case is "hello"

    Here is a high-level description of response messages:

    https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#HTTP/1.1_response_messages

    >>> get_response_body(b'HTTP/1.1 200 OK\\r\\n\\r\\n')
    ''
    
    >>> get_response_body(b'HTTP/1.1 200 OK\\r\\n\\r\\nbody')
    'body'

    >>> get_response_body(b'HTTP/1.1 200 OK\\r\\n\\r\\nnegative')
    'negative'

    >>> get_response_body(b'HTTP/1.1 200 OK\\r\\nheader\\r\\n\\r\\nbody')
    'body'

    >>> get_response_body(b'HTTP/1.1 500 OK\\r\\n\\r\\nerror')
    Traceback (most recent call last):
    ...
    Exception: HTTP request failed: 500
    """

    status = response[9:12].decode()

    # Raise an exception if the request was unsuccessful
    if status != "200":
        raise Exception(f"HTTP request failed: {status}")

    # TODO: Split body from the response
    # It is separated from the headers by a pair of newlines
    body = response.decode()

    return body


def get_sentiment(text):
    """
    Performs HTTP request to sentiment API and returns response body

    A connection is established by wrapping a TCP socket in an SSL context


    The SSL module provides documentation and examples for this process:
    https://docs.python.org/3/library/ssl.html

    >>> get_sentiment("I hate sandcastles")
    'negative'

    >>> get_sentiment("I like movies")
    'positive'
    """

    host = "joncraton.com"

    # TODO: Create a new default SSLContext for the connection
    ssl_context = None

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # TODO: Connect to `host` on port 443
        

        # TODO: Properly wrap the TCP socket in our SSLContext
        with ssl_context.wrap_socket() as ssock:
            # TODO: Properly build HTTP request to send
            req = text

            # Send the entire request to the API server
            ssock.sendall(req.encode())

            # Receive initial HTTP data
            res = ssock.recv(1024)

            # Receive all HTTP data
            expected_length = int(re.findall(rb"content-length:\s*(\d+)", res, flags=re.I)[-1])
            get_body_length = lambda r: len(r) - r.index(b"\r\n\r\n") - 4

            while get_body_length(res) < expected_length:
                res += ssock.recv(1024)

            # TODO: Return only the response body from `res`
            return res


if __name__ == "__main__":
    print(get_sentiment(" ".join(sys.argv[1:])))
