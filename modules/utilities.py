# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                      utilities
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from modules import session, swapi


# -------------------------------------------------- page pagination --------------------------------------------------

def pagination_number_get(page_name: str) -> int:
    """ Gets the pagination number from variable in session. """
    return session.pagination_number_get(page_name)


def pagination_number_set(page_name: str, items_number: int):
    """
        Calculates the number of pages of pagination.
        The result is rounded up from the formula: (numerator + denominator - 1) // denominator
        Next, sets the number of subpages (pagination of the page) and remembers it as variable in the sessions.
    """
    pagination_number = (items_number + swapi.PAGINATION_NUMBER - 1) // swapi.PAGINATION_NUMBER
    session.pagination_number_set(page_name, pagination_number)


# ------------------------------------------------- other untilities --------------------------------------------------

def change_list_value(array: list, value_old: str, value_new: str) -> list:
    """ Returns a given list with a changed value. """
    for index, value in enumerate(array):
        if value == value_old:
            array[index] = value_new

    return array


def unpack_data(data_list: list) -> str:
    """ Returns a string concatenated with the list data. """
    return ', '.join(data_list)
