<?php
$database_username='sammy';
$database_password='Password123#@!';
try{
    $db=new PDO("mysql:host=localhost;jetson=data;charset=utf8",$database_username,$database_password);
    echo "Database Connect Successfully";
    echo '<br>';
  
} catch (PDOExpception $e){
    echo $e->getMessage();
}

?>
