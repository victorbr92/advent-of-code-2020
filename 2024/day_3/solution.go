package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func Solve(fname string) {
	instruction := ReadInput(fname)
	solution1 := Part1(instruction)
	solution2 := Part2(instruction)

	fmt.Printf("Part 1: %d\nPart 2: %d\n", solution1, solution2)
}

func find_mult(instruction string) int {
	re := regexp.MustCompile(`mul\(\d{1,5},\d{1,5}\)`)
	matches := re.FindAllString(instruction, -1)

	re_numbers := regexp.MustCompile(`\d+`)

	var total int
	for _, match := range matches {
		// fmt.Println(match)
		numbers := re_numbers.FindAllString(match, -1)
		mul := 1
		for _, number := range numbers {
			num, _ := strconv.Atoi(number)
			mul *= num
		}
		total += mul
	}
	return total
}

func Part1(instruction string) int {
	total := find_mult(instruction)
	return total
}

func Part2(instruction string) int {
	safe_report_counter := 0

	re := regexp.MustCompile(`(do\(\)|don't\(\))`)
	matches := re.FindAllStringIndex(instruction, -1)
	last_index := 0
	consider := true

	for _, match := range matches {
		last_text := instruction[last_index:match[0]]
		next_instruction := instruction[match[0]:match[1]]
		fmt.Println(last_index, match[0], next_instruction)

		if consider {
			// fmt.Println(last_text)
			// fmt.Println()
			current := find_mult(last_text)
			safe_report_counter += current
		}
		if next_instruction == "do()" {
			consider = true
		} else {
			consider = false
		}
		last_index = match[1]
	}

	return safe_report_counter
}

func ReadInput(fname string) string {
	file, err := os.Open(fname)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scan := bufio.NewScanner(file)

	var full_string string
	for scan.Scan() {
		full_string += scan.Text()
	}

	return full_string
}

func main() {
	path, _ := os.Getwd()
	filepath := path + "/input.txt"
	Solve(filepath)
}
