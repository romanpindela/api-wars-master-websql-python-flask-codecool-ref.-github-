// --------------------------------------------------------------------------------------------------------------------
//                                                       API Wars
//                                                 client: utilities.js
//                                                        v 1.0
// --------------------------------------------------------------------------------------------------------------------

export let utilities = {
    capitalize: function (text, lower = false) {
        /**
         * Capitalizes first letters of words in string.
         * @param {string} text String to be modified
         * @param {boolean=false} lower Whether all other letters should be lowercased
         * @return {string}
         * @usage
         *   capitalize('fix this string');     // -> 'Fix This String'
         *   capitalize('javaSCrIPT');          // -> 'JavaSCrIPT'
         *   capitalize('javaSCrIPT', true);    // -> 'Javascript'
         */
        return (lower ? text.toLowerCase() : text).replace(/(?:^|\s|["'([{])+\S/g, match => match.toUpperCase());
    }
}