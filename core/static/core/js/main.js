const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

const Web = {
  handleEvents: function () {
    // Remove overlay
    const overlay = $(".overlay");
    overlay.addEventListener("click", () => {
      overlay.classList.toggle("overlay--active");
    });

    // Minimize sidebar
    const sidebar = $(".sidebar");
    const sidebar__minimize = $(".sidebar__minimize");
    sidebar__minimize.addEventListener("click", () => {
      sidebar.classList.toggle("sidebar--minimize");

      sidebar__minimize.classList.toggle("fa-caret-left");
      sidebar__minimize.classList.toggle("fa-caret-right");
    });

    // Select menu item
    const menu__items = $$(".menu__item");
    menu__items.forEach((element) => {
      element.addEventListener("click", () => {
        const menu__item__selected = $(".menu__item--selected");
        menu__item__selected.classList.toggle("menu__item--selected");
        menu__item__selected.classList.toggle("font-effect-anaglyph");

        element.classList.toggle("menu__item--selected");
        element.classList.toggle("font-effect-anaglyph");
      });
    });

    // Search button glowing after focusing search field
    const search__field = $(".search-bar__field");
    const search__btn = $(".search-bar__btn");
    search__field.addEventListener("focus", () => {
      search__btn.style.color = "white";
      search__btn.style.textShadow =
        "0 0 0.125em hsl(0 0% 100% / 0.3), 0 0 0.45em white";
    });
    search__field.addEventListener("focusout", () => {
      search__btn.style.color = "var(--red-color-2)";
      search__btn.style.textShadow =
        "0 0 0.125em hsl(0 0% 100% / 0.3), 0 0 0.45em var(--red-color-2)";
    });
  },

  start: function () {
    this.handleEvents();
  },
};

Web.start();
