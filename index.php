<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Apache server controlled Jetson nano leds</title>
      <link rel="stylesheet" href="style.css">
   </head>
   <body>
      


      <form action="ledon.php">
         <input id="button"  value="ON" type="submit" id="btnon">
      </form>

      <form action="ledoff.php">
         <input id="button2" type="submit" value="OFF" id="btnoff">
      </form>
      
       <form action="led_select.php" method="POST">
      <div class="input-wrapper">
         <input class="input" autocomplete="off" name="ledselect" placeholder="Select Leds. Sample: 00110 1 open 0 closed" type="text">
      </div> 
<input type="submit"  value="Select" id="btnselect" >
      </form>

      <img src="b-removebg-preview.png" width=350 >

      <h1>Coded by Ali edis</h1>
   </body>
</html>
