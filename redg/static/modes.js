
const toggleColorMode = e =>{
    if (e.currentTarget.classList.contains("light--hidden")){
      document.documentElement.setAttribute("color-scheme", "light");

      localStorage.setItem("color-scheme", "light");
      return;
    }

    document.documentElement.setAttribute("color-scheme", "dark");

    localStorage.setItem("color-scheme", "dark");
};

const toggleColorButtons = document.querySelectorAll(".btn-mode-toggle")

toggleColorButtons.forEach(btn =>{
  btn.addEventListener("click", toggleColorMode);

});
