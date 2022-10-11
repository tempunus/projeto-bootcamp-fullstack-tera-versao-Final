const progressValue = document.getElementsByClassName("percent")
console.log(progressValue)
const input = document.getElementsByClassName("valueInput").value
console.log(input)

changeProgress = () => {
    progressValue.setAttribute("style", "width"+ input + "%")
    console.log(progressValue)

}
