
(function () {
    const gameElement = document.getElementById('aljebraic-game');

    if (!gameElement) return;

    let questionId = Number(gameElement.dataset.questionId);
    let remainingSeconds = Math.ceil(Number(gameElement.dataset.remainingSeconds));
    let waitingForResponse = false;
    let gameFinished = false;
    let timerInterval;

    const timerElement = document.getElementById('timer');
    const answerInput = document.getElementById('answer-input');
    const submitButton = document.getElementById('submit-answer');
    const messageElement = document.getElementById('message');

    function renderTimer() {
        const minutes = Math.floor(remainingSeconds / 60);
        const seconds = remainingSeconds % 60;

        timerElement.textContent =
            String(minutes).padStart(2, '0') + ':' +
            String(seconds).padStart(2, '0');
    }

    function finishGame() {
        if (gameFinished) return;

        gameFinished = true;
        waitingForResponse = true;
        answerInput.disabled = true;
        submitButton.disabled = true;
        messageElement.textContent = 'Waktu habis. Menampilkan hasil...';

        clearInterval(timerInterval);

        const nextButton = document.querySelector('.otree-btn-next, button[name="submit"]');
        if (nextButton) {
            nextButton.click();
        }
    }

    function submitAnswer() {
        if (gameFinished || waitingForResponse) return;

        const value = answerInput.value.trim();

        if (value === '' || !Number.isInteger(Number(value))) {
            messageElement.textContent = 'Masukkan jawaban berupa bilangan bulat.';
            answerInput.focus();

            return;
        }

        waitingForResponse = true;
        submitButton.disabled = true;
        messageElement.textContent = '';

        liveSend({
            type: 'answer',
            answer: value,
            question_id: questionId
        });
    }

    submitButton.addEventListener('click', submitAnswer);

    answerInput.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            submitAnswer();
        }
    });

    // Callback global untuk pesan dari server oTree.
    window.liveRecv = function (data) {
        if (data.finished) {
            finishGame();
            return;
        }

        if (data.error) {
            messageElement.textContent = data.error;

            waitingForResponse = false;
            submitButton.disabled = false;
            answerInput.focus();
            return;
        }

        if (data.stale) {
            messageElement.textContent = 'Soal telah berubah. Silakan jawab soal yang tampil.';
            waitingForResponse = false;
            submitButton.disabled = false;
            return;
        }

        if (data.question !== undefined) {
            questionId = Number(data.question_id);
            document.getElementById('question').textContent = data.question;
            document.getElementById('correct-count').textContent = data.correct_count;
            document.getElementById('wrong-count').textContent = data.wrong_count;
            document.getElementById('score').textContent = data.total_score;

            answerInput.value = '';
            waitingForResponse = false;
            submitButton.disabled = false;
            answerInput.focus();
        }
    };

    renderTimer();

    timerInterval = setInterval(function () {
        if (gameFinished) {
            clearInterval(timerInterval);
            return;
        }

        remainingSeconds = Math.max(0, remainingSeconds - 1);
        renderTimer();

        if (remainingSeconds <= 0) {
            finishGame();
        }
    }, 1000);

    answerInput.focus();
})();
