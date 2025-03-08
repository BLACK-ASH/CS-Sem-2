<?php
$num = 1234;
echo "Number: $num";
$reverse = 0;
while($num > 0) {
    $reminder = $num % 10;
    $reverse = $reverse * 10 + $reminder;
    $num = (int)($num / 10);
}
echo "<br>Reverse Number: $reverse";
?>