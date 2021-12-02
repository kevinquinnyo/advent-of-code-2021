package main

import (
	"os"
	"fmt"
	"bufio"
	"strconv"
)

func main() {
	var count int = 0
	var last int = -1 // FIXME: learn a more idiomatic golang way to do this

	file, err := os.Open("data.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		n, _ := strconv.Atoi(scanner.Text())

		if (last != -1 && n > last) {
			count++
		}

		last = n
	}

	fmt.Println(count)
}
