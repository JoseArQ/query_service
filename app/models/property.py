from typing import Optional
from dataclasses import dataclass


@dataclass
class Property:
    """DAO for read properties with status"""
    
    id : Optional[int] 
    address : str
    city : str
    price : int
    description : str
    status : str

    def __post_init__(self):
        if not self.address.strip():
            raise ValueError('Address cannot be empty')

        if self.price <= 0:
            raise ValueError('Price must be positive')
