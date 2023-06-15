const bars = document.getElementsByClassName('bar-parent');

for (const bar of bars) {
    const pct = bar.dataset.pct;

    bar.style.width = pct.toString() + '%';
}