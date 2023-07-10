const serverDomain = "http://127.0.0.1:8000/api/v1/docs/product/create/";

function manageProductForm() {
    let form = document.getElementById("product__create").style
    if (form.display === "block") {
        form.display = "none";
    } else {
        form.display = "block";
    }
}

function takeNumberic(event) {
    // let regex = ;
    event.target.value = parseInt(event.target.value) || 0;
}

function closeForm() {
    document.getElementById("product__create").style.display = "none";
}

async function sendData(event, id) {
    event.preventDefault();

    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";

    let formData = new FormData(document.getElementsByClassName('active_form')[0]);
    formData.append("user", id);
    await axios.post("http://127.0.0.1:8000/api/v1/docs/product/create/", 
            formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                }}).then(res => console.log(res.data)).catch(err => console.log(err));
    location.reload();
}