<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="style.css">
        <title>V-Plotter Pathcreator - MAIN</title>
    </head>
    <body>
        <script src="script.js"></script>
        <h1>V-Plotter Pathcreator</h1>
        <a href="choose.php">Templates</a>
        <a href="">Reload page</a>
        <a href="index.php?clear">Clear page</a>
        
        <table>
            <tr>
                <th>Polyline</th>
                <th>original Path data=</th>
                <th>new Path (only L and M)</th>
            </tr>
            <tr>
                <td><textarea id="mytextareapolyline" readonly></textarea></td>
                <td><textarea id="mytextareapathold" ><?php if($_GET["d"]){echo(urldecode($_GET["d"]));} ?></textarea></td>
                <td><textarea id="mytextareapathnew" readonly></textarea></td>
            </tr>
            <tr>
                <td>Number of Polylinepoints=<input type="number" id="numPointsPolyline" min="10"<?php if($_GET["npp"]){echo("value='".$_GET["npp"]."'");} ?>></td>
                
                <td>
                    Viewbox-Size=<input type="number" id="svgviewBox" <?php if($_GET["svb"]){echo("value='".$_GET["svb"]."'");} ?>>
                    <input type="submit" onclick="run();">
                </td>
                <td>Number per Path Segment=<input type="number" id="numPointsPathSegment" min="10" <?php if($_GET["npps"]){echo("value='".$_GET["npps"]."'");} ?>></td>
            </tr>
            <tr>
                <td>green</td>
                <td>black</td>
                <td>red</td>
            </tr>
        </table>
        <svg xmlns="http://www.w3.org/2000/svg" id="svg">
            <path id="mypath"></path>
            <polyline id="mypolyline" points="" />
            <path id="new"></path>
            <path id="dummy"></path>
        </svg>
    </body>
</html>