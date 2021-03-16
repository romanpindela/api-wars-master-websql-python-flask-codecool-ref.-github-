# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                server: routes handling
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from flask import Flask, render_template, redirect, request, jsonify
from modules import api, constants as c, data_controller as dc, utilities as util

app = Flask(__name__)
app.secret_key = '#I\'ll be back!:D'  # encrypt session variables


# ---------------------------------------------------- main route -----------------------------------------------------

@app.route('/')
def index():
    """ Shows starter page. """
    return redirect('/planets/1')


@app.route('/<subject>/<int:page_number>')
def subject_page(subject, page_number):
    """ Shows a page listing the data specified in the subject variable. """
    subject_data = dc.data_get(subject, page_number)
    button_data = dc.button_data_get(subject, subject_data)

    if subject == c.SUBJECT.PEOPLE:
        subject_data = dc.data_change_url_to_name(subject_data, c.KEY.People.HOMEWORLD)

    return render_template(
        'index.html',
        subjects_list=c.SUBJECT_ORDER,
        subject_name=subject,
        subject_data=subject_data,
        button_data=button_data,
        column_names=dc.column_names_get(subject),
        pages_number=util.pagination_number_get(subject),
        page_active=page_number
    )


# ------------------------------------------- api request & response routes -------------------------------------------

@app.route('/api', methods=['POST'])
def api_data():
    """ Receives and responds to the client's request. """
    response = api.data_get(request.get_json())
    return jsonify(response)


# ----------------------------------------------------- main code -----------------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
