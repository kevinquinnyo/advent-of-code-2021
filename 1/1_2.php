<?php
declare(strict_types=1);

$count = 0;
$prev = [];
$stack = [];

$fh = fopen('data.txt', 'r');
if ($fh) {
    while (!feof($fh)) {
        $line = fgets($fh);
        $n = $line ? trim($line) : null;
        if ($n === null) {
            continue;
        }

        $stack[] = $n;

        while (count($stack) == 3) {
            if (array_sum($stack) > array_sum($prev)) {
                $count += 1;
            }

            $prev = $stack;
            array_shift($stack);
        }
    }

    fclose($fh);
}
var_dump($count);
