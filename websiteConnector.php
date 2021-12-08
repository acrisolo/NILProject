<?php

$servername = "localhost";
$database = "nil";
$username = "root";
$password = "dataBases234!";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);

//define PDO- tell about databse file
$pdo = new PDO($servername,$database, $username, $password);

//$link =  mysqli_connect("localhost","root", "dataBases234!", "nil");
//return $link;

//write SQL
$statement = $pdo->query("SELECT * FROM test");

//run the SQL
$rows = $statement->fetchAll(PDO::FETCH_ASSOC);

//show it on the screen
var_dump($rows);
