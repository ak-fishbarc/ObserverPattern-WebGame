const range_value = document.getElementById("RangeValue");
const howmany = document.getElementById("Howmany");

range_value.innerHTML = howmany.value;
howmany.addEventListener("input", (event) => {
    range_value.innerHTML = event.target.value;
});

howmany.addEventListener("submit", (event) => {
    event.stopImmediatePropagation();
});

