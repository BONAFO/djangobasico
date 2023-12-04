
// document.getElementById("delete_account").onclick = async (e) => {
//     e.preventDefault()
//     const user_confirm = prompt("Estas seguro de querer eliminar tu cuenta \n eso es irreversible... \n y nos vas a poner tristes... =_( \n Mi contraseña:");
//     if (user_confirm.trim() !== "") {
//         const response = await fetch(e.target.href, {
//             method: 'POST',
//             body: JSON.stringify({
//                 "password": user_confirm.trim()
//             }),

//             headers: {
//                 "X-CSRFToken": get_cookies("csrftoken"),
//                 "content-type": "application/json",
//             },
//         });
//     }

// }

// csrfmiddlewaretoken

// const delete_user = () => {

// }


document.getElementById("delete_account").onclick = async (e) => {
    e.preventDefault()
    const user_confirm = confirm("Estas seguro de querer eliminar tu cuenta \n eso es irreversible... \n y nos vas a poner tristes... =_(");
    document.getElementById("formi-cont").hidden = !user_confirm

}

document.getElementById("formi").onsubmit = async (e) => {
    e.preventDefault()
    const formdata = new FormData(document.getElementById("formi"));
    fetch(document.getElementById("delete_account").href, {
        method: 'POST',
        body: formdata,
        credentials: 'same-origin',
    }).then(res => {
        if (res.status === 200) {
            alert("Adios! =_) Te vamos a extrañar")
            window.location.reload()
        }
    });
}