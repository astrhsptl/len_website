document.getElementById("id_avatar").oninput = function() {
    let imgLabel = document.getElementsByTagName("label")[0]
    let img = document.getElementById("id_avatar")
    // imgLabel.style.color = "rgba(6, 45, 120, 0.9)";
    imgLabel.style.color = "rgba(6, 45, 120, 0.9)";
    // imgLabel.style.fontWeight = "400";
    imgLabel.textContent = img.files[0].name 
}