const menu = document.getElementById('menu');

for (const e of menu.children) {
    e.onclick = function () {
        toggle_menu();
    }
}

window.onscroll = function() {
    if (scrollY == 0) {
        header.classList.remove(['header-scrolled']);
    } else if (!header.classList.contains('header-scrolled')) {
        header.classList.add(['header-scrolled']);
    }
};


function toggle_menu() {
    if (!menu.classList.contains('open')) {
        menu.classList.add('open');
    } else {
        menu.classList.remove('open');
    }
}