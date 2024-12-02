package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func Solve(fname string) {
	reports := ReadInput(fname)
	solution1 := Part1(reports)
	solution2 := Part2(reports)

	fmt.Printf("Part 1: %d\nPart 2: %d\n", solution1, solution2)
}

func check_report(report []int) int {
	diff := report[1] - report[0]
	if diff > 3 || diff < -3 || diff == 0 {
		return 0
	}
	for level := 2; level < len(report); level++ {
		current_diff := report[level] - report[level-1]
		if current_diff > 3 || current_diff < -3 || current_diff == 0 || diff*current_diff < 0 {
			return 0
		}
		diff = current_diff
	}
	return 1
}

func Part1(reports [][]int) int {
	safe_report_counter := 0
	for _, report := range reports {
		safe_report := check_report(report)
		safe_report_counter += safe_report
	}
	return safe_report_counter
}

func Part2(reports [][]int) int {
	safe_report_counter := 0
	for _, report := range reports {
		safe_report := check_report(report)
		if safe_report == 0 {
			fmt.Println("---")
			for level := range report {
				new_report := append([]int{}, report...)
				new_report = append(new_report[:level], new_report[level+1:]...)
				fmt.Println(report, new_report)
				safe_report = check_report(new_report)
				if safe_report > 0 {
					safe_report = 1
					break
				}
			}
		}
		safe_report_counter += safe_report
	}
	return safe_report_counter
}

func ReadInput(fname string) [][]int {
	file, err := os.Open(fname)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var reports [][]int
	var report []int

	scan := bufio.NewScanner(file)
	for scan.Scan() {
		string_line := strings.Fields(scan.Text())
		report = make([]int, 0)
		for _, part := range string_line {
			num, err := strconv.Atoi(strings.TrimSpace(part))
			if err != nil {
				fmt.Printf("Error converting %s to int: %v\n", part, err)
				continue
			}
			report = append(report, num)
		}
		reports = append(reports, report)
	}

	return reports
}

func main() {
	path, _ := os.Getwd()
	filepath := path + "/input.txt"
	Solve(filepath)
}
