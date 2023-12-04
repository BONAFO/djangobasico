document.getElementById("form").onsubmit = (e) => {
    e.preventDefault()
    const form = new FormData(document.getElementById("form"));
    // const formData ={};
    // for (let pair of form.entries()) {
    //     formData[pair[0]] = pair[1];
    // }
    // let url = window.location.origin;
    // url+="/app/delete-user/12"

    const url = window.location.href;
    fetch(url,{
        method: 'POST',
        body: form,
        credentials: 'same-origin',
    });
    // const form = document.getElementById("form");
    // var formData = new FormData(form);
    // // output as an object
    // console.log(Object.fromEntries(formData));

    // // ...or iterate through the name-value pairs
    // for (var pair of formData.entries()) {
    //   console.log(pair[0] + ": " + pair[1]);
    // }

}


