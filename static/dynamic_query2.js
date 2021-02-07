const deepFind2 = (f, obj = {}) =>
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



document.getElementById("cargo_itemInput").addEventListener("input", getText2);

  
  
  function getText2 () {
    var n = document.getElementById('cargo_itemInput').value;
    console.log(n);
    fetch("/productdata")
    .then((res) => res.json())
    .then((data) => {
      const m = deepFind2((x) => x.product === n, data);
      if (typeof m !== "undefined") {
        document.getElementById("hs_codeInput").value = m.hs_code;
      } else {
        document.getElementById("hs_codeInput").value = "";
      }
    })
  };