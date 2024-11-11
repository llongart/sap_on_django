// /**
//  * Cambiar automáticamente a modo oscuro/claro dependiendo del tema del usuario
// **/
// let prefers = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
// let html = document.querySelector('html');
 
// html.classList.add(prefers);
// html.setAttribute('data-bs-theme', prefers);  

// Cambiar el color del tema de la página (Oscuro/Claro)
let currentTheme = getDefaultTheme();
setTheme(currentTheme);

addButtonThemeListener();

/**
 * Listens for the click of the button and execute the theme change
**/
function addButtonThemeListener() {
    const buttonToggler = document.querySelector('[data-bs-theme-toggle]');
    buttonToggler.addEventListener("click", () => {
        const newTheme = getNewTheme(currentTheme);
        setTheme(newTheme);
        currentTheme = newTheme;
        saveTheme(newTheme);
    });
}

/**
 * Get the default theme for the user
 * @return {String} theme - the theme of the user
 *
**/
function getDefaultTheme() {
    const systemSettingDark = window.matchMedia("(prefers-color-scheme: dark)");
    const systemSettingTheme = systemSettingDark.matches ? "dark" : "light";
    const savedTheme = getSavedTheme();
    return savedTheme ? savedTheme : systemSettingTheme;
}


/**
 * Returns the new theme
 * @param {String} theme - the current app theme, dark or light
 *
**/
function getNewTheme(theme) {
    return theme === "dark" ? "light" : "dark";
}

/**
 * Sets the theme globally
 * @param {String} theme - dark or light
 *
**/
function setTheme(theme) {
    const html = document.querySelector("html");
    // html.classList.add(getDefaultTheme())
    html.setAttribute("data-bs-theme", theme);
}

/**
 * Returns the theme saved in memory
 * @return {String} theme - the saved theme
 *
**/
function getSavedTheme() {
    return localStorage.getItem("data-bs-theme");
}

/**
 * Saves theme in memory
 * @return {String} theme - the theme to save
 *
**/
function saveTheme(theme) {
    localStorage.setItem("data-bs-theme", theme);
}

