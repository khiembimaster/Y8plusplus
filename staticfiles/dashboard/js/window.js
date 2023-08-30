const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

const Web = {
  handleEvents: function () {
    // Select navigation item
    const windows_nav__items = $$(".window__nav__item");
    console.log(windows_nav__items);
    windows_nav__items.forEach((element) => {
      element.addEventListener("click", () => {
        const windows_nav__item__selected = $(".window__nav__item--selected");
        windows_nav__item__selected.classList.toggle(
          "window__nav__item--selected"
        );

        element.classList.toggle("window__nav__item--selected");
      });
    });
  },

  start: function () {
    this.handleEvents();
  },
};

Web.start();
