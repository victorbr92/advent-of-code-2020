package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

func Solve(fname string) {
	c1, c2 := ReadInput(fname)
	solution1 := Part1(c1, c2)
	solution2 := Part2(c1, c2)

	fmt.Printf("Part 1: %d\nPart 2: %d\n", solution1, solution2)
}

func Part1(c1 []int, c2 []int) int {
	diff := 0
	for idx, val1 := range c1 {
		val2 := c2[idx]
		local_diff := val1 - val2
		if local_diff < 0 {
			diff += -local_diff
		} else {
			diff += local_diff
		}
		// fmt.Println(val1, val2, local_diff)
	}
	return diff
}

func get_counter(s []int) map[int]int {
	count := make(map[int]int)
	for _, val := range s {
		count[val] += 1
	}
	return count
}

func Part2(c1 []int, c2 []int) int {
	counter := get_counter(c2)
	sum := 0
	for _, val := range c1 {
		sum += val * counter[val]
	}
	return sum
}

func ReadInput(fname string) ([]int, []int) {
	file, err := os.Open(fname)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var c1 []int
	var c2 []int

	scan := bufio.NewScanner(file)
	for scan.Scan() {
		r := strings.Split(scan.Text(), "   ")
		i, _ := strconv.Atoi(r[0])
		j, _ := strconv.Atoi(r[1])
		c1 = append(c1, i)
		c2 = append(c2, j)
	}
	slices.Sort(c1)
	slices.Sort(c2)

	return c1, c2
}

func main() {
	path, _ := os.Getwd()
	filepath := path + "/day_1/input.txt"
	Solve(filepath)
}
