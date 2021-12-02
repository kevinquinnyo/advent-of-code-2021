package main

import (
	"os"
	"fmt"
	"bufio"
	"strconv"
	"strings"
)

func main() {
	var forw int = 0
	var aim int = 0
	var depth int = 0
	var depth_increase int = 0

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
		if direction ==  "down" {
			aim += amt
			continue
		}

		if direction == "up" {
			aim -= amt
			continue
		}

		if direction == "forward" {
			forw += amt
			depth_increase = amt * aim
			depth += depth_increase
		}
	}

	fmt.Println(forw * depth)
}
