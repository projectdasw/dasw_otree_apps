let remainingTime;
let timerInterval;
let gameFinished = false;
let submitting = false;

document.addEventListener('DOMContentLoaded', function () {
    remainingTime = Number(window.transcriptionGame.remainingTime || 0);
    updateTimer();
    startTimer();
    setupSubmitButton();
    focusInput();
});

function startTimer() {
    timerInterval = setInterval(function () {
        if (gameFinished) {clearInterval(timerInterval); return;}
        remainingTime--;
        if (remainingTime < 0) {remainingTime = 0;}
        updateTimer();
        if (remainingTime <= 0) {handleTimeUp();}
    }, 1000);
}

function updateTimer() {
    const timer = document.getElementById('timer');
    const totalSeconds = Math.max(0, Math.floor(remainingTime));
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;


    if (!timer) {return;}
    timer.textContent = String(minutes).padStart(2, '0') + ':' + String(seconds).padStart(2, '0');
}

function setupSubmitButton() {
    const button = document.getElementById('submit-answer');

    if (!button) {return;}
    button.addEventListener('click', submitAnswer);
}

function submitAnswer() {
    const button = document.getElementById('submit-answer');
    const input = document.getElementById('transcription-input');
    const answer = input.value;

    if (gameFinished) {return;}
    if (submitting) {return;}
    if (remainingTime <= 0) {handleTimeUp(); return;}
    if (!input) {return;}
    submitting = true;
    if (button) {button.disabled = true; button.textContent = 'Checking...';}
    liveSend({type: 'submit', answer: answer});

    // Debug
    // console.log('Sending answer:', answer);
}

function liveRecv(data) {
    if (!data) {console.warn('liveRecv received empty data'); return;}
    if (data.type === 'time_up') {handleTimeUp(data); return;}
    if (data.type === 'next_task') {handleNextTask(data); return;}
    console.warn('Unknown server response:', data);

    // Debug
    // console.log('Received from server:', data);
}

function handleNextTask(data) {
    const button = document.getElementById('submit-answer');
    const input = document.getElementById('transcription-input');
    const sourceText = document.getElementById('source-text');

    submitting = false;
    updateElement('completed-count', data.completed_count);
    updateElement('score', data.score);
    updateElement('correct-count', data.correct_count);
    updateElement('incorrect-count', data.incorrect_count);

    if (typeof data.remaining_time !== 'undefined') {
        remainingTime = Number(data.remaining_time);
        updateTimer();
    }

    if (sourceText) {sourceText.textContent = data.next_task;}
    if (input) {input.value = ''; input.disabled = false; input.focus();}
    if (button) {button.disabled = false; button.textContent = 'Submit Answer';}
    showFeedback(data.correct);

    // Debug
    // console.log('Loading next task:', data.next_task);
}

function showFeedback(correct) {
    const feedback = document.getElementById('feedback');

    if (!feedback) {return;}

    if (correct) {
        feedback.textContent = 'Correct! Keep it up';
        feedback.className = 'fw-bold text-success';
    } else {
        feedback.textContent = 'Incorrect. Try the next puzzle!';
        feedback.className = 'fw-bold text-danger';
    }

    feedback.style.display = 'block';

    setTimeout(function () {
        if (!gameFinished) {
            feedback.style.display = 'none';
        }
    }, 800);
}

function handleTimeUp(data) {
    const button = document.getElementById('submit-answer');
    const input = document.getElementById('transcription-input');
    const form = document.getElementById('form');

    if (gameFinished) {return;}
    gameFinished = true;
    remainingTime = 0;
    clearInterval(timerInterval);
    updateTimer();
    if (input) {input.disabled = true;}
    if (button) {button.disabled = true;}

    setTimeout(function () {
        if (form) {
            form.submit();
        }
    }, 500);
}

function updateElement(elementId, value) {
    const element = document.getElementById(elementId);

    if (!element) {return;}
    element.textContent = value;
}

function focusInput() {
    const input = document.getElementById('transcription-input');

    if (input) {input.focus();}
}