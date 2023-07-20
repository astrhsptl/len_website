let preload = () => {
    for (let item of document.getElementsByClassName("preload")) {
        item.classList.remove("preload");
    };
}

window.onload = preload()


function openHeaderMenu() {
    document.getElementById("burger_opened").classList.add('burger_state_open');
    document.getElementsByTagName("body")[0].style.overflow = "hidden";
};

function closeHeaderMenu() {
    document.getElementById("burger_opened").classList.remove('burger_state_open')
    document.getElementsByTagName("body")[0].style.overflow = "auto";
}