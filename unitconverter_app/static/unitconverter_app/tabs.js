const tabElements = document.querySelectorAll("button[role='tab']");
const panelElements = document.querySelectorAll("div[role='tabpanel']");
let activeIndex = 0;

tabElements.forEach((tab, index) => {
  tab.addEventListener("click", () => {
    setActiveTab(index);
  });
});

const setActiveTab = (index) => {
  tabElements[activeIndex].setAttribute("aria-selected", "false");
  tabElements[index].setAttribute("aria-selected", "true");
  setActivePanel(index);
  activeIndex = index;
};
const setActivePanel = (index) => {
  panelElements[activeIndex].setAttribute("hidden", "");
  panelElements[index].removeAttribute("hidden");
};
