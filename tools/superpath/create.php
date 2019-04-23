<!DOCTYPE html>
<html lang="de">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3pro.css">
    <title>V-Plotter Pathcreator - V2</title>
</head>

<body>
    <div class="w3-margin">
        <h1>V-Plotter Pathcreator</h1>
        <h6>Version 2.0</h6>
        <br>
        Choose a way to enter your scetch
        <div class="w3-cell w3-mobile">
            <div class="w3-panel w3-card w3-center w3-margin">
                <form action="process_svg-def.php" method="post">
                    <h2>Put SVG-Path d(efinition) here:</h2>
                    <textarea class="w3-animate-input w3-codespan" name="textarea" width="70%"></textarea>
                    <br>
                    <button class="w3-btn w3-margin" type="submit">Senden</button>
                </form>
            </div>
        </div>
        <div class="w3-cell w3-mobile w3-disabled">
            <div class="w3-panel w3-card w3-center w3-margin">
                <h2>Comming soon...</h2>
                <textarea class="w3-animate-input w3-codespan" name="1" width="70%">enter full svg code</textarea>
                <br>
                <button class="w3-btn w3-margin" type="submit">Senden</button>
            </div>
        </div>
    </div>
</body>

</html>