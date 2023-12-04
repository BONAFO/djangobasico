document.getElementById("form").onsubmit=async(e)=>{
    e.preventDefault()
    const form = new FormData(document.getElementById("form"));
    const method = "POST";
    const url = window.location.href;
    const response = await fetch(url, {
        method: method,
        body: (method !== "GET") ? (form) : (undefined),
        credentials: 'same-origin',
    })
    console.log(response)
    if(response.status === 500){
        document.getElementById("err-500").hidden = false;
    }else {
        document.getElementById("err-500").hidden = true;

    }
}