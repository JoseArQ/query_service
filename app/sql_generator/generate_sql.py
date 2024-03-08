from typing import List, Tuple, Dict


def generate_query(
        query_base: str, 
        queries : dict, 
        query_filter_mappers : dict,
        model_fields : dict,
        exclude_filters : dict = {},
        ) -> Tuple[str, List[str]]:
    """Generate a query string based on the provided base query, filters, and model fields.

    Args:
        query_base (str): The base query string.
        queries (dict): A dictionary containing query filters.
        query_filter_mappers (dict): A dictionary mapping query filters to corresponding model fields.
        model_fields (dict): A dictionary containing model fields.
        exclude_filters (dict, optional): A dictionary containing exclude filters. Defaults to {}.

    Returns:
        Tuple[str, List]: A tuple containing the generated query string and a list of parameters.
    """
    try:
        query_filters, query_parameters = get_filter_query(queries=queries, query_filter_mappers=query_filter_mappers)
        exclude_queries, exclude_values = generate_exclude_query(
            exclude_filters=exclude_filters,
            model_fields=model_fields
            )
        
    
        if exclude_queries:
            query_filters = join_filters(filters=[query_filters, exclude_queries])
            query_parameters.extend(exclude_values)

    
        full_query =  add_filter(query=query_base, filter=query_filters)

        return full_query , query_parameters
    except Exception as e:
        tb = e.__traceback__
        error_message = f"""File {tb.tb_frame.f_code.co_filename} line {tb.tb_lineno} in {tb.tb_frame.f_code.co_name}"""
        print(error_message)

def generate_exclude_query(exclude_filters : Dict[str, List], model_fields : Dict[str, str]) -> Tuple[str, List]:
    """
    Generate exclude queries based on the provided exclude filters and model fields.

    Args:
        exclude_filters (dict): A dictionary containing exclude filters.
        model_fields (dict): A dictionary containing model fields.

    Returns:
        Tuple[str, List]: A tuple containing the generated exclude query string and a list of values.
    """
    exclude_queries = []
    exclude_values = []
    for field, values in exclude_filters.items():
        field_q = model_fields.get(field, None)
        if field_q:
            placeholders = ', '.join(['%s'] * len(values))
            exclude_queries.append(
                f"{field_q} NOT IN ({placeholders})"
            )
            exclude_values.extend(values)

    return " ".join(exclude_queries), exclude_values

def get_filter_query(queries : Dict[str, str], query_filter_mappers : Dict[str, str]) -> Tuple[str, List]:
    """
    Generate filter queries based on the provided queries and query filter mappers.

    Args:
        queries (dict): A dictionary containing queries.
        query_filter_mappers (dict): A dictionary mapping queries to corresponding filter mappers.

    Returns:
        Tuple[str, List]: A tuple containing the generated filter query string and a list of parameters.
    """

    parameters = []
    prop_filters = []
    for param, value in queries.items():
        
        query_filter = query_filter_mappers.get(param, None)
        if query_filter:
            prop_filters.append(query_filter)
            parameters.append(value)

    return join_filters(filters=prop_filters), parameters

### AUX FUNCTION
def add_filter(*, query : str, filter: str) -> str:
    """Add SQL condition using WHERE. If query not have filter return query input"""
    return f"{query} WHERE {filter}" if filter else query

def join_filters(*, filters : List[str]):
    """Joining filter fields with AND"""
    return " AND ".join(filters)
  
def join_filter(*, query : str, filter : str) -> str:
    """Add filter to existing query"""
    return " ".join([query, "AND", filter])