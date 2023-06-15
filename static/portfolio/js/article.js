const form = document.forms['form'];

async function comecarComentario() {
    form.classList.remove('hidden');
}

/* form.onsubmit = _ => {
    form.classList.
} */

async function like(object, comentario) {
    if (object.liked === undefined) {
        let result = await fetch('/blog/comment/' + comentario + '/like');

        if (result.ok) {
            object.src = '/static/portfolio/img/like-blue.png';
            object.nextElementSibling.innerHTML = await result.text();
            object.liked = true;
        }
    }
}