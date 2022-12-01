package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	counts := make([]int, 1000)

	elves := 0
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			elves++
		} else {
			num, _ := strconv.Atoi(line)
			counts[elves] += num
		}
	}

	sort.Sort(sort.Reverse(sort.IntSlice(counts)))

	sum_top_three := counts[0] + counts[1] + counts[2]

	fmt.Println(sum_top_three)
}
