document.addEventListener("DOMContentLoaded", function () {
    const reverseMapping = jsVars.reverse_mapping;
    // contoh: {7:"A", 3:"K", 5:"Z"}

    const input = document.querySelector("input.form-control");
    const button = document.querySelector("button.btn-outline-success");

    const solvedBadge = document.querySelector(".badge.text-bg-success");
    const failedBadge = document.querySelector(".badge.text-bg-danger");

    let solved = 0;
    let failed = 0;

    button.addEventListener("click", () => {
        const userInput = input.value.trim().toUpperCase();

        // Ambil angka acak dari tabel
        const tdList = document.querySelectorAll("tr.text-center.fs-2.fw-bold td");
        const numbers = Array.from(tdList).map(td => parseInt(td.textContent));

        // Decode angka → huruf
        const correctLetters = numbers.map(n => reverseMapping[n] || "?");

        // Cek apakah input sesuai (hanya 1 huruf)
        const isCorrect = userInput === correctLetters[0];

        if (isCorrect) {
            solved++;
            solvedBadge.innerHTML = `Solved: ${solved}`;
            input.classList.add("is-valid");
            input.classList.remove("is-invalid");
        } else {
            failed++;
            failedBadge.innerHTML = `Failed: ${failed}`;
            input.classList.add("is-invalid");
            input.classList.remove("is-valid");
        }

        input.value = "";
        input.focus();
    });
});
