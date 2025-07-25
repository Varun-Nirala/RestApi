import * as Constants from './constants.js';

// Entry function.
mainEntry();

/**
 * Entry function in this script.
 *  1. Add `onRadioButtonSelectionChange()` function Event Listeners to the change in `RadioButton` (Text = GET_ALL, GET, POST) selection.
 *  2. Call `onRestRequestSubmitButton()` function which eventually add Event Listener to the `Button` (Text = Submit) button.
 */
function mainEntry() {
    console.log("mainEntry() Called");
    
    console.log("Welcome to the Home Page!");

    document.addEventListener('DOMContentLoaded', function() {
        
        const radioButtons = document.querySelectorAll('input[name="restMethodOptions"]');
        radioButtons.forEach(radio => {
            radio.addEventListener('change', onRadioButtonSelectionChange);
        });

        onRadioButtonSelectionChange();

        onRestRequestSubmitButton();
    });
}

/**
 * Parse the Json file present @filepath and if successful in parsing it as Json then call the `callbackFunction(filepath, data)`.
 * Where, 
 *      `filepath` is same as passed argument,
 *      `data` is parsed Json.
 */
function parseJson(filepath, callbackFunction){
    console.log(`parseJson(filepath}, callbackFunction) Called, with filepath = ${filepath}, callback = ${callbackFunction.name}`);

    fetch(filepath)
    .then(response => response.json())  // Parse the Json
    .then(data => {
        // Now data contains the JavaScript object parsed from JSON file.
        // Process json as you like using 'data' object.
        console.log(data);
        callbackFunction(filepath, data);
    })
    .catch(error => console.error(`Error loading Json file ${filepath}: ${error}`));
}

/**
 * Send `GET` REST request to the provided URL `endpoint`.
 * Return the recieved data.
 */
async function sendGetRequestToServerToGet(endpoint) {
    console.log(`sendGetRequestToServerToGet(endpoint) Called, with endpoint = ${endpoint}.`);

    // 'fetch()' API returns a Promise and not actual data.
    fetch(
        endpoint,
        { method: 'GET' }   // Default method is GET. So, we can remove this argument.
    )
    .then(response => response.json())
    .then(data => {
        // Now data contains the JavaScript object parsed from Json file.
        // Process json as you like using 'data' object.
        console.log(data);
        return data;
    })
    .catch(error => console.error(`Error occured in GET request: ${error}`));
}

/**
 * To be called on Send Get Request button click event.
 * @returns :   Failure -> throw exception error.
 *              Success -> Show output in 'Response'.
 */
function onSendGetRequestEvent() {
    console.log("onSendGetRequestEvent() Called.");
    // alert("onSendGetRequestEvent()");

    const url = `${BASE_URL}/about`;

    fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error(`Network responseded with Error. ${response.status} - ${response.statusText}!`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('result').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById('result').innerText = `Error: ${error.message}`;
    });
}

/**
 * Handle `GET` REST request, when `RadioButton` (Text = GET_ALL) is clicked.
 * It uses `sendGetRequestToServerToGet(endpoint)` function internally.
 * Param `inputVal` should be one of the `const GET_ALL_OPTIONS` defined in constants.js file.
 * 
 * Return: It return all data from either 'users.json', 'products.json' or 'orders.json'.
 */
async function handleSubmitRequest_GetALL(inputVal) {
    console.log(`handleSubmitRequest_GetALL() Called with ${inputVal}`);
    let resultText = "";

    for (let index = 0; index < Constants.GET_ALL_OPTIONS.length; index++) {
        if (inputVal == Constants.GET_ALL_OPTIONS[index]) {
            resultText = await sendGetRequestToServerToGet(`/getAll/${Constants.GET_ALL_OPTIONS[index]}`).toString();
            break;
        }
    }
    return resultText;
}

/**
 * Handle `GET` REST request, when `RadioButton` (Text = GET) is clicked.
 * It uses `sendGetRequestToServerToGet(endpoint)` function internally.
 * Param `inputVal` should be one of the `const GET_ONE_OPTION` defined in constants.js file.
 * 
 * Return: It return one of the entry from either 'users.json', 'products.json' or 'orders.json'.
 */
async function handleSubmitRequest_Get(inputVal) {
    console.log(`handleSubmitRequest_Get() Called with ${inputVal}`);

    let resultText = "";

    const tokens = inputVal.split('/');
    console.assert(tokens.length === 3, 'Tokens is not 3 as expected!');

    for (let index = 0; index < Constants.GET_ONE_OPTION.length; index++) {
        if (tokens[1] == Constants.GET_ONE_OPTION[index]) {
            resultText = await sendGetRequestToServerToGet(`/get/${Constants.GET_ONE_OPTION[index]}/tokens[2]`).toString();
            break;
        }
    }
    return resultText;
}

async function handleSubmitRequest_Post(inputVal) {
    let resultText = "";

    // TODO

    return resultText;
}


/**
 * Invoked as callback, as it registered with `Button` (Text = Submit).
 * It further dispatches request to other functions, depending on the selected `RadioButton` (Text = GET_ALL, GET, POST).
 */
function onRestRequestSubmitButton() {
    console.log("onRestRequestSubmitButton() Called.");
    // alert("onRestRequestSubmitButton()");
    document.getElementById('result').innerText = "";

    document.getElementById('restMethodForm').addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent from default submitting.

        const selectedRestMethod = getSelectedRestActionFromRadioButtons();
        console.log(`onRestRequestSubmitButton(), selected REST method: ${selectedRestMethod}`);

        let resultText = "";

        // Check if a radio button is selected
        if (selectedRestMethod.length != 0) {
            const inputVal = document.getElementById("restTextInput").value;

            switch(selectedRestMethod) {
                case "GET_ALL":
                    resultText = handleSubmitRequest_GetALL(inputVal);
                    break;

                case "GET":
                    resultText = handleSubmitRequest_Get(inputVal);
                    break;

                case "POST":
                    resultText = handleSubmitRequest_Post(inputVal);
                    break;

                default:
                    resultText = "Error case: Un-recognized option for GET request.";
                    break;
            }

        } else {
            resultText = "Please selected a REST method.";
        }

        document.getElementById('result').textContent = resultText;
    });
}

/**
 * Invoked as callback, as it registered with `RadioButton` (Text = GET_ALL, GET, POST).
 * It also displays the available options which user should put as arguments.
 */
function onRadioButtonSelectionChange() {
    console.log("onRadioButtonSelectionChange() Called.");
    // alert("onRadioButtonSelectionChange()");

    const additionalInput = document.getElementById('userRestInputField');
    const restAction = getSelectedRestActionFromRadioButtons();

    console.log(`restAction : ${restAction}`);

    const getOptions = Constants.GET_ALL_OPTIONS.map(element => element.slice(0, -1));

    let validOptionsText = "";
    switch (restAction) {
        case "GET_ALL":
            additionalInput.style.display = 'block';
            validOptionsText = `Can choose from: ${Constants.GET_ALL_OPTIONS.toString()}`;
            break;

        case "GET":
            additionalInput.style.display = 'block';
            validOptionsText = `Can choose from: ${getOptions.toString()}`;
            break;

        case "POST":
            additionalInput.style.display = 'block';
            validOptionsText = "TODO: Post";
            break;

        default:
            additionalInput.style.display = 'none'; // Hide the input field
            additionalInput.style.display = 'block';
            validOptionsText = "TODO: Default";
    }
    document.getElementById('validOptions').textContent = validOptionsText;
}

/**
 * Simple show alert box on button click with text showing Button name.
 */
function alertOnButtonClick(buttonId) {
    console.log("alertOnButtonClick() Called.");

    const button = document.getElementById(buttonId)

    button.addEventListener('click', function() {
        alert(`Button name = ${button.name} is clicked!`);
    });
}

/**
 * Simple show alert box on button click with text showing Button name and input value.
 */
function alertWithTextOfInputFieldOnButtonClick(buttonId, textFieldId) {
    console.log("alertWithTextOfInputFieldOnButtonClick() Called.");

    const button = document.getElementById(buttonId)
    button.addEventListener('click', function() {
        const inputVal = document.getElementById(textFieldId).value;
        alert(`Button name = ${button.name} associated with text input field = ${document.getElementById(textFieldId)} with value = ${inputVal} is clicked!`);
    });
}

/**
 * Get the easy to read REST (not actually REST, as we are returning GET_ALL [which is not a REST method], GET, and POST) 
 * method from the selected `RadioButton`.
 * @returns:
 *      `GET_ALL`   -> fetch all values.
 *      `GET`       -> fetch a single record.
 *      `POST`      -> TODO
 */
function getSelectedRestActionFromRadioButtons() {
    console.log("getSelectedRestActionFromRadioButtons() Called.");
    // alert("getSelectedRestActionFromRadioButtons()");
    const selectedRestMethod = document.querySelector('input[name="restMethodOptions"]:checked');

    let restMethod = "";

    switch (selectedRestMethod.value) {
        case "getRestMethod_All":
            restMethod = "GET_ALL";
            break;

        case "getRestMethod":
            restMethod = "GET";
            break;
        case "postRestMethod":
            restMethod = "POST";
            break;
    }
    return restMethod;
}