
const form = new FormData(document.getElementById("form"));
document.getElementById("form").onsubmit=(e)=>{
    e.preventDefault()
    const url = window.location.href;
    const method = "post";
    
    fetch(url,{
        method: method,
        body: (method !== "GET") ? (form) : (undefined),
        credentials: 'same-origin',
    });
}