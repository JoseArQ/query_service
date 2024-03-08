import logging
from http.server import HTTPServer

from configs.config import SERVER_PORT, SERVER_HOST
from .http_handler_server import RestRequestHandler

def run_server(
        server_class=HTTPServer, 
        handler_class=RestRequestHandler,
        port=SERVER_PORT,
        host=SERVER_HOST
        ):
    """
    Start the HTTP server with the specified handler class and listen for incoming requests.

    Args:
        server_class (class): The class representing the HTTP server. Defaults to HTTPServer.
        handler_class (class): The class representing the request handler. Defaults to RestRequestHandler.
        port (int): The port on which the server will listen for incoming requests. Defaults to SERVER_PORT.
        host (str): The host address on which the server will bind. Defaults to SERVER_HOST.

    Returns:
        None
    """
    logging.basicConfig(level=logging.INFO)
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    logging.info("starting server httpd...")
    try:
        logging.info(f"server on port: {port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("closing server httpd...")
    
    httpd.server_close()
    logging.info("stoped server httpd...")
        