<?php

$post_deger=$_POST["ledselect"];

try {
    $baglanti = new PDO("mysql:host=localhost;dbname=jetson", "sammy", "Password123#@!");
    $baglanti->exec("SET NAMES utf8");
    $baglanti->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $sorgu = $baglanti->prepare("UPDATE led SET led_status = ? WHERE id = 1");
    $sorgu->bindParam(1, $post_deger, PDO::PARAM_STR);
    
    $sorgu->execute();

    if ($sorgu->rowCount() > 0) {
       Header("location:index.php");
    } else {
        echo "Herhangi bir kay?t güncellenemedi.";
    }

} catch (PDOException $e) {
    die($e->getMessage());
}

$baglanti = null;

?>
