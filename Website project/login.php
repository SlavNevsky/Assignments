<?php
    session_start();
    // header('location:index.html');
    // echo "Sucessfully Logged in";

     // Connect to the database
     $dbusername = "if0_34366088";
     $servername = "sql206.infinityfree.com";
     $dbname = "if0_34366088_aficionados_db";
     $dbpassword = "P@ssword";
 
     $conn = mysqli_connect($servername, $dbusername, $dbpassword, $dbname);
     if(!$conn){
         die("Connection failed");
     }
 
    //  mysqli_select_db($conn, 'id20823144_rooibok_db');

     // Get the form data from the POST request
    //  $user_name = $_POST['user_name'];
     $user_name = $_POST['user_name'];
     $password = $_POST['password'];
     $hashed_password = password_hash($password, PASSWORD_DEFAULT);
     
    
 
     // Check for errors in connection
     if (mysqli_connect_errno()) {
         echo "Failed to connect to MySQL: " . mysqli_connect_error();
         exit();
     }
 
     //Check if account exists already
 
     $quer= "SELECT * FROM user_data WHERE user_name = '$user_name' && password = '$password'";
     $result= mysqli_query($conn, $quer);
     $num= mysqli_num_rows($result);
     if ($num==1){
        $_SESSION['user_name'] = $user_name;
        header('location:index.html');
        echo "Successfully logged in";
     }
 
     else{
        header('location:index.html');
     }

?>


