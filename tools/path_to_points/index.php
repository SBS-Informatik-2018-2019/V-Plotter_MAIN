<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3pro.css">
    <link rel="stylesheet" href="style.css">
    <title>V-Plotter Pathcreator - MAIN</title>
</head>

<body>
    <script src="raphael.min.js"></script>
    <script src="script.js"></script>
    <h1>V-Plotter Pathcreator</h1>
    <a href="choose.php">Templates</a>
    <a href="index.php?clear">Clear page</a>
    <a href="" id="link1" style="display:none">Reload page</a>
    Share:<input type="url" id="link2" readonly>

    <table>
        <tr>
            <th>Polyline</th>
            <th>original Path data=</th>
            <th>new Path (only L and M)</th>
        </tr>
        <tr>
            <td><textarea id="mytextareapolyline" readonly></textarea></td>
            <td><textarea id="mytextareapathold"><?php if ($_GET["d"]) {
                                                        echo (urldecode($_GET["d"]));
                                                    } ?></textarea></td>
            <td><textarea id="mytextareapathnew" readonly></textarea></td>
        </tr>
        <tr>
            <td>Number of Polylinepoints=<input type="number" id="numPointsPolyline" min="10" <?php if ($_GET["npp"]) {
                                                                                                    echo ("value='" . $_GET["npp"] . "'");
                                                                                                } ?>>
            </td>
            <td>
                Viewbox-Size=<input type="number" id="svgviewBox" <?php if ($_GET["svb"]) {
                                                                        echo ("value='" . $_GET["svb"] . "'");
                                                                    } ?>>
                <input type="submit" onclick="run();">
                <br>

            </td>
            <td>Number per Path Segment=<input type="number" id="numPointsPathSegment" min="10" <?php if ($_GET["npps"]) {
                                                                                                    echo ("value='" . $_GET["npps"] . "'");
                                                                                                } ?>>
            </td>
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
    Absolute Path d=
    <textarea id="bottom" readonly></textarea>

</body>

</html>