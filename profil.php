<?php

include 'config.php';
session_start();
$user_id = $_SESSION['user_id'];

if (!isset($user_id)) {
   header('location:login.php');
};

if (isset($_GET['logout'])) {
   unset($user_id);
   session_destroy();
   header('location:login.php');
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Profil</title>
   <link rel="icon" href="bekicot.jpg"/>

   <!-- custom css file link  -->
   <link rel="stylesheet" href="css/darkside.css">
   <link rel="stylesheet" href="css/jamal.css">
   <link rel="stylesheet" href="css/harus.css"/>
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>

</head>

<body>
   <nav>
      <div class="logo" style="display: flex;align-items: center;">
         <span class="brand-text" style="color:#01939c; font-size:26px; font-weight:bold; letter-spacing: 1px;margin-left: 20px;">K</span>
         <span class="brand-text" style="color:#01939c; font-size:26px; font-weight:bold; letter-spacing: 1px;margin-left: 10px;">K</span>
         <span class="brand-text" style="color:#01939c; font-size:26px; font-weight:bold; letter-spacing: 1px;margin-left: 10px;">B</span>
      </div>
        </div>
        <div class="hamburger">
            <div class="line1"></div>
            <div class="line2"></div>
            <div class="line3"></div>
        </div>
        <ul class="nav-links">
            <li><a href="beranda.html">BERANDA</a></li>
            <li><a href="#">VISI DAN MISI</a></li>
            <li><a href="profil.php">PROFIL</a></li>
            <li><a href="index2.php">DISCUSION</a></li>  
        </ul>
   </nav>

   <div class="container">


      <div class="profile">
         <?php
         $select = mysqli_query($conn, "SELECT * FROM `user_form` WHERE id = '$user_id'") or die('query failed');
         if (mysqli_num_rows($select) > 0) {
            $fetch = mysqli_fetch_assoc($select);
         }
         if ($fetch['image'] == '') {
            echo '<img src="images/default-avatar.png">';
         } else {
            echo '<img src="uploaded_img/' . $fetch['image'] . '">';
         }
         ?>
         <h3><?php echo $fetch['name']; ?></h3>
         <a href="update_profile.php" class="btn">update profile</a>
         <a href="profil.php?logout=<?php echo $user_id; ?>" class="delete-btn">logout</a>
         <p>new <a href="login.php">login</a> or <a href="register.php">register</a></p>
      </div>

      <div class="profile1">
         <div class="kalimat">
            <span class="text">Profile Anggota</span>
            <?php
            $select = mysqli_query($conn, "SELECT * FROM `user_form` WHERE id = '$user_id'") or die('query failed');
            if (mysqli_num_rows($select) > 0) {
               $fetch = mysqli_fetch_assoc($select);
            }
            ?>
            <div id class="text1">Id</div>
            <span class="box"><?php echo $fetch['id']; ?></span>
            <div id class="text2">Nama</div>
            <span class="box1"><?php echo $fetch['name']; ?></span>
            <div id class="text3">E-mail</div>
            <span class="box2"><?php echo $fetch['email']; ?></span>
         </div>
      </div>

   </div>
   <script src="script/java1.js"></script>
   <script src="https://cdn.rawgit.com/bungfrangki/efeksalju/2a7805c7/efek-salju-2.js" type="text/javascript"></script>
</body>

</html>