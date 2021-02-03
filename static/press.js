
window.onload = function () {
  document.getElementById("btn").addEventListener("click", getText);
};


function getText() {
  var c = document.getElementById("input1").value;
  fetch("/tabledata")
    .then((res) => res.json())
    .then((data) => {
        const d = deepFind (x => x.name === "asdj", data)
        console.log(d)
    })

}

