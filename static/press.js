const deepFind = (f, obj = {}) =>
{ if (Object (obj) === obj)
  { if (f (obj) === true)
      return obj

    for (const [ k, v ] of Object.entries (obj))
    { const res =
        deepFind (f, v)

      if (res !== undefined)
        return res
    }
  }

  return undefined
}



window.onload = function () {
  document.getElementById("input1").addEventListener("input", getText);
};

function getText() {
  var c = document.getElementById("input1").value;
  fetch("/tabledata")
    .then((res) => res.json())
    .then((data) => {
      const d = deepFind((x) => x.name === c, data);
      if (typeof d !== "undefined") {
        document.getElementById("input2").value = d.company;
      } else {
        document.getElementById("input2").value = "";
      }
    });
}
