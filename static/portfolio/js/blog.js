async function like(object, post) {
    if (object.liked === undefined) {
        let result = await fetch('/blog/like/' + post);

        if (result.ok) {
            object.src = '/static/portfolio/img/like-blue.png';
            object.nextElementSibling.innerHTML = await result.text();
            object.liked = true;
        }
    }
}