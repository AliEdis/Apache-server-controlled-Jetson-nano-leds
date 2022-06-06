


<?php

try {

    $baglanti = new PDO("mysql:host=localhost;dbname=jetson", "sammy", "Password123#@!");
    $baglanti->exec("SET NAMES utf8");
    $baglanti->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $sonuc = $baglanti->exec("UPDATE led SET led_status=1 WHERE id=1;");
     
    if ($sonuc > 0) {
        header("Location:index.php");
 } else {
        Header("Location:index.php");  
  }

} catch (PDOException $e) {
    die($e->getMessage());
}

$baglanti = null;

?>
