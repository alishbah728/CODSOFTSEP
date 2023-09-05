document.addEventListener("DOMContentLoaded", function () {
    const lengthInput = document.getElementById("length");
    const complexitySelect = document.getElementById("complexity");
    const generateButton = document.getElementById("generate");
    const passwordDisplay = document.getElementById("password");

    generateButton.addEventListener("click", function () {
        const length = parseInt(lengthInput.value);
        const complexity = complexitySelect.value;
        const password = generatePassword(length, complexity);
        passwordDisplay.textContent = password;
    });

    function generatePassword(length, complexity) {
        let charset = "";

        if (complexity.includes("lowercase")) {
            charset += "abcdefghijklmnopqrstuvwxyz";
        }
        if (complexity.includes("uppercase")) {
            charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        }
        if (complexity.includes("digits")) {
            charset += "0123456789";
        }
        if (complexity.includes("special")) {
            charset += "!@#$%^&*()-_+=<>?";
        }

        let password = "";
        for (let i = 0; i < length; i++) {
            const randomIndex = Math.floor(Math.random() * charset.length);
            password += charset.charAt(randomIndex);
        }

        return password;
    }
});
