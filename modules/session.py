# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                    session handler
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from flask import session


# -------------------------------------------------- page pagination --------------------------------------------------

def pagination_number_set(page_name: str, pagination_number: int):
    """ Sets the pagination number. """
    session[f'pagination_{page_name}'] = pagination_number


def pagination_number_get(page_name: str) -> int:
    """ Gets the pagination number. """
    return session[f'pagination_{page_name}']
