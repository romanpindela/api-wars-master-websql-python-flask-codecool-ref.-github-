# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                     data handler: data processing and preparation
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from modules import constants as c, swapi, utilities as util


# ------------------------------------------------ main data handlers -------------------------------------------------


def data_prepare(raw_data: list, headers_list: tuple) -> list:
    """ Returns only the necessary data for a given subject. """
    prepared_data = []
    for raw_item in raw_data:
        prepared_item = {}
        for key in headers_list:
            prepared_item[key] = raw_item[key]
        prepared_data.append(prepared_item)

    return prepared_data


def change_url_to_name(subject_data: list, column_name: str) -> list:
    """ Changes names instead of urls in cell data. """
    for record in subject_data:
        url = "".join(record[column_name])
        record[column_name] = swapi.get_data_name(url, full_url=True)

    return subject_data


# ----------------------------------------------- button data handlers ------------------------------------------------

def button_data_get(subject_data: tuple, column_names: tuple) -> list:
    """ Returns the modal window data needed to handle client-side events. """
    record_data = []
    for record in subject_data:
        button_data = {}
        for column_name in column_names:
            data = record[column_name]
            button_data[column_name] = {
                'amount of data': len(data),
                'data': util.unpack_data(data)
            }
        record_data.append(button_data)

    return record_data


def columns_with_button_get(subject: str) -> tuple:
    """ Returns the names of data for the corresponding column for button insertion. """
    if subject == c.SUBJECT.PLANETS:
        return c.COLUMN_WITH_BUTTON.PLANETS
    elif subject == c.SUBJECT.STARSHIPS:
        return c.COLUMN_WITH_BUTTON.STARSHIPS
    elif subject == c.SUBJECT.VEHICLES:
        return c.COLUMN_WITH_BUTTON.VEHICLES
    elif subject == c.SUBJECT.PEOPLE:
        return c.COLUMN_WITH_BUTTON.PEOPLE
    else:
        raise ValueError(f'There are no column names for the button data in the {subject} subject.')


# ----------------------------------------------- column names handlers -----------------------------------------------

def column_names_get(subject: str) -> tuple:
    """ Returns column names. """
    if subject == c.SUBJECT.PLANETS:
        return c.HEADERS.PLANETS
    elif subject == c.SUBJECT.STARSHIPS:
        return c.HEADERS.STARSHIPS
    elif subject == c.SUBJECT.VEHICLES:
        return c.HEADERS.VEHICLES
    elif subject == c.SUBJECT.PEOPLE:
        return c.HEADERS.PEOPLE
    else:
        raise ValueError(f'There are no column names for the {subject} subject.')


def column_names_for_modal_window(subject_name: str, column_names: tuple) -> tuple:
    """ Gets column names for modal window (removes column names that contain buttons). """
    if subject_name == c.SUBJECT.PLANETS:
        columns_with_button = c.COLUMN_WITH_BUTTON.PLANETS
    elif subject_name == c.SUBJECT.STARSHIPS:
        columns_with_button = c.COLUMN_WITH_BUTTON.STARSHIPS
    elif subject_name == c.SUBJECT.VEHICLES:
        columns_with_button = c.COLUMN_WITH_BUTTON.VEHICLES
    elif subject_name == c.SUBJECT.PEOPLE:
        columns_with_button = c.COLUMN_WITH_BUTTON.PEOPLE
    else:
        raise ValueError(f'The columns that contain buttons for {subject_name} not found.')

    column_names = list(column_names)
    for column_to_remove in columns_with_button:
        column_names.remove(column_to_remove)

    return tuple(column_names)


def column_names_prepare(raw_names) -> tuple:
    """
        Returns the tuple of column names, where:
            * character '_' is replaced with a space ' ';
            * the first letter in a word is capitalized.
    """
    return tuple([name.replace('_', ' ').capitalize() for name in raw_names])
