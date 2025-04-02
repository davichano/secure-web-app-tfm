let loginAttempts = 0;

function handleLogin() {
    if (loginAttempts >= 5) {
        alert("Has superado el número máximo de intentos. Por favor, inténtalo más tarde.");
        return;
    }
    loginAttempts++;
    // Lógica para manejar el inicio de sesión
}