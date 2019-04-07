
var numPoints = 350;


var numbernode = document.getElementById("numbernode");
numbernode.innerHTML = numPoints;

var mypath = document.getElementById("mypath");
var pathLength = mypath.getTotalLength();
var polinePoints = [];

for (var i = 0; i < numPoints; i++) {
    var p = mypath.getPointAtLength(i * pathLength / numPoints);
    polinePoints.push(p.x);
    polinePoints.push(",");
    polinePoints.push(p.y);
    polinePoints.push("\n");
}

var mypolygon = document.getElementById("mypolyline");
mypolygon.setAttribute("points", polinePoints.join(" "));
var mytextarea = document.getElementById("mytextarea");
polinePoints.unshift("<polyline points='\n");
polinePoints.push("' />");

mytextarea.innerHTML = polinePoints.join(" ");