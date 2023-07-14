document.getElementById("id_avatar").oninput = function() {
    let imgLabel = document.getElementsByTagName("label")[0]
    let img = document.getElementById("id_avatar")
    imgLabel.textContent = img.files[0].name 
}