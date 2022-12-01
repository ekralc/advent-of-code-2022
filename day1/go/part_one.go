package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	running_total := 0
	max_running_total := 0

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			if running_total > max_running_total {
				max_running_total = running_total
			}

			running_total = 0
		} else {
			num, _ := strconv.Atoi(line)
			running_total += num
		}
	}

	fmt.Println(max_running_total)
}
