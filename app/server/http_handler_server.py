import json
from typing import Dict, Any
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from router.routes import service_routes
from configs.logger import get_stream_logger

logger = get_stream_logger(name=__name__)

class RestRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """
        Handle HTTP GET method.

        Retrieves the relative path and query parameters from the request,
        calls the appropriate handler function based on the path,
        and sends a response with the result.

        Returns:
            None
        """

        relative_path = self._get_path()
        query_params = self._get_params()
       
        try:
            handler_resp = service_routes.get_handler(route=relative_path, query_params=query_params)
            if "error" in handler_resp:
                self.response(data=handler_resp["error"], status_code=404)
            
            self.response(data=handler_resp["data"], status_code=200)
        except Exception as e:
            logger.error(str(e))
            self.response(data=str(e), status_code=403)
            
    def _get_path(self) -> str:
        """
        Extract the path component from the request URL.

        Returns:
            str: The path component of the URL.
        """
        url_parsed = urlparse(url=self.path)
        return url_parsed.path
    
    def _get_params(self) -> Dict[str, Any]:
        """
        Extract the query parameters from the request URL.

        Returns:
            dict: A dictionary containing the query parameters.
        """
        url_parsed = urlparse(url=self.path)
        query_params = parse_qs(url_parsed.query)

        return {
            param : value[0]  for param, value in query_params.items()
            }
    
    def response(self, data=None, status_code=None):
        """
        Send an HTTP response with the provided data and status code.

        Args:
            data (Any, optional): The data to include in the response body. Defaults to None.
            status_code (int, optional): The HTTP status code to include in the response. Defaults to None.

        Returns:
            int: The number of bytes written to the response body.
        """

        if not status_code:
            status_code = ''
        
        if not data:
            data = ''

        self.send_response(status_code)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","*")
        self.send_header("Access-Control-Allow-Headers","*")
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        response = {
            "data": data
        }

        return self.wfile.write(json.dumps(response).encode())
    
