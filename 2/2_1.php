<?php
declare(strict_types=1);

$horiz = 0;
$depth = 0;

$fh = fopen('data.txt', 'r');
if ($fh) {
    while (!feof($fh)) {
        $line = fgets($fh);
        $n = $line ? trim($line) : null;
        if ($n === null) {
            continue;
        }

        [$direction, $amt] = explode(' ', $line);
        $amt = (int)$amt;

        if ($direction === 'forward') {
            $horiz += $amt;
            continue;
        }

        if ($direction === 'up') {
            $amt *= -1;
        }

        $depth += $amt;
    }
    fclose($fh);
}
var_dump($horiz * $depth);
