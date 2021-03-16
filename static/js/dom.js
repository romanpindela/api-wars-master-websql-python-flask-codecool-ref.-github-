// --------------------------------------------------------------------------------------------------------------------
//                                                       API Wars
//                                                     client: DOM
//                                                        v 1.0
// --------------------------------------------------------------------------------------------------------------------

import {c} from './constants.js'
import {dataHandler as dh} from "./data_handler.js";
import {modalWindow} from "./modals.js";
import {utilities as util} from "./utilities.js";


export let dom = {
    buttonData: {
        initEventListener: function () {
            // Inits event listeners for the button's data.
            const buttons = document.querySelectorAll('.button-data');
            buttons.forEach(button => {
                button.addEventListener('click', this.click);
            });
        },
        click: function (event) {
            // Sends a request and receives response from the server, than create and displays a modal window with data.
            event.preventDefault();
            const button = event.target;
            const buttonData = buttonDataGet(button);

            dh.apiPost(
                c.api.URL,
                dh.prepareRequestData(buttonData[c.data.key.columnName], buttonData[c.data.key.data]),
                modalWindow.show,
                buttonData
            );

            function buttonDataGet (button) {
                // Collects the data necessary to display the modal window. The pattern:
                return {
                    [c.data.key.recordName]: button.dataset.recordName,
                    [c.data.key.columnName]: button.dataset.columnName,
                    [c.data.key.data]: button.dataset.data
                };
            }
        }
    }
}