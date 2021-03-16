# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                       data format:  formatting data in tables
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import locale
from modules import constants as c, utilities as util


# ---------------------------------------------- formatting controllers -----------------------------------------------

def data_format(subject: str, data: list) -> list:
    """ Returns formatted the subject data. """
    locale.setlocale(locale.LC_ALL, '')

    for item in data:
        if subject == c.SUBJECT.PLANETS:
            item[c.KEY.PLANETS.DIAMETER] = _format_diameter(item[c.KEY.PLANETS.DIAMETER])
            item[c.KEY.PLANETS.WATER] = _format_water(item[c.KEY.PLANETS.WATER])
            item[c.KEY.PLANETS.POPULATION] = _format_population(item[c.KEY.PLANETS.POPULATION])
            item[c.KEY.PLANETS.ROTATION] = _format_rotation(item[c.KEY.PLANETS.ROTATION])
            item[c.KEY.PLANETS.ORBITAL] = _format_orbital(item[c.KEY.PLANETS.ORBITAL])
        elif subject == c.SUBJECT.STARSHIPS:
            item[c.KEY.STARSHIPS.CREW] = _format_crew_and_passengers(item[c.KEY.STARSHIPS.CREW])
            item[c.KEY.STARSHIPS.PASSENGERS] = _format_crew_and_passengers(item[c.KEY.STARSHIPS.PASSENGERS])
            item[c.KEY.STARSHIPS.CARGO] = _format_cargo(item[c.KEY.STARSHIPS.CARGO])
            item[c.KEY.STARSHIPS.LENGTH] = _format_length(item[c.KEY.STARSHIPS.LENGTH])
            item[c.KEY.STARSHIPS.ATSP] = _format_atsp(item[c.KEY.STARSHIPS.ATSP])
            item[c.KEY.STARSHIPS.MGLT] = _format_mglt(item[c.KEY.STARSHIPS.MGLT])
        elif subject == c.SUBJECT.VEHICLES:
            item[c.KEY.VEHICLES.CREW] = _format_crew_and_passengers(item[c.KEY.VEHICLES.CREW])
            item[c.KEY.VEHICLES.PASSENGERS] = _format_crew_and_passengers(item[c.KEY.VEHICLES.PASSENGERS])
            item[c.KEY.VEHICLES.CARGO] = _format_cargo(item[c.KEY.VEHICLES.CARGO])
            item[c.KEY.VEHICLES.LENGTH] = _format_length(item[c.KEY.VEHICLES.LENGTH])
            item[c.KEY.VEHICLES.ATSP] = _format_atsp(item[c.KEY.VEHICLES.ATSP])
        elif subject == c.SUBJECT.PEOPLE:
            item[c.KEY.PEOPLE.HEIGHT] = _format_height(item[c.KEY.PEOPLE.HEIGHT])
            item[c.KEY.PEOPLE.MASS] = _format_mass(item[c.KEY.PEOPLE.MASS])
            if c.KEY.PEOPLE.HOMEWORLD in item:
                item[c.KEY.PEOPLE.HOMEWORLD] = _format_homeworld(item[c.KEY.PEOPLE.HOMEWORLD])
    return data


# ----------------------------------------- formatting of individual columns ------------------------------------------

def _format_atsp(data: str) -> str:
    data = _prepare_integer(data)
    return '{:n} km/h'.format(float(data)) if _valid_number(data) else data


def _format_cargo(data: str) -> str:
    data = _prepare_integer(data)
    return '{:n} kg'.format(int(data)) if _valid_number(data) else data


def _format_crew_and_passengers(data: str) -> str:
    data = _prepare_integer(data)

    if data == '0':
        return 'not carry'
    if data == '1':
        return f'{data} person'
    if _data_range(data):
        return f'{data} people'

    return '{:n} people'.format(int(data)) if _valid_number(data) else data


def _format_diameter(data: str) -> str:
    data = _prepare_integer(data)
    if data == '0':
        return c.FORMAT_NAME.UNKNOWN

    return '{:n} km'.format(int(data)) if _valid_number(data) else data


def _format_height(data: str) -> str:
    data = _prepare_integer(data)
    height = int(data) / 100  # convert cm -> m
    return '{:n} m'.format(height) if _valid_number(data) else data


def _format_homeworld(data: str) -> list:
    return [data]  # list needed for later data processing


def _format_length(data: str) -> str:
    data = _prepare_float(data)
    return '{:n} m'.format(float(data)) if _valid_number(data) else data


def _format_mass(data: str) -> str:
    data = _prepare_float(data)
    return '{:n} kg'.format(float(data)) if _valid_number(data) else data


def _format_mglt(data: str) -> str:
    data = _prepare_integer(data)
    return '{:n} mglt/h'.format(float(data)) if _valid_number(data) else data


def _format_orbital(data: str) -> str:
    data = _prepare_integer(data)
    if data == '0':
        return c.FORMAT_NAME.UNKNOWN

    return '{:n} days'.format(int(data)) if _valid_number(data) else data


def _format_population(data: str) -> str:
    data = _prepare_integer(data)
    return '{:n} people'.format(int(data)) if _valid_number(data) else data


def _format_rotation(data: str) -> str:
    data = _prepare_integer(data)
    if data == '0':
        return c.FORMAT_NAME.UNKNOWN

    return '{:n} hours'.format(int(data)) if _valid_number(data) else data


def _format_water(data: str) -> str:
    if data == '0':
        return c.FORMAT_NAME.NO_WATER

    return '{:n}%'.format(float(data)) if _valid_number(data) else data


# ------------------------------------------- internal formatting functions -------------------------------------------

def _data_range(data: str) -> bool:
    """ Checks if a string data are a numbers in range. """
    return True if data.find('-') != -1 else False


def _prepare_integer(data: str) -> str:
    """ Removes unnecessary characters from the string representing an integer """
    return data.replace(",", "")  # for numbers with the thousand separator


def _prepare_float(data: str) -> str:
    """ Removes unnecessary characters from the string representing an integer """
    return data.replace(",", ".")  # for numbers with coma ","


def _valid_number(data: str) -> bool:
    """ Checks if a data is valid integer or float number. """
    try:
        if data.isdigit():
            return isinstance(int(data), int)
        else:
            return isinstance(float(data), float)
    except ValueError:
        return False


# ------------------------------------------------- other formatting --------------------------------------------------

def column_names_format(column_names: tuple) -> tuple:
    """ Return a renamed column name if necessary. """
    MGlT = c.KEY.STARSHIPS.MGLT
    if MGlT in column_names:
        column_names = tuple(util.change_list_value(list(column_names), MGlT, c.COLUMN_NEW_NAME.MGLT))

    return column_names
