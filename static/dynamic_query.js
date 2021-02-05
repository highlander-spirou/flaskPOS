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
  document.getElementById("companyInput").addEventListener("input", getText);
};

function getText() {
  var c = document.getElementById("companyInput").value;
  console.log(c);
  fetch("/fixed_data")
    .then((res) => res.json())
    .then((data) => {
      const d = deepFind((x) => x.company === c, data);
      if (typeof d !== "undefined") {
        document.getElementById("cityInput").value = d.city;
        document.getElementById("zipInput").value = d.zipcode;
      } else {
        document.getElementById("cityInput").value = "";
        document.getElementById("zipInput").value = "";
      }
    });
}
