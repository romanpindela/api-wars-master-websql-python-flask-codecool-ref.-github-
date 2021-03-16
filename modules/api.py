# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                api: request & response
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------
#  Valid request pattern:
#       {
#           'api_wars':
#               {
#                   'swapi':
#                       {
#                           'request': [ < list of the url requests to the swapi api database >]
#                       },
#                   'modal window':
#                       {
#                           'subject': ' <the subject name string> '
#                       }
#               }
#       }
#
#  Valid response pattern:
#       {
#           'api_wars':
#               {
#                   'modal window':
#                       {
#                           'injection code': ' <html string with data for injection to modal window> '
#                       }
#               }
#       }
#
# ---------------------------------------------------------------------------------------------------------------------

from modules import\
    constants as c,\
    data_controller as dc,\
    data_format as df,\
    data_handler as dh,\
    modal_window as mw,\
    swapi


# API key names.
class _Key:
    HEADER = 'api_wars'
    INJECTION_CODE = 'injection code'
    MODAL_WINDOW = 'modal window'
    REQUEST = 'request'
    SUBJECT = 'subject'
    SWAPI = 'swapi'


KEY = _Key()


# -------------------------------------------------- api controller ---------------------------------------------------

def data_get(request_data: dict) -> dict:
    """ Prepares data at the client's request. """
    if not request_data:
        return {'valueError': 'None request data.'}
    if KEY.HEADER not in request_data:
        return {'valueError': 'Wrong request data.'}

    subject = _subject_get_proper(request_data[KEY.HEADER][KEY.MODAL_WINDOW][KEY.SUBJECT])
    swapi_response = _data_get(request_data[KEY.HEADER][KEY.SWAPI][KEY.REQUEST])
    data_prepared = _data_prepare(subject, swapi_response)
    column_names_prepared = _column_names_prepare(data_prepared[0])  # only the first record

    return {
        KEY.HEADER: {
            KEY.MODAL_WINDOW: {
                KEY.INJECTION_CODE: mw.html_table_prepare(data_prepared, column_names_prepared)
            }
        }
    }


def _data_prepare(subject: str, row_data: list) -> tuple:
    """ Prepares the data for create html code. """
    headers_list = dc.column_names_get_necessary(subject, modal_window=True)
    prepared_data = dh.data_prepare(row_data, headers_list)
    prepared_data = df.data_format(subject, prepared_data)

    return tuple(prepared_data)


def _subject_get_proper(subject: str) -> str:
    """ Returns proper subject. """
    if subject in c.COLUMN_NAMES_WITH_PLANETS:
        subject = c.SUBJECT.PLANETS
    elif subject in c.COLUMN_NAMES_WITH_PEOPLE:
        subject = c.SUBJECT.PEOPLE

    return subject


# --------------------------------------------------- api handlers ----------------------------------------------------

def _data_get(request_data: list) -> list:
    """ Prepares data at the client's request. """
    response_data = []
    for url in request_data:
        response_data.append(swapi.get_data(url, full_url=True))

    return response_data


def _column_names_prepare(data_record: dict) -> tuple:
    """ Prepares column names. """
    column_names = []
    for key in data_record:
        column_names.append(key)

    return tuple(dh.column_names_prepare(column_names))
