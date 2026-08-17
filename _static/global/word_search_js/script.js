function submitGuess() {

    const input = document.getElementById("countGuess");
    const guess = input.value.trim();

    if (guess === "") {
        input.focus();
        return;
    }

    liveSend({
        count_guess: guess
    });
}


liveRecv = function(data) {

    // =========================
    // UPDATE SCORE
    // =========================

    if (data.new_score !== undefined) {

        const scoreElement =
            document.getElementById("playerScore");

        scoreElement.textContent = data.new_score;

        if (data.new_score > 0) {
            scoreElement.classList.add(
                "fw-bold",
                "text-success"
            );
        }
    }


    // =========================
    // UPDATE TARGET
    // =========================

    if (data.new_target_character !== undefined) {

        document.getElementById(
            "targetCharacter"
        ).textContent =
            data.new_target_character;
    }


    // =========================
    // UPDATE BOARD
    // =========================

    if (data.new_board !== undefined) {

        const boardBody =
            document.getElementById("boardBody");

        // Hanya hapus isi tbody
        boardBody.innerHTML = "";


        data.new_board.forEach(row => {

            const tr = document.createElement("tr");


            row.forEach(char => {

                const td = document.createElement("td");

                td.className =
                    "board-cell border border-3 fs-4";


                const strong =
                    document.createElement("strong");

                strong.textContent = char;


                td.appendChild(strong);
                tr.appendChild(td);

            });


            boardBody.appendChild(tr);

        });
    }

    if (data.correct !== undefined) {

    const feedback = document.getElementById("feedback");

    if (data.correct) {
        feedback.textContent = "Correct!";
        feedback.className = "alert alert-success fw-bold mt-3";
    } else {
        feedback.textContent = "Incorrect. Try the next puzzle!";
        feedback.className = "alert alert-danger fw-bold mt-3";
    }
}


    // =========================
    // RESET INPUT
    // =========================

    document.getElementById("countGuess").value = "";
};