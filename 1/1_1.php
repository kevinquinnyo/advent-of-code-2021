<?php
declare(strict_types=1);

$count = 0;
$last = null;
$fh = fopen('data.txt', 'r');
if ($fh) {
    while (!feof($fh)) {
        $line = fgets($fh);
        $n = $line ? trim($line) : null;

        if ($n && $last && $n > $last) {
            $count += 1;
        }

        $last = $n;
    }

    fclose($fh);
}
var_dump($count);
