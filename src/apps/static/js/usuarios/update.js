document.getElementById("form").onsubmit= (e)=> {
    e.preventDefault()
    const form = new FormData(document.getElementById("form"));

    const url = window.location.href;
    const method = "post";
    fetch(url,{
        method: method,
        body: (method !== "GET") ? (form) : (undefined),
        credentials: 'same-origin',
    });
}