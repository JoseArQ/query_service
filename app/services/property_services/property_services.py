
from database.db import connect
from configs.config import DB_CONFIG
from models.utils import dataclass_to_dict
from models.property import Property
from sql_generator.generate_sql import generate_query

from .property_sql_constants import (
    PROPERTY_JOIN_QUERY, 
    PROPERTY_QUERY_FILTERS, 
    PROPERTY_FIELD_MAPPERS, 
    EXCLUDE_PROPERY_STATUS
    )


def get_properties(query_params : dict):
    
    query, parameters = generate_query(
        query_base=PROPERTY_JOIN_QUERY,
        queries=query_params,
        query_filter_mappers=PROPERTY_QUERY_FILTERS,
        model_fields=PROPERTY_FIELD_MAPPERS,
        exclude_filters=EXCLUDE_PROPERY_STATUS
    )

    try:
        with connect(data_connection=DB_CONFIG) as cursor:
            # print("running query: ", query, parameters)
            cursor.execute(query, parameters) 
            props = cursor.fetchall()
            if props is None:
                raise ValueError('property with does not exists')
            
            properties = [Property(*p) for p in props]
            data = [dataclass_to_dict(p, exclude_fields=["id"]) for p in properties]
            
            return data
    except ValueError as e:
        tb = e.__traceback__
        error_message = f"""File {tb.tb_frame.f_code.co_filename} line {tb.tb_lineno} in {tb.tb_frame.f_code.co_name}"""
        print(error_message)
    