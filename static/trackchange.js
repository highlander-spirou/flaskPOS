document.getElementById("cityInput").addEventListener("input", sendText);

function sendText() {
  var c = document.getElementById("cityInput").value;
  fetch("/cache", {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify({ cityInput: c }),
  });
}
