document.forms[0].onsubmit = async (f) => {
    f.preventDefault();

    const parameters = new URLSearchParams(window.location.search);

    const uname = document.querySelector('#username').value;
    const pword = document.querySelector('#password').value;

    const formData = new FormData();

    formData.append('username', uname);
    formData.append('password', pword);
    formData.append('next', parameters.get('next'));

    await fetch(url='/login/', data={
        method: 'POST',
        redirect: 'follow',
        body: formData
    }).then(async resp => { console.log(await resp.text()) });
}