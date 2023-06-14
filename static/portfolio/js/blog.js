async function like(post) {
    await fetch('/blog/like/' + post);
}