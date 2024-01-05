<?php

include 'config.php';
session_start();

if(isset($_POST['submit'])){

   $email = mysqli_real_escape_string($conn, $_POST['email']);
   $pass = mysqli_real_escape_string($conn, md5($_POST['password']));

   $select = mysqli_query($conn, "SELECT * FROM `user_form` WHERE email = '$email' AND password = '$pass'") or die('query failed');

   if(mysqli_num_rows($select) > 0){
      $row = mysqli_fetch_assoc($select);
      $_SESSION['user_id'] = $row['id'];
      header('location:home-login.php');
   }else{
      $message[] = 'Email dan Password Salah';
   }

}

?>

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Login I Puskesmas Sejahtera</title>
   <link rel="icon" href="gambar/logo-title.png" />

   <!-- custom css file link  -->
   <link rel="stylesheet" href="css/login.css">

</head>
<body>
<div class="form-container">
   <form action="" method="post" enctype="multipart/form-data">
      <h3>LOGIN</h3>
      <?php
      if(isset($message)){
         foreach($message as $message){
            echo '<div class="message">'.$message.'</div>';
         }
      }
      ?>
      <input type="email" name="email" placeholder="Masukkan E-mail" class="box" required>
      <input type="password" name="password" placeholder="Masukkan Password" class="box" required>
      <input type="submit" name="submit" value="Login" class="btn">
      <p>Tidak Punya Akun? <a href="register.php">Daftar Sekarang</a></p>
   </form>
</div>
<script src="https://cdn.rawgit.com/bungfrangki/efeksalju/2a7805c7/efek-salju.js" type="text/javascript"></script>
</body>
</html>