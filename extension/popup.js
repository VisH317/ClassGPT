const input = document.getElementById("question")
const p = document.getElementById("output")
const button = document.getElementById("button")

input.addEventListener("change", () => {
    p.innerText = ""
})

button.addEventListener("click", () => {
    if(input.value==="") return
    // setup request and set to output
})

