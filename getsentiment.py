import socket
import ssl
import sys
import re


def get_sentiment(text):
    """ 
    Returns the sentiment polarity for a given text

    >>> get_sentiment("I hate sandcastles.")
    -0.8
    """
    response = get_api_response(text)

    # Grab the HTTP response body
    # It is separated from the headers by a pair of newlines
    body = response.split("\r\n\r\n")[1]

    # Tokenize the JSON string
    # Normally we'd use json.loads or similar here. I've chosen to code a very crude
    # parser to demonstrate what happens under the hood
    tokens = re.split(r'[{}":\[\],\n]+', body)

    for i, token in enumerate(tokens):
        # When we find the token we're interested in (polarity) we return its value
        if token == "<insert token value here>":
            return float(tokens[i + 1])


def get_api_response(text):
    """
    Performs HTTP request to sentiment API and returns response body
    """

    host = "sentim-api.herokuapp.com"

    # Create a new default SSLContext for the connection
    ssl_context = ssl.<method to create default SSLContext>

    # Create a TCP socket
    with socket.socket(<appropriate parameters to create IPv4 TCP socket>) as sock:
        # Connect on port 443
        sock.<method to create connection on port 443>

        # Wrap the TCP connection in our SSLContext
        with ssl_context.wrap_socket(sock, server_hostname=host) as ssock:
            # Build HTTP request to send
            request = build_api_request(text).encode()

            # Send the entire request to the API server
            ssock.<method to send request>

            # Recieve up to 1024 response bytes and decode to string
            data = ssock.<method to recieve 1024 bytes of data from socket>

            return data.decode()


def build_api_request(text, host="sentim-api.herokuapp.com", path="/api/v1/"):
    """ 
    Builds an HTTP POST API request

    >>> build_api_request("").split("Content-Length:")[1][:2]
    '11'

    >>> build_api_request("test").split("Content-Length:")[1][:2]
    '15'
    """

    # Create POST request body
    body = '{"text":"' + text + '"}'

    return (
        f"POST {path} HTTP/1.1\r\n"
        # Add needed HTTP headers
        f"Host:{host}\r\n"
        f"Accept: application/json\r\n"
        f"Content-Type:application/json\r\n"
        # Set the content length to the length of our body content
        f"Content-Length:{<expression for the length of the body>}\r\n"
        # Append the request body terminated with two newlines
        f"\r\n{<expression for the request body>}\r\n\r\n"
    )


if __name__ == "__main__":
    print(get_sentiment(" ".join(sys.argv[1:])))
