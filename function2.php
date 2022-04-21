<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Function</title>
</head>
<body>
  <h1>Function</h1>
  <?php
    function basic(){
      print("Lorem<br>");
      print("Lorem2<br>");
    }

    basic();
    basic();
   ?>
   <h2>parameter &amp; argument</h2>
   <?php
   function sum($left, $right){
     print($left+$right);
     print("<br>");
   }
    sum(2,3);
    sum(22,9);
    ?>
 </body>
 </html>
