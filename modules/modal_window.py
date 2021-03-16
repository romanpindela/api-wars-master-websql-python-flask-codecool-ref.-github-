# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                         modal window: html code for injection
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from yattag import Doc


def html_table_prepare(data: tuple, headers: tuple) -> str:
    """ Returns a string that contains html code with data. """
    doc, tag, text = Doc().tagtext()

    with tag('table', klass="table table-sm table-responsive-lg table-bordered table-striped"):
        # Header names.
        with tag('thead', klass="table-dark"):
            with tag('tr'):
                for column_name in headers:
                    with tag('th'):
                        text(column_name)
        # Subject data
        with tag('tbody'):
            for record in data:
                with tag('tr'):
                    for cell_data in record.values():
                        with tag('td'):
                            text(str(cell_data))

    return doc.getvalue()
