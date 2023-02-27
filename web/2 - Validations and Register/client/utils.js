export {
    byID,
    bySel,
    bySelAll,
    whenClick,
    whenAllClick,
    syncWait,

    byPOSTasJSON,

    isValidDate,
    timedRun,
};

////////////////////////////////////////////////////////////////////////////////
///
///     DOM
///
////////////////////////////////////////////////////////////////////////////////

/**
 * @param {string} id 
 * @returns Element
 */
function byID(id) {
    return document.getElementById(id);
}

/**
 * @param {string} selector
 * @returns Element
 */
function bySel(selector) {
    return document.querySelector(selector);
}

/**
 * @param {string} selector
 * @returns Array[Element]
 */
function bySelAll(selector) {
    return [...document.querySelectorAll(selector)];
}

/**
 * @param {string} id 
 * @param {Function} handler 
 */
function whenClick(id, handler) {
    document.getElementById(id).addEventListener('click', handler);
}

/**
 * @param {string} query
 * @param {Function} handler
 */
function whenAllClick(query, handler) {
    for (let elem of document.querySelectorAll(query)) {
        elem.addEventListener('click', handler);
    }
}

////////////////////////////////////////////////////////////////////////////////
///
///     COMMUNICATIONS
///
////////////////////////////////////////////////////////////////////////////////

/**
 * @param {string} fetchURL 
 * @param {Object} dataObj 
 * @param {boolean} responseAsJSON 
 * @returns 
 */
async function byPOSTasJSON(fetchURL, dataObj, mode = 'cors') {
    const resp = await fetch(fetchURL, {
            method: 'POST',
            mode: mode,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dataObj),
        });
    return resp;
}

////////////////////////////////////////////////////////////////////////////////
///
///     MISC
///
////////////////////////////////////////////////////////////////////////////////

/**
 * 
 * @param {number} millisecs 
 */
function syncWait(millisecs) {
    const until = Date.now() + millisecs;
    while (Date.now() <= until) { }
}

function isValidDate(date) {
    const YEAR       = '(19[0-9][0-9]|20[0-4][0-9]|2050)';
    const DD_MM_31   = '(0[1-9]|[12][0-9]|30|31)/(0[13578]|1[02])';
    const DD_MM_30   = '(0[1-9]|[12][0-9]|30)/(0[469]|11)';
    const DD_FEB     = '(0[1-9]|1[0-9]|2[0-8])/02';
    const LEAP_YEARS = '(1904|1908|1912|1920|1924|1928|1932|1936|1940|1944'
                       + '|1948|1952|1956|1960|1964|1968|1972|1976|1980'
                       + '|1984|1988|1992|1996|2000|2004|2008|2012|2016'
                       + '|2020|2024|2028|2032|2036|2040|2044|2048)'
                       ;
    const DD_FEB_LEAP_YEAR = `(0[1-9]|[12][0-9])/02/${LEAP_YEARS}`;
    const dateRegExp = new RegExp(
        `^(${DD_FEB_LEAP_YEAR}|(${DD_MM_31}|${DD_MM_30}|${DD_FEB})/${YEAR})$`
    );
    return dateRegExp.test(date.trim());
}

// const isValidDate = (function() {
//     const YEAR       = '(19[0-9][0-9]|20[0-4][0-9]|2050)';
//     const DD_MM_31   = '(0[1-9]|[12][0-9]|30|31)/(0[13578]|1[02])';
//     const DD_MM_30   = '(0[1-9]|[12][0-9]|30)/(0[469]|11)';
//     const DD_FEB     = '(0[1-9]|1[0-9]|2[0-8])/02';
//     const LEAP_YEARS = '(1904|1908|1912|1920|1924|1928|1932|1936|1940|1944'
//                        + '|1948|1952|1956|1960|1964|1968|1972|1976|1980'
//                        + '|1984|1988|1992|1996|2000|2004|2008|2012|2016'
//                        + '|2020|2024|2028|2032|2036|2040|2044|2048)'
//                        ;
//     const DD_FEB_LEAP_YEAR = `(0[1-9]|[12][0-9])/02/${LEAP_YEARS}`;
//     const dateRegExp = new RegExp(
//         `^(${DD_FEB_LEAP_YEAR}|(${DD_MM_31}|${DD_MM_30}|${DD_FEB})/${YEAR})$`
//     );
//     return function isValidDate(date) {
//         return dateRegExp.test(date.trim())
//     };
// })();

function isValidDate2(date) {
    const dateRegExp = new RegExp(`^\d{2}/\d{2}/\d{4}$`);
    date = date.trim();
    if (dateRegExp.test(date)) {
        const [day, month, year] = date.split('/').map(valStr => parseInt(val, 10));
        if (year >= 1900 && year <= 2050 && month >= 1 && month <= 12 
            && day >= 1 ) {
            return    [1, 3, 5, 7, 8, 10, 12].includes(month) && day <= 31
                   || [4, 6, 9, 11].includes(month) && day <= 30
                   || month === 2 && isLeapYear(year) && day <= 29
                   || month === 2 && day <= 28
            ;
        }
    }
    return false;
}

function isLeapYear(year) {
    return year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0);
}

function timedRun(fun, ...args) {
    const start = Date.now();
    for (let i = 0; i < 10_000_000; i += 1) {
        fun(...args);
    }
    return (Date.now() - start) / 1000;
}
