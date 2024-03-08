from typing import Dict, Any

class ServiceRouter:
    _routes = {}

    def __init__(self, base_path : str = '') -> None:
        
        if not base_path:
            base_path = '/'
        
        self.base_path = base_path
    
    def add_route(self, route : str, handler : object) -> None:
        """
        Add a route and its corresponding handler to the server.

        Args:
            route (str): The route to be added.
            handler (object): The handler object associated with the route.

        Returns:
            None
        """
        full_path = self.base_path + route
        self._routes[full_path] = handler
    
    def get_handler(self, route : str, query_params : Dict[str, Any]) -> Dict[str, Any]:
        """
        Get the handler for a specified route and call it with the provided query parameters.

        Args:
            route (str): The route for which to retrieve the handler.
            query_params (dict): A dictionary containing query parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the result of calling the handler or an error message if the route is not found or an exception occurs.
        """
        try:
            handler = self._routes.get(route, None)
            if not handler:
                raise Exception(f"{route} route not found")
            
            return {
                "data" : handler(query_params=query_params)
            }
        
        except Exception as e:
            tb = e.__traceback__
            error_message = f"""File {tb.tb_frame.f_code.co_filename} line {tb.tb_lineno} in {tb.tb_frame.f_code.co_name}"""
            print(error_message)
            return {
                "error": error_message
                }
