<?php
$stop = 100;
for ($i = 2; $i <= $stop; $i++) {
    $isPrime = true;
    for ($j = 2; $j < $i; $j++) {
        if ($i % $j == 0) {
            $isPrime = false;
            break;
        }
    }
    if ($isPrime) {
        echo "$i, ";
    }
}
?>