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



document.getElementById("consignee_nameInput").addEventListener("input", getText3);

  
  
function getText3() {
    var c = document.getElementById("consignee_nameInput").value;
    console.log(c);
    fetch("/companydata")
      .then((res) => res.json())
      .then((data) => {
        const d = deepFind((x) => x.company === c, data);
        if (typeof d !== "undefined") {
          document.getElementById("consignee_addressInput").value = d.address;
          document.getElementById("consignee_telephoneInput").value = d.telephone;
        } else {
          document.getElementById("consignee_addressInput").value = "";
          document.getElementById("consignee_telephoneInput").value = "";
        }
      });
  }