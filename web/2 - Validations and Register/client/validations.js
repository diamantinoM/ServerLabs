export {
    installValidators,
    validateAllFields,
    resetAllFields,
    ValidationError,
    addPredicates,
};

let predicates = makePredicates({
    emailAddr : /^[a-z\d]{2,}@[a-z\d]{2,}\.[a-z]{2,}$/i
});

function makePredicates(predicateDefs) {
    const predicates = {};
    for (let [predName, predValue] of Object.entries(predicateDefs)) {
        const predExpr = predValue.hasOwnProperty('expr') ? predValue.expr : predValue;
        let predDef = (
            predExpr instanceof Function ? {expr: predExpr}
          : predExpr instanceof RegExp   ? 
                        {expr: (inputValue) => predExpr.test(inputValue.trim())}
          : (inputValue) => inputValue.trim() === predicateValue
      );
      predDef.showSuccess = !!predValue.showSuccess;
      predicates[predName] = predDef;
    }
    return predicates;
}

function addPredicates(predicateDefs) {
    predicates = {...predicates, ...makePredicates(predicateDefs)};
}

function runPredicateFor(field) {
    if (field instanceof HTMLSelectElement) {
        return !field.required || field.value.trim() !== '';
    }
    else if (field.type === 'checkbox') {
        return !field.required || field.checked;
    }
    // assume field is input and type is 'text'
    const predDef = predicateDefOf(field)
    return (
        field.required ? predDef.expr(field.value)
        // if a field optional, we don't run the predicate if the value
        // is empty (ie, if it's empty, then it's valid)
        : field.value.trim() === '' || predDef.expr(field.value)
    );
}

function predicateNameOf(field) {
    return field.getAttribute('data-validation');
}

function predicateDefOf(field) {
    const predDef = predicates[predicateNameOf(field)];
    return predDef;
}

class ValidationError extends Error {};

function installValidators(ancestorNode = document) {
    // Install validators for inputs only. checkboxes and selects 
    // will be handled by the default validator in runPredicateFor
    fieldsToValidate(ancestorNode).forEach(
        field => field.addEventListener('input', ev => validateField(field))
    );
}

function validateAllFields(ancestorNode = document) {
    let allValid = true;
    fieldsToValidate(ancestorNode).forEach(function(field) {
        allValid &&= validateField(field);
    });
    return allValid;
}

function resetAllFields(ancestorNode = document) {
    ancestorNode.querySelectorAll('input, select').forEach(resetField);
}

function fieldsToValidate(ancestorNode = document) {
    const fields = ancestorNode.querySelectorAll(
        'input[data-validation], select[data-validation]'
    );
    return fields === null ? [] : [...fields];
}

function validateField(field) {
    const statusElem = getStatusElemFor(field);
    if (!statusElem) {
        throw new ValidationError(`No status element for field: ${describeField(field)}!`);
    }

    const isValid = runPredicateFor(field);
    if (isValid) {
        statusElem.classList.remove('status-error');
        const predDef = predicateDefOf(field);
        if (predDef && predDef.showSuccess) {
            statusElem.classList.add('status-success');
        }
    }
    else {
        statusElem.classList.add('status-error');
        statusElem.classList.remove('status-success');
    }
    return isValid;
}

function resetField(field) {
    if (field instanceof HTMLSelectElement) {
        field.selectedIndex = 0;
        const defaultOption = [...field.options].find(option => option.defaultSelected);
        if (defaultOption) {
            field.selectedIndex = defaultOption.index;
        }
    }
    else  if (field.type === 'checkbox') {
        field.checked = false;
    }
    else {
        field.value = '';
    }

    if (field.hasAttribute('data-validation')) {
        const statusElem = getStatusElemFor(field);
        if (!statusElem) {
            throw new ValidationError(`No status element for field: ${describeField(field)}`);
        }
        statusElem.classList.remove('status-error');
    }
}

function getStatusElemFor(field) {
    const statusElem = field.parentNode.querySelector('.status');
    return statusElem;
}

function describeField(field) {
    const type = field[Symbol.toStringTag] || field.constructor.name || 'N/D';
    const id = field.id || 'N/D';
    const name = field.name || 'N/D';
    return `<type: ${type} id: ${id} name: ${name}>`;
}

////////////////////////////////////////////////////////////////////////////////
