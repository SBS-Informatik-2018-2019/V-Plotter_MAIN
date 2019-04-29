<!DOCTYPE html>
<html lang="de">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3pro.css">
    <title>V-Plotter Pathcreator V2 - Processing...</title>
</head>

<body>
    <div class="w3-margin">
        <h1>V-Plotter Pathcreator</h1>
        <h6>Version 2.0</h6>
        <br>
        <?php
        if (isset($_POST["textarea"])) :
            ?>
            <div class="w3-cell w3-mobile">
                <div class="w3-panel w3-card w3-center w3-margin">
                    <h2>Input</h2>
                    <textarea readonly id="textarea_in" class="w3-animate-input w3-codespan" width="70%"><?php echo (str_replace("  ", " ", trim($_POST["textarea"]))); ?></textarea>
                    <label for="input_numberPerPathSegment">input_numberPerPathSegment=</label><input type="number" id="input_numberPerPathSegment" value="<?php echo (str_replace(" ", "", trim($_POST["textarea"]))); ">
                    <br><br>
                </div>
            </div>
            <img src="/superpath/loading.gif.dis" class="w3-image" alt="Loading">
            <div class="w3-cell w3-mobile">
                <div class="w3-panel w3-card w3-center w3-margin">
                    <h2>Absolute</h2>
                    <textarea readonly id="textarea_out_absolute"></textarea>
                    <script src="raphael.min.js"></script>
                    <script>
                        // use Raphael.js to Absolute Path Coordinates
                        try {
                            var path_string = document.querySelector("#textarea_in").innerHTML;
                            var path_string_rel = Raphael.pathToRelative(path_string);
                            var path_string_abs = Raphael._pathToAbsolute(path_string_rel);
                            document.querySelector("#textarea_out_absolute").innerHTML = path_string_abs;
                        } catch (error) {
                            document.querySelector("#textarea_out_absolute").innerHTML = "ERROR - Please check Path d";
                        }
                    </script>
                </div>
            </div>
            <div class="w3-cell w3-mobile">
                <div class="w3-panel w3-card w3-center w3-margin">
                    <h2>Svg für V-Plotter</h2>
                    <textarea readonly id="textarea_out_plotter"></textarea>
                    <svg display="none">
                        <path id="path_dummy" d="">
                    </svg>
                    <script>
                        //Kommentar
                        try {
                            var pathdata = document.querySelector("#textarea_out_absolute").innerHTML;
                            var numPointsPathSegment = document.querySelector("#input_numberPerPathSegment").value;
                            var paths = [];
                            paths = pathdata.split("M");
                            var newpath = [];
                            for (var j = 1; j < paths.length; j++) {
                                var element = paths[j];
                                var pathdummy = document.getElementById("path_dummy");
                                pathdummy.setAttribute("d", "M " + element);
                                var pathDummyLength = pathdummy.getTotalLength();
                                var p = pathdummy.getPointAtLength(0.0000000001);
                                newpath.push("M");
                                newpath.push(p.x + ",");
                                newpath.push(p.y);
                                newpath.push("\n");
                                newpath.push("L");
                                for (var i = 1; i < numPointsPathSegment + 1; i++) {
                                    var p = pathdummy.getPointAtLength(i * pathDummyLength / numPointsPathSegment);
                                    newpath.push(p.x + ",");
                                    newpath.push(p.y);
                                    newpath.push("\n");
                                }
                            }
                            pathdummy.setAttribute("d","");
                            newpath.unshift("<svg xmlns='http://www.w3.org/2000/svg'><path d='");
                            newpath.push("' fill='none' stroke='black'/></svg>")
                            document.querySelector("#textarea_out_plotter").innerHTML = newpath.join(" ");
                        } catch (error) {
                            console.log(error)
                            document.querySelector("#textarea_out_plotter").innerHTML = "ERROR - Please check Path d";
                        }
                    </script>
                </div>
            </div>

        <?php
    endif;
    if (!isset($_POST["textarea"])) :
        ?>
            <h2>Oops something went wrong...</h2>

        <?php
    endif;
    ?>
        <a href="create.php">Back</a>
    </div>

</body>

</html>