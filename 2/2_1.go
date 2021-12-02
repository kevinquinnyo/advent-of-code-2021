package main

import (
	"os"
	"fmt"
	"bufio"
	"strconv"
	"strings"
)

func main() {
	var horiz int = 0
	var depth int = 0

	file, err := os.Open("data.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		direction := fields[0]
		amt, _ := strconv.Atoi(fields[1])
		if direction ==  "forward" {
			horiz += amt
			continue
		}

		if direction == "up" {
			amt *= -1
		}

		depth += amt
	}

	fmt.Println(horiz * depth)
}
