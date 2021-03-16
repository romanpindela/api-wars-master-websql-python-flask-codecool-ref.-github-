# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                            controller: server logic control
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from modules import data_format as df, data_handler as dh, swapi, utilities as util


# ----------------------------------------------- main data controllers -----------------------------------------------

def data_get(subject: str, page_number: int) -> tuple:
    """ Collects the data of the subject. """
    def data_get_from_swapi(subject: str, page_number: int) -> dict:
        """ Gets the subject data from the external api. """
        row_data = swapi.get_data(f'{subject}/?page={page_number}')

        # error handling
        if 'detail' in row_data and row_data['detail'] == 'Not found':
            raise ValueError(f'Page {page_number} with list of the {subject} not found.')

        return row_data

    # ------------- data_get() -------------
    row_data = data_get_from_swapi(subject, page_number)
    data = dh.data_prepare(row_data['results'], column_names_get_necessary(subject))  # 'results' - the subject data
    data = df.data_format(subject, data)
    util.pagination_number_set(subject, row_data['count'])  # 'count' - the number of items in subject

    return tuple(data)


def data_change_url_to_name(subject_data: tuple, column_name: str) -> tuple:
    """ Changes names instead of urls in cell data (later displayed on the buttons). """
    return tuple(dh.change_url_to_name(list(subject_data), column_name))


# ---------------------------------------------- button data controllers ----------------------------------------------

def button_data_get(subject: str, subject_data: tuple) -> list:
    """ Returns the modal window data needed to handle client-side events. """
    return dh.button_data_get(subject_data, dh.columns_with_button_get(subject))


# ---------------------------------------------- column names controllers ---------------------------------------------

def column_names_get(subject: str) -> tuple:
    """ Returns column names. """
    column_names = dh.column_names_get(subject)
    column_names = df.column_names_format(column_names)
    column_names = dh.column_names_prepare(column_names)

    return column_names


def column_names_get_necessary(subject: str, modal_window: bool = False) -> tuple:
    """ Returns the necessary header names used in column names. """
    columns = dh.column_names_get(subject)
    if modal_window:
        columns = dh.column_names_for_modal_window(subject, columns)

    return columns
