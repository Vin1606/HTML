<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puskesmas Sejahtera I Home</title>
    <link rel="stylesheet" type="text/css" href="css/login-home.css">
    <link rel="icon" href="gambar/logo-title.png" style="width: 100px;">
    <link rel="stylesheet" type="text/css" href="https://cdn.prinsh.com/NathanPrinsley-textstyle/nprinsh-stext.css"/>
</head>
<body>
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

    <div class="profile-login">
        <div class="kalimat">
            <div class= "box-profile">
                <span class="nprinsley-text-glitchan">Profile Anda</span>
            </div>
            <?php
            $select = mysqli_query($conn, "SELECT * FROM `user_form` WHERE id = '$user_id'") or die('query failed');
            if (mysqli_num_rows($select) > 0) {
                $fetch = mysqli_fetch_assoc($select);
            }
            ?>
            <div class="background-biodata">
                <div class="profile">
                    <?php
                        $select = mysqli_query($conn, "SELECT * FROM `user_form` WHERE id = '$user_id'") or die('query failed');
                            if (mysqli_num_rows($select) > 0) {
                        $fetch = mysqli_fetch_assoc($select);
                        }
                        if ($fetch['image'] == '') {
                            echo '<img src="images/default-avatar.png">';
                        }   
                        else {
                            echo '<img src="uploaded_img/' . $fetch['image'] . '">';
                        }
                    ?>
                </div>
                <div class="biodata">
                    <div id class="text1">
                        <span>ID : </span>
                        <span class="box"><?php echo $fetch['id']; ?></span>
                    </div>
                    <div id class="text2">
                        <span>Nama : </span>
                        <span class="box1"><?php echo $fetch['name']; ?></span>
                    </div>
                    <div id class="text3">
                        <span>E-mail : </span>
                        <span class="box2"><?php echo $fetch['email']; ?></span>
                    </div>
                </div>
            </div>
            <div class = "logout">
                <a href="profil.php?logout=<?php echo $user_id; ?>" class="logout-btn">Logout</a>
            </div>
        </div>
    </div>

    <div class="background-header">
        <div class="header">
            <div class="logo-header">
                <img src="gambar/logo.png" class="logo">
            </div>
            <div class="email">
                <i class="fa-solid fa-envelope logo-email"></i>
            </div>
            <div class="email-text">
                <span class="nprinsley-text-glitchan">Punya Pertanyaan ?</span>
                <span>puskesmas_sejahtera@gmail.com</span>
            </div>
            <div class="telpon">
                <i class="fa-solid fa-phone logo-telpon"></i>
            </div>
            <div class="telpon-text">
                <span class="nprinsley-text-glitchan">Telpon</span>
                <span>081311277841</span>
            </div>
        </div>
    </div>

    <nav class="navbar-background">
        <div class="navbar">
            <li><a href="home-login.php"><i class="fa-solid fa-house logo-rumah"></i>Home</a></li>
            <li><a href="pelayanan.html"><i class="fa-solid fa-bars logo-layanan"></i>Layanan</a></li>
            <li><a href="artikel.html"><i class="fa-solid fa-newspaper logo-artikel"></i>Artikel</a></li>
            <li><a href="#tentang-kami"><i class="fa-solid fa-address-card logo-tentang"></i>Tentang Kami</a></li>
        </div>
    </nav>

    <div class="background-gambar-slider">
        <div class="gambar-slider">
            <img src="gambar-1.jpg" id="slide">
        </div>
    </div>

    <div class="background-layanan-kami" id="tentang-kami">
        <div class="nprinsley-text-rainbowan tentang-kami-text">Tentang Kami</div>
    </div>

    <div class="background-informasi-puskesmas">
        <div class="isi-puskesmas">
            <img src="gambar/puskes.jpg">
        </div>

        <div class="text-puskesmas">
            <span class="informasi-puskesmas">Puskesmas Sejahtera merupakan puskesmas yang terletak di daerah kota Jakarta Timur yang dapat melayani Pasien Umum dan BPJS. Puskesmas Sejahtera merupakan puskesmas yang mengutamakan kesehatan masyarakat dan merupakan salah satu puskesmas yang tidak mencari keuntungan, oleh sebab itu kami selalu sedia menangani keluhan ataupun penyakit yang dialami oleh pasien tanpa memandang mereka kaya ataupun miskin. Selain itu Puskesmas Sejahtera memberikan pelayanan kesehatan yang berkualitas dan efektif untuk memberikan nilai terbaik, sehingga menjadi pilihan utama bagi semua masyarakat dan perusahaan.</span>
            <div class="background-icon-atas">
                <div class="background-logo-icon-waktu">
                    <i class="fa-solid fa-clock logo-waktu"></i>
                    <div class="text-layanan">
                        <span class="layanan24-text">Layanan 24 Jam</span>
                    </div>
                </div>
                <div class="background-logo-icon-orang">
                    <i class="fa-solid fa-person-dress logo-orang"></i>
                    <div class="text-layanan">
                        <span class="bersalin-text">Ruang Bersalin</span>
                    </div>
                </div>
                <div class="background-logo-icon-medical">
                    <i class="fa-solid fa-kit-medical logo-medical"></i>
                    <div class="text-layanan">
                        <span class="medical-text">Medical Check-Up</span>
                    </div>
                </div>
            </div>
            <div class="background-icon-bawah">
                <div class="background-logo-icon-bintang">
                    <i class="fa-solid fa-star logo-bintang"></i>
                    <div class="text-layanan">
                        <span class="medical-text">Pelayanan Terbaik</span>
                    </div>
                </div>
                <div class="background-logo-icon-obat">
                    <i class="fa-solid fa-tablets logo-obat"></i>
                    <div class="text-layanan">
                        <span class="medical-text">Obat Racikan</span>
                    </div>
                </div>
                <div class="background-logo-icon-money">
                    <i class="fa-solid fa-money-bill logo-uang"></i>
                    <div class="text-layanan">
                        <span class="medical-text">Harga Terjangkau</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class = "background-kontak-gawat-darurat">
        <div class="background-gawat-darurat">
            <div class="gawat-darurat-text">
                <span class="saat-text">Saat Gawat Darurat</span>
            </div>
        </div>
        <div class="background-peringatan">
            <div class="peringatan-text">
                <span class="ajakan-text">Kami Puskesmas Sejahtera Siap Melayani Dengan Sepenuh Hati, Jika Anda Dalam Situasi Gawat Darurat Segera Langsung</span>
            </div>
        </div>    
        <div class="background-kontak">
            <div class="kontak-text">
                <i class="fa-brands fa-whatsapp logo-wa"></i><a href="https://wa.me/6281311277841?text=Halo%2C%20saya%20ingin%20bertanya." target="_blank" class="wa-text">Hubungi saya di WhatsApp</a>
            </div>
        </div>
    </div>

    <div class="background-footer">
        <div class="footer-body">
            <div class="box-kontak">
                <span class>Alamat Kami</span>
                <div class="footer-keterangan-box">
                    <div class="box-alamat">
                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3966.27886678929!2d106.9043776756328!3d-6.22691609376115!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e69f34dd1b36197%3A0x1622bbc41baff09d!2sJl.%20Purbaya%20I%20No.18%2C%20RT.6%2FRW.6%2C%20Pd.%20Bambu%2C%20Kec.%20Duren%20Sawit%2C%20Kota%20Jakarta%20Timur%2C%20Daerah%20Khusus%20Ibukota%20Jakarta%2013430!5e0!3m2!1sid!2sid!4v1702697763000!5m2!1sid!2sid" width="250" height="200"  allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" class="maps"></iframe>
                        <span class="alamat">Jalan Purbaya 1 Nomor 18
                            RT.006 RW.006 Kelurahan Duren Sawit
                            Kecamatan Duren Sawit
                            Jakarta Timur</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="box-quick-menu">
                <span class="box-media-sosial">Quick Menu</span>
                <div class="background-footer-keterangan-quick_menu">
                    <div class="footer-keterangan-quick_menu">
                        <li><a href="home-login.php">Home</li></a>
                        <li><a href="artikel.html">Artikel</li></a>
                        <li><a href="pelayanan.html">Layanan</li></a>
                        <li><a href="visi misi.html">Visi Misi</li></a>
                    </div>
                </div>
            </div>
            <div class="background-footer-sosial">
                <div class="footer-sosial-media">
                    <span class="box-sosial-media">Media Sosial</span>
                    <div class="facebook-media">
                        <li><a href="https://www.facebook.com/?locale=id_ID" target="_blank"><i class="fa-brands fa-facebook-f logo-facebook"></i><span>Facebook</span></a></li>
                    </div>
                    <div class="twiter-media">
                        <li><a href="https://twitter.com/?lang=id" target="_blank"><i class="fa-brands fa-twitter logo-twiter"></i><span>Twitter</span></a></li>
                    </div>
                    <div class="instagram-media">
                        <li><a href="https://www.instagram.com/" target="_blank"><i class="fa-brands fa-instagram logo-instagram"></i><span>Instagram</span></a></li>
                    </div>
                    <div class="youtube-media">
                        <li><a href="https://www.youtube.com/" target="_blank"><i class="fa-brands fa-youtube logo-youtube"></i><span>Youtube</span></a></li>
                    </div>
                </div>
            </div>
        </div>
            </div>
        </div>
        <div class="background-copyright">
            <div class="copyright-text">2023 © PUSKESMAS SEJAHTERA ALL RIGHTS RESERVED.</div>
        </div>
    </div>
    <script src="https://kit.fontawesome.com/c2752fde40.js" crossorigin="anonymous"></script>
    <script>
        var images = ["gambar-1.jpg", "gambar-2.jpg"];
        var i = 0;
        
        function slide() {
            document.getElementById('slide').src = images[i];
            if(i < images.length - 1) {
                i++; 
            } 
            else { 
                i = 0;
            }
          setTimeout("slide()", 3000);
        }
        
        window.onload = slide;
    </script>
        
</body>
</html>