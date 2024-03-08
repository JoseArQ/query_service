from services.property_services.property_services import get_property

from .router import ServiceRouter

service_routes = ServiceRouter()

service_routes.add_route(route='api/properties', handler=get_property)