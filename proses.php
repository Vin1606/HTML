<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puskesmas Sejahtera I Rincian Pendaftaran</title>
    <link rel="stylesheet" type="text/css" href="css/proses.css">
    <link rel="icon" href="logo-title.png" style="width: 100px;">
    <link rel="stylesheet" type="text/css" href="https://cdn.prinsh.com/NathanPrinsley-textstyle/nprinsh-stext.css"/>
</head>
<body>
    <div class="background-header">
        <div class="header">
            <span class="nprinsley-text-rainbowan">Rincian Pendaftaran</span>
        </div>
    </div>
    <div class="background-pendaftaran">
        <div class="background-data-pendaftaran" style="padding: 20px 30px; font-size: 25px; background-color:darkslategray ; width: 700px; border: 3px solid orange; font-family: 'Times New Roman', Times, serif; color:white; border-radius: 20px;">
            <div class="background-data_diri-text">
                <span style="font-size: 30px; font-weight: bold;">Data Diri Anda</span>
            </div>
            <div class="background-data_diri" style="text-align: left; padding: 20px 0; font-size: 25px;">
            <span>Kode Pendaftaran : <input type="text" id="code" style="font-size:20px; background: none; border: none; color: white;" readonly><br>
                <?php 
                    $nama = $_POST["nama"];
                    $umur = $_POST["umur"];
                    $jk = $_POST["jenis-kelamin"];
                    $alamat = $_POST["alamat"];
                    $telpon = $_POST["telpon"];
                    $menu_pelayanan = $_POST["menu_pelayanan"];
                    $tgl = $_POST["date"];
                    $pesan = $_POST["pesan"];
                    if (!empty($nama))
                        echo("Nama : $nama <br>");
                    if (!empty($umur))
                        echo("Umur : $umur <br>");
                    if (!empty($jk))
                        echo("Jenis Kelamin : $jk <br>");
                    if (!empty($alamat))
                        echo("Alamat : $alamat <br>");
                    if (!empty($telpon))
                        echo("No. Telpon : $telpon <br>");
                    if (!empty($menu_pelayanan))
                        echo("Pelayanan : $menu_pelayanan <br>");
                    if (!empty($tgl))
                        echo("Tgl Pelayanan : $tgl <br>");
                    if (!empty($pesan))
                        echo("Komentar : $pesan <br>");
                ?>
            </div>
        </div>
        <div class="background-kalimat-peringatan">
            <div class="kalimat-peringatan">
                <span>Periksa Data Anda Kembali, Jika Ada Kesalahan Mohon Klik Tombol Dibawah Ini</span>
                <div class="background-daftar-ulang">
                    <a href="layanan.html">Registrasi Ulang</a>   
                </div>
            </div>
        </div>
    </div>
    <div class="background-text">
        <div class="background-text-body">
            <span class="nprinsley-text-glitchan">Tunjukkan Kode Pendaftaran Untuk Mendapatkan Nomor Antrian</span>
            <span class="nprinsley-text-glitchan">Screenshoot Halaman Ini</span>
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
    // Fungsi untuk menghasilkan kode otomatis
    function generateCode() {
        // Menghasilkan angka acak antara 100000 dan 999999
        var code = Math.floor(10000 + Math.random() * 20000);
        return code;
    }

    // Menampilkan kode otomatis di elemen input
    document.getElementById('code').value = generateCode();
</script>
</body>
</html>

