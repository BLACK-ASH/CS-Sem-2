<?php
$num = 10;
for ($i = 1; $i <= $num; $i++) {
    $fatorial = 1;
    for ($j = 1; $j <= $i; $j++) {
        $fatorial *= $j;
    }
    echo "Fatorial Of $i Is: $fatorial<br>";
}
?>