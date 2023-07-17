document.getElementById("id_photo").oninput = function() {
    let imgLabel = document.getElementById("image_container")
    let img = document.getElementById("id_photo")
    imgLabel.textContent = img.files[0].name 
    imgLabel.style.color = "rgba(6, 45, 120, 0.9)";
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
