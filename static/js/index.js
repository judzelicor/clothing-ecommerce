const menuToggler = document.querySelector(".menuToggler__g7w9")
const mobileMenu = document.querySelector(".mobileTopIslandMenu__g7w9")
const closeMobileMenu = document.querySelector(".closeMobileMenu__g7w9")

menuToggler.addEventListener("click", () => {
    mobileMenu.classList.add("visible")
})

closeMobileMenu.addEventListener("click", () => {
    mobileMenu.classList.remove("visible")
})