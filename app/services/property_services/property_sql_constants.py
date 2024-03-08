PROPERTY_JOIN_QUERY = """SELECT p.id, p.address, p.city, p.price, p.description, s.name as status 
            FROM property p 
            INNER JOIN status_history sh ON p.id = sh.property_id
            INNER JOIN status s ON sh.status_id = s.id"""

EXCLUDE_PROPERY_STATUS = {
    "status": ["comprado", "comprando"]
}

PROPERTY_QUERY_FILTERS = {
    "city" : "p.city=%s",
    "status": "s.name=%s",
    "year_gte": "p.year>=%s",
    "year_lte": "p.year<=%s",
}

PROPERTY_FIELD_MAPPERS = {
    "city" : "p.city",
    "status": "s.name"
}
