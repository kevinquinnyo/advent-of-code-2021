package main

import (
	"os"
	"fmt"
	"bufio"
	"strconv"
)

func sum(a []int) int {
	res := 0
	for _, v := range a {
		res += v
	}

	return res
}

func main() {
	var count int = 0
	var prev []int
	var stack []int

	file, err := os.Open("data.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		n, _ := strconv.Atoi(scanner.Text())
		stack = append(stack, n)

		for len(stack) == 3 {
			if (len(prev) != 0 && sum(stack) > sum(prev)) {
				count++
			}

			prev = stack
			stack = stack[1:] // pop first item off
		}
	}

	fmt.Println(count)
}
