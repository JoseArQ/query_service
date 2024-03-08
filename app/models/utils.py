from dataclasses import asdict, fields

def dataclass_to_dict(dataclass_instance, exclude_fields=None):
    """
    Convert a dataclass instance to a Python dictionary, excluding specified fields.

    Args:
        dataclass_instance: An instance of a dataclass.
        exclude_fields (list, optional): A list of field names to exclude from the resulting dictionary. Defaults to None.

    Returns:
        dict: A dictionary representation of the dataclass instance with specified fields excluded.
    """
    if exclude_fields is None:
        exclude_fields = []

    dataclass_dict = asdict(dataclass_instance)
    return {field_name: dataclass_dict[field_name] for field_name in dataclass_dict if field_name not in exclude_fields}

