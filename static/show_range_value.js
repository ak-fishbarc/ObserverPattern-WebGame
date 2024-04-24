// Script to show the value of the slider in the form.
const range_value = document.getElementById("RangeValue");
const howmany = document.getElementById("Howmany");

range_value.innerHTML = howmany.value;
howmany.addEventListener("input", (event) => {
    range_value.innerHTML = event.target.value;
});

// Prevent browser from resending data after submitting.
howmany.addEventListener("submit", (event) => {
    event.stopImmediatePropagation();
});


