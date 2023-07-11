const serverDomain = "http://127.0.0.1:8000/api/v1/docs/product/create/";

document.getElementById("id_photo").oninput = function() {
    let imgLabel = document.getElementById("image_container")
    let img = document.getElementById("id_photo")
    imgLabel.textContent = img.files[0].name 
}

function manageProductForm() {
    let form = document.getElementById("product__create").style
    let body = document.getElementsByTagName("body")[0]

    if (form.display === "block") {
        form.display = "none";
        body.style.overflow = "auto";
    } else {
        body.style.overflow = "hidden";
        form.display = "block";
    }
}

function takeNumberic(event) {
    event.target.value = parseInt(event.target.value) || 0;
}

function closeForm() {
    document.getElementById("product__create").style.display = "none";
    document.getElementsByTagName("body")[0].style.overflow = "auto";
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