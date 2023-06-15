const header = document.getElementById('header');
const theme_toggle = document.getElementById('theme-toggle');

function toggle_theme() {
    const label = theme_toggle.children[0];
    const opposite_theme = label.innerHTML === 'dark_mode' ? 'dark' : 'light';
    const current_theme = opposite_theme === 'dark' ? 'light' : 'dark';

    label.innerHTML = current_theme + '_mode';

    for (const e of document.querySelectorAll(`.${current_theme}`)) {
        e.classList.replace(current_theme, opposite_theme);
    }

    localStorage.setItem('theme', opposite_theme);
}

const themeCookie = localStorage.getItem('theme');

if (themeCookie === 'light') {
    toggle_theme();
}