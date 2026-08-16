document.addEventListener("DOMContentLoaded", function () {

    const input = document.getElementById(
        "answer-input"
    );

    const button = document.getElementById(
        "solve-button"
    );

    const countdown = document.getElementById(
        "countdown"
    );

    let remainingTime = Math.ceil(
        window.decodingRemainingTime || 0
    );

    let timeUp = false;


    // ==========================================
    // FINISH TASK
    // ==========================================

    function finishTask() {

        if (timeUp) {
            return;
        }

        timeUp = true;

        input.disabled = true;
        button.disabled = true;

        countdown.textContent = "Time's Up";

        const form = document.querySelector("form");

        if (form) {
            form.submit();
        }
    }


    // ==========================================
    // UPDATE COUNTDOWN
    // ==========================================

    function updateCountdown() {

        if (remainingTime <= 0) {
            finishTask();
            return;
        }

        const minutes = Math.floor(
            remainingTime / 60
        );

        const seconds = remainingTime % 60;

        countdown.textContent =
            "Countdown: "
            + String(minutes).padStart(2, "0")
            + ":"
            + String(seconds).padStart(2, "0");

        remainingTime--;
    }


    // ==========================================
    // INITIAL COUNTDOWN
    // ==========================================

    updateCountdown();


    const countdownInterval = setInterval(
        function () {

            if (timeUp) {
                clearInterval(
                    countdownInterval
                );

                return;
            }

            updateCountdown();

            if (timeUp) {
                clearInterval(
                    countdownInterval
                );
            }

        },
        1000
    );


    // ==========================================
    // SOLVE BUTTON
    // ==========================================

    button.addEventListener(
        "click",
        function () {

            if (timeUp) {
                return;
            }

            const answer = input.value
                .trim()
                .toUpperCase();

            if (!answer) {
                return;
            }

            liveSend({
                answer: answer
            });

            input.value = "";

            input.focus();
        }
    );


    // ==========================================
    // ENTER KEY
    // ==========================================

    input.addEventListener(
        "keydown",
        function (event) {

            if (event.key === "Enter") {

                event.preventDefault();

                button.click();
            }
        }
    );

});


    function liveRecv(data) {

    console.log(
        "Response backend:",
        data
    );

    if (data.time_up) {

        input.disabled = true;
        button.disabled = true;

        return;
    }

    if (data.error) {

        console.error(data.error);

        return;
    }

    document.querySelector(
        ".badge-solved"
    ).textContent =
        "Solved: "
        + data.correct_answers;

    document.querySelector(
        ".badge-failed"
    ).textContent =
        "Failed: "
        + data.incorrect_answers;

    const table =
        document.querySelector(
            "#decoding-table"
        );

    const letterCells =
        table.querySelectorAll(
            ".letter-cell"
        );

    const numberCells =
        table.querySelectorAll(
            ".number-cell"
        );

    data.letters.forEach(
        function (letter, index) {

            letterCells[index]
                .textContent = letter;
        }
    );

    data.numbers.forEach(
        function (number, index) {

            numberCells[index]
                .textContent = number;
        }
    );

    const targetCells =
        document.querySelectorAll(
            ".target-cell"
        );

    data.target_numbers.forEach(
        function (number, index) {

            targetCells[index]
                .textContent = number;
        }
    );
}