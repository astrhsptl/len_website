function openHeaderMenu() {
    let menu = document.getElementById("burger_opened");

    menu.classList.add('burger_state_open')

    document.getElementsByTagName("body")[0].style.overflow = "hidden";
}

function closeHeaderMenu() {
    document.getElementById("burger_opened").classList.remove('burger_state_open')
    document.getElementsByTagName("body")[0].style.overflow = "auto";

}