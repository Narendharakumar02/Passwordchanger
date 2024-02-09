<?php
$con=new mysqli('localhost','root','','databasesaveinfo');
if($con){
    echo "connection is successfull !!";
}
else{
    die(mysqli_error($con));
}

?>