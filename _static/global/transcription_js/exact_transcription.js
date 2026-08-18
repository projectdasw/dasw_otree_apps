let remainingTime;
let timerInterval;

let gameFinished = false;
let submitting = false;


// ============================================================
// INITIALIZATION
// ============================================================

document.addEventListener('DOMContentLoaded', function () {

    remainingTime =
        Number(window.transcriptionGame.remainingTime || 0);

    updateTimer();

    startTimer();

    setupSubmitButton();

    focusInput();

});


// ============================================================
// TIMER
// ============================================================

function startTimer() {

    timerInterval = setInterval(function () {

        if (gameFinished) {

            clearInterval(timerInterval);

            return;
        }

        remainingTime -= 1;

        updateTimer();

        if (remainingTime <= 0) {

            remainingTime = 0;

            updateTimer();

            handleTimeUp();

        }

    }, 1000);

}


function updateTimer() {

    const timerElement =
        document.getElementById('timer');

    if (!timerElement) {
        return;
    }

    const totalSeconds =
        Math.max(
            0,
            Math.floor(remainingTime)
        );

    const minutes =
        Math.floor(totalSeconds / 60);

    const seconds =
        totalSeconds % 60;

    timerElement.textContent =
        String(minutes).padStart(2, '0')
        + ':'
        + String(seconds).padStart(2, '0');

}


// ============================================================
// SUBMIT BUTTON
// ============================================================

function setupSubmitButton() {

    const button =
        document.getElementById('submit-answer');

    if (!button) {
        return;
    }

    button.addEventListener(
        'click',
        submitAnswer
    );

}


function submitAnswer() {

    if (gameFinished) {
        return;
    }

    if (submitting) {
        return;
    }

    if (remainingTime <= 0) {

        handleTimeUp();

        return;
    }

    const input =
        document.getElementById(
            'transcription-input'
        );

    if (!input) {
        return;
    }

    const answer =
        input.value;

    submitting = true;

    setSubmitState(true);

    liveSend({

        type: 'submit',

        answer: answer

    });

}


// ============================================================
// SUBMIT BUTTON STATE
// ============================================================

function setSubmitState(disabled) {

    const button =
        document.getElementById(
            'submit-answer'
        );

    if (!button) {
        return;
    }

    button.disabled = disabled;

    if (disabled) {

        button.dataset.originalText =
            button.textContent;

        button.textContent =
            'Checking...';

    } else {

        button.textContent =
            button.dataset.originalText ||
            'Submit Answer';

    }

}


// ============================================================
// RECEIVE SERVER RESPONSE
// ============================================================

function liveRecv(data) {

    if (!data) {
        return;
    }


    // ========================================================
    // TIME UP
    // ========================================================

    if (data.type === 'time_up') {

        handleTimeUp(data);

        return;
    }


    // ========================================================
    // NEXT TASK
    // ========================================================

    if (data.type === 'next_task') {

        handleNextTask(data);

    }

}


// ============================================================
// HANDLE NEXT TASK
// ============================================================

function handleNextTask(data) {

    submitting = false;

    setSubmitState(false);


    // --------------------------------------------------------
    // UPDATE SCORE
    // --------------------------------------------------------

    updateElement(
        'score',
        data.score
    );


    updateElement(
        'completed-count',
        data.completed_count
    );


    updateElement(
        'correct-count',
        data.correct_count
    );


    // --------------------------------------------------------
    // UPDATE TIMER
    // --------------------------------------------------------

    if (
        typeof data.remaining_time !==
        'undefined'
    ) {

        remainingTime =
            Number(
                data.remaining_time
            );

        updateTimer();

    }


    // --------------------------------------------------------
    // UPDATE SOURCE TEXT
    // --------------------------------------------------------

    updateElement(
        'source-text',
        data.next_task
    );


    // --------------------------------------------------------
    // CLEAR INPUT
    // --------------------------------------------------------

    const input =
        document.getElementById(
            'transcription-input'
        );

    if (input) {

        input.value = '';

        input.focus();

    }


    // --------------------------------------------------------
    // FEEDBACK
    // --------------------------------------------------------

    showFeedback(
        data.correct
    );


    // --------------------------------------------------------
    // CHECK TIMER
    // --------------------------------------------------------

    if (remainingTime <= 0) {

        handleTimeUp();

    }

}


// ============================================================
// FEEDBACK
// ============================================================

function showFeedback(correct) {

    const feedback =
        document.getElementById(
            'feedback'
        );

    if (!feedback) {
        return;
    }


    if (correct) {

        feedback.textContent =
            'Correct!';

        feedback.className =
            'alert alert-success';

    } else {

        feedback.textContent =
            'Incorrect.';

        feedback.className =
            'alert alert-danger';

    }


    feedback.style.display =
        'block';


    setTimeout(function () {

        if (!gameFinished) {

            feedback.style.display =
                'none';

        }

    }, 800);

}


// ============================================================
// TIME UP
// ============================================================

function handleTimeUp(data) {

    if (gameFinished) {
        return;
    }

    gameFinished = true;

    remainingTime = 0;

    clearInterval(timerInterval);

    updateTimer();

    setSubmitState(true);


    const input =
        document.getElementById(
            'transcription-input'
        );

    if (input) {

        input.disabled = true;

    }


    if (data) {

        if (
            typeof data.score !==
            'undefined'
        ) {

            updateElement(
                'score',
                data.score
            );

        }

        if (
            typeof data.completed_count !==
            'undefined'
        ) {

            updateElement(
                'completed-count',
                data.completed_count
            );

        }

        if (
            typeof data.correct_count !==
            'undefined'
        ) {

            updateElement(
                'correct-count',
                data.correct_count
            );

        }

    }


    // --------------------------------------------------------
    // REDIRECT TO RESULTS
    // --------------------------------------------------------

    setTimeout(function () {

    const form =
        document.getElementById('form');

    if (form) {

        form.submit();

    }

}, 500);

}


// ============================================================
// HELPER
// ============================================================

function updateElement(
    elementId,
    value
) {

    const element =
        document.getElementById(
            elementId
        );

    if (!element) {
        return;
    }

    element.textContent =
        value;

}


function focusInput() {

    const input =
        document.getElementById(
            'transcription-input'
        );

    if (input) {

        input.focus();

    }

}