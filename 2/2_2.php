<?php
declare(strict_types=1);

$forw = 0;
$aim = 0;
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

        switch ($direction) {
            case "down":
                $aim += $amt;
                break;
            case "up":
                $aim -= $amt;
                break;
            case "forward":
                $forw += $amt;
                $depthIncrease = $amt * $aim;
                $depth += $depthIncrease;
        }
    }
    fclose($fh);
}
var_dump($forw * $depth);
