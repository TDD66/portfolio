const counter = document.getElementById("visitor-counter");

fetch("https://visitor-counter-344446164530.europe-west2.run.app")
    .then(response => response.json())
    .then(data => {
        counter.textContent = "Visitor Counter: " + data.count;
        counter.style.visibility = "visible";
    })
    .catch(() => {
        counter.textContent = "Visitor Counter: ...";
        counter.style.visibility = "visible";
    });