function openPage(x, y) {
    var indice = x
    var target = y
    var url = 'http://127.0.0.1:5555/web/courses/allCourses/html/' + indice + '.html'
   

    var xml = new XMLHttpRequest()

    xml.onreadystatechange = function () {
        if (xml.readyState == 4 && xml.status == 200) {
            document.getElementById(target).innerHTML = xml.responseText
        }
    }

    xml.open("GET", url, true)

    xml.send()
}