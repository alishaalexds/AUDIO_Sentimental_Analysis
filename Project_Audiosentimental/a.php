
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Audio sentimental </title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

    <link rel="stylesheet" href="style.css">

    <style>
    audio {
        vertical-align: bottom;
        width: 10em;
    }
    video {
        max-width: 100%;
        vertical-align: top;
    }
    input {
        border: 1px solid #d9d9d9;
        border-radius: 1px;
        font-size: 2em;
        margin: .2em;
        width: 30%;
    }
    p,
    .inner {
        padding: 1em;
    }
    li {
        border-bottom: 1px solid rgb(189, 189, 189);
        border-left: 1px solid rgb(189, 189, 189);
        padding: .5em;
    }
    label {
        display: inline-block;
        width: 8em;
    }
    </style>

  
</head>

<body>
 
    <article>
      
<h1 style="text-align:center">Audio Sentiment Analysis </h1>

        <section class="experiment recordrtc">
         <div><a href='index.php'><button>Back To Home</button></a></div>
			<hr>
            

            <div >
			<h3>RESULT</h3>
               <?php
                $python=`python pgm.py`;
				
				echo "<pre> $python</pre>";
				?>
            </div>

            <br>

        </section>

</body>

</html>
