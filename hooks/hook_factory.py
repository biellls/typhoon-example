"""Used to extend the functionality of typhoon's built-in get_hook method

For every custom hook you create define a mapping in HOOK_MAPPINGS so it can be accessed by calling
typhoon.hooks.hook_factory.get_hook('custom_hook_id'). Typhoon will try to import the file from the builtin hooks
and if no mapping is found then it will try to load the module located at $TYPHOON_HOME/hooks/hooks_factory.py and
call its get_hook method."""
import logging

from typhoon.connections import get_connection_params
from typhoon.contrib.hooks.hook_interface import HookInterface

# Add mappings here
HOOK_MAPPINGS = {
    # eg: 'postgres_custom': MyPostgresHook,
}


def get_hook(conn_id: str) -> HookInterface:
    conn_params = get_connection_params(conn_id)
    try:
        hook_class = HOOK_MAPPINGS.get(conn_params.conn_type)
        return hook_class(conn_id)
    except KeyError:
        logging.error(f'Connection type {conn_params.conn_type} unrecognised. Not defined in hook mappings')
