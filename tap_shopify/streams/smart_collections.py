import shopify

from tap_shopify.streams.base import Stream
from tap_shopify.context import Context


class SmartCollections(Stream):
    name = 'smart_collections'
    replication_object = shopify.SmartCollection
    replication_key = 'updated_at'


Context.stream_objects['smart_collections'] = SmartCollections
