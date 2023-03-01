import { 
    installValidators,
    validateAllFields,
    resetAllFields,
    addPredicates,
} from './validations.js';

import {
    bySel,
    whenClick,
    syncWait,
    isValidDate,
    byPOSTasJSON,
} from './utils.js';


const URL = 'http://127.0.0.1:8000';
const TOURNAMENT_ID = 1;

addPredicates({
    fullName           : /^\p{Letter}{2,}( \p{Letter}{2,})+$/u,
    password           : { 
        expr: /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[#$%&]).{6,10}$/,
        showSuccess: true,
    },
    confirmPassword     : {
        expr: confirmPassword,
        showSuccess: true,
    },
    'date_DD/MM/YYYY'  : isValidDate,
    phoneNumber        : /^(\+\d{3})?\d{9}$/,
});

window.addEventListener('load', function() {
    installValidators();
    whenClick('reset', e => resetAllFields());
    whenClick('submit', validateAndSubmitForm);
});

async function validateAndSubmitForm() {
    if (!validateAllFields()) {
        return;
    }
    try {
        const [responseOK, responseData] = await registerPlayer();
        const showStatusFn = responseOK ? showSuccess : showError;
        showStatusFn(responseData);
    } 
    catch (error) {
        showSubmissionInfo(`ERROR: An error has ocurred when connecting to server at ${URL}`, false);
        console.error(error);
    }
}

async function registerPlayer() {
    const player = {
        full_name     : bySel('[name=fullName]').value,
        email         : bySel('[name=email]').value,
        password      : bySel('[name=password]').value,
        phone_number  : bySel('[name=phoneNumber]').value,
        birth_date    : bySel('[name=birthDate]').value,
        level         : bySel('[name=level]').value,
        tournament_id : TOURNAMENT_ID,
    };
    const response = await byPOSTasJSON(`${URL}/register`, player);
    return [response.ok, await response.json()];
}

/**
 * @param {Object} responseData 
 */
function showSuccess(responseData) {
    const msg = `Inscrição realizada com sucesso.<br>
Player: ${responseData.full_name} <br>
ID: ${responseData.id} <br>
Email: ${responseData.email}`;
    const formFields = document.querySelector('.info');
    formFields.style.display = 'none';
    const elemsToHide = document.querySelectorAll('form > button, .checkbox');
    elemsToHide.forEach(elem => elem.style.display = 'none');
    showSubmissionInfo(msg, true);
}


/**
 * @param {Object} responseData 
 */
function showError(responseData) {
    const errorInfo = responseData.detail;
    const msg = `Não foi possível concluir a inscrição. ${errorInfo.error_msg}`;
    showSubmissionInfo(msg, false);
}

function showSubmissionInfo(msg, success) {
    const submissionStatusElem = document.querySelector('.submission-status');
    const [cssClassToAdd, cssClassToRem] = (success ? 
          ['submission-status-ok', 'submission-status-error'] 
        : ['submission-status-error', 'submission-status-ok'] 
    );
    submissionStatusElem.innerHTML = `${msg}`;
    submissionStatusElem.classList.add(cssClassToAdd);
    submissionStatusElem.classList.remove(cssClassToRem);
}

function confirmPassword(passwd2) {
    const passwd1 = document.getElementById('password').value;
    return passwd1 && passwd1 === passwd2;
}

