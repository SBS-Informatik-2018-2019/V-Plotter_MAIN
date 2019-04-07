function run() {

    // selected numbers
    var numPointsPolyline = document.getElementById("numPointsPolyline").value;
    var numPointsPathSegment = document.getElementById("numPointsPathSegment").value;
    var svgviewbox =  document.getElementById("svgviewBox").value;
    document.getElementById("svg").setAttribute("viewBox", "0 0 " + svgviewbox + " " + svgviewbox);


    // list to path
    var mytextareapathold = document.getElementById("mytextareapathold");
    document.getElementById("mypath").setAttribute("d", mytextareapathold.value);

    // one polyline from the path
    var mypath = document.getElementById("mypath");
    var pathLength = mypath.getTotalLength();
    var polinePoints = [];
    for (var i = 0; i < numPointsPolyline; i++) {
        var p = mypath.getPointAtLength(i * pathLength / numPointsPolyline);
        polinePoints.push(p.x);
        polinePoints.push(",");
        polinePoints.push(p.y);
        polinePoints.push("\n");
    }
    var mypolyline = document.getElementById("mypolyline");
    mypolyline.setAttribute("points", polinePoints.join(" "));
    polinePoints.unshift("<polyline points='\n");
    polinePoints.push("' />");
    var mytextareapolyline = document.getElementById("mytextareapolyline");
    mytextareapolyline.innerHTML = polinePoints.join(" ");

    // path only with lines
    var mypath = document.getElementById("mypath");
    var pathdata = mypath.getAttribute("d").toUpperCase();
    var paths = [];
    paths = pathdata.split("M");
    var newpath = [];
    
    for (var j = 1; j < paths.length; j++) {
        var element = paths[j];
        var pathdummy = document.getElementById("dummy");
        pathdummy.setAttribute("d", "M " + element);
        var pathDummyLength = pathdummy.getTotalLength();
       
        var p = pathdummy.getPointAtLength(0.0000000001);
        newpath.push("M");
        newpath.push(p.x);
        newpath.push(p.y);
        newpath.push("L");
        for (var i = 1; i < numPointsPathSegment; i++) {
            var p = pathdummy.getPointAtLength(i * pathDummyLength / numPointsPathSegment);
            newpath.push(p.x);
            newpath.push(p.y);
        }
        
    }
    document.getElementById("dummy").removeAttribute("d")
    var newpathelement = document.getElementById("new");
    newpathelement.setAttribute("d", newpath.join(" "))

    newpath.unshift("<path d='")
    var mytextareapathnew = document.getElementById("mytextareapathnew");
    newpath.push("' />")
    mytextareapathnew.innerHTML = newpath.join(" ");


    
}