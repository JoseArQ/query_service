from services.property_services.property_services import get_properties

from .router import ServiceRouter

service_routes = ServiceRouter()

service_routes.add_route(route='api/properties', handler=get_properties)