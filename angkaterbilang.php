<?php
error_reporting(E_ALL ^ E_NOTICE);

function terbilang($x)
{
    $bil = array("", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan");
    if ($x < 10)
        return " " . $bil[$x];
    elseif ($x < 100)
        return terbilang($x / 10) . " puluh" . terbilang($x % 10);
    elseif ($x < 1000)
        return terbilang($x / 100) . " ratus" . terbilang($x % 100);
    elseif ($x < 1000000)
        return terbilang($x / 1000) . " ribu" . terbilang($x % 1000);
    elseif ($x < 1000000000)
        return terbilang($x / 1000000) . " juta" . terbilang($x % 1000000);
    elseif ($x < 1000000000000)
        return terbilang($x / 1000000000) . " miliar" . terbilang($x % 1000000000);
    elseif ($x < 1000000000000000)
        return terbilang($x / 1000000000000) . " triliun" . terbilang($x % 1000000000000);
}

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terbilang</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }

        h1 {
            color: #333;
            margin-bottom: 20px;
        }

        input[type="text"],
        input[type="submit"],
        .clear-btn {
            padding: 10px 20px;
            margin-bottom: 20px;
            width: 100%;
            box-sizing: border-box;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        input[type="text"] {
            border: 1px solid #ccc;
            margin-bottom: 10px;
            outline: none;
        }

        input[type="submit"] {
            background-color: #1e88e5;
            color: #fff;
            transition: background-color 0.3s ease;
        }

        input[type="submit"]:hover {
            background-color: #0d47a1;
        }

        .clear-btn {
            background-color: #ccc;
            color: #333;
            transition: background-color 0.3s ease;
        }

        .clear-btn:hover {
            background-color: #999;
        }

        b {
            color: #1e88e5;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Konversi Angka ke Terbilang</h1>
        <form id="form" action="" method="get" onsubmit="return validateInput()">
            <input id="angkaInput" type="text" name="angka" placeholder="Masukkan angka...">
            <br>
            <input type="submit" value="Tampilkan">
            <br>
            <button type="button" class="clear-btn" onclick="clearInput()">Clear</button>
        </form>
        <?php if ($_GET['angka']) : ?>
            <p id="result">Hasil: <b><?php echo terbilang($_GET['angka']); ?></b></p>
        <?php endif; ?>
    </div>

    <script>
        function validateInput() {
            var angka = document.getElementById("angkaInput").value;
            if (isNaN(angka) || angka == "" || angka == 0) {
                alert("Masukkan angka yang valid (tidak boleh kosong atau nol)");
                return false;
            }
            return true;
        }

        function clearInput() {
            document.getElementById('angkaInput').value = '';
            document.getElementById('result').style.display = 'none';
        }

        setTimeout(function() {
            document.getElementById('result').style.display = 'none';
        }, 10000);
    </script>
</body>

</html>
