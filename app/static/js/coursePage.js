function openPage(x, y) {
    var indice = x
    var target = y
    var url = 'https://tempunus.github.io/projeto-bootcamp-fullstack-tera-versao-Final/web/courses/allCourses/html/' + indice + '.html'
   

    var xml = new XMLHttpRequest()

    xml.onreadystatechange = function () {
        if (xml.readyState == 4 && xml.status == 200) {
            document.getElementById(target).innerHTML = xml.responseText
        }
    }

    xml.open("GET", url, true)

    xml.send()

}



    const progress = document.getElementById('progress')
    const next = document.getElementById('next')
    const circles = document.querySelectorAll('.circle')


    let currentActive = 1

    next.addEventListener('click', () => {
        
    var url = 'https://tempunus.github.io/projeto-bootcamp-fullstack-tera-versao-Final/web/courses/allCourses/html/' + currentActive + '.html'
   

    var xml = new XMLHttpRequest()

    xml.onreadystatechange = function () {
        if (xml.readyState == 4 && xml.status == 200) {
            document.getElementById("courseContent").innerHTML = xml.responseText
        }
    }

    xml.open("GET", url, true)

    xml.send()
    if(currentActive > circles.length){
        currentActive = circles.length
    }

    currentActive++


    update()
    console.log(currentActive)
    console.log(typeof(currentActive))

    

    })



    function update(){
    circles.forEach((circle, idx) => {
        if (idx < currentActive) {
        circle.classList.add('active')
        }else{
        circle.classList.remove('active')
        }
    })


    const actives = document.querySelectorAll('.active')

    progress.style.width = (actives.length - 1) / (circles.length - 1) * 100 + '%'


    if (currentActive === circles.length) {
        next.disabled = true
    }else{
        next.disabled = false
    }
    }








    


