// --------------------------------------------------------------------------------------------------------------------
//                                                       API Wars
//                                               client: modals components
//                                                        v 1.0
// --------------------------------------------------------------------------------------------------------------------

import {c} from './constants.js'
import {utilities as util} from "./utilities.js";

const modalWindowContainer = {
    title: document.querySelector('.modal-title'),
    body: document.querySelector('.modal-body'),
    footer: document.querySelector('.modal-footer')
};


export let modalWindow = {
    show: function (modalWindowData) {
        // Displays the modal window with data.
        setData(modalWindowData);
        initCleanData();

        $('#modal-window').modal();
    }
}

function setData (modalWindowData) {
    // Sets the data in the html elements of modal window.
    modalWindowContainer.title.innerHTML = `${util.capitalize(modalWindowData[c.data.key.columnName])} of ${modalWindowData[c.data.key.recordName]}`;
    modalWindowContainer.body.innerHTML = modalWindowData[c.data.key.data];
    modalWindowContainer.footer.innerHTML = '<button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>';
}

function initCleanData () {
    // Adds the event listeners fired when close the modal window to cleans a html elements.
    $('#modal-window').on('hidden.bs.modal', function () {
        modalWindowContainer.title.innerHTML = ' ';
        modalWindowContainer.body.innerHTML = ' ';
        modalWindowContainer.footer.innerHTML = ' ';
    });
}