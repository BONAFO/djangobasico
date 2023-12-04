const get_cookies=(cookie)=>{
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
        const cookie_arr = cookies[i].split("=");
        if(cookie_arr[0].toLowerCase() === cookie.toLowerCase()){
            return  cookie_arr[1]
        }
        
    }
}

