<?php
    $hostname = "localhost";
    $dbName = "teste";
    $dbUser = "root";
    $password = "";

    $mysqli = new mysqli($hostname, $dbUser ,$password, $dbName);

    if($mysqli->connect_errno){
        echo "Falha na conexão: (".$mysqli->connect_errno.") ".$mysqli->connect_error;
    }
    else{
        echo "Conexão realizada com sucesso!";
    }

?>