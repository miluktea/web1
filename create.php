<?php
require_once('lib/print.php');
require('view/top.php');
?>

   <a href="create.php">create</a>
   <form action="create_process.php" method="post">
     <p><input type="text" name="title" placeholder="title"></p>
     <p><textarea name="description" placeholder="description"></textarea></p>
     <p><input type="submit"></p>
   </form>

<?php
require('view/bottom.php');
?>
