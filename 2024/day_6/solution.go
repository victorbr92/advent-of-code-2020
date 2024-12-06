package main

import (
	"bufio"
	"fmt"
	"os"
	"sync"
	"time"
)

// rune -> arrays
var DIRECTIONS = map[rune][2]int{
	'^': {-1, 0},
	'>': {0, 1},
	'v': {1, 0},
	'<': {0, -1},
}

// arrays -> arrays
var CHANGE = map[[2]int][2]int{
	{-1, 0}: {0, 1},
	{0, 1}:  {1, 0},
	{1, 0}:  {0, -1},
	{0, -1}: {-1, 0},
}

func execute_route(grid [][]rune, current_row, current_col int, direction [2]int) int {
	positions := make(map[[2]int]struct{})
	positions_dir := make(map[[4]int]struct{})

	pos := [2]int{current_row, current_col}
	positions[pos] = struct{}{}
	positions_dir[[4]int{current_row, current_col, direction[0], direction[1]}] = struct{}{}

	for {
		// Move to the next position
		current_row += direction[0]
		current_col += direction[1]

		// Check if we left the map
		if current_col < 0 || current_col >= len(grid[0]) || current_row < 0 || current_row >= len(grid) {
			break
		}

		elem := grid[current_row][current_col]
		if elem == '#' {
			// Backtrack and change direction
			current_row -= direction[0]
			current_col -= direction[1]
			direction = CHANGE[direction]
		} else {
			// Track visited positions with directions
			_, ok := positions_dir[[4]int{current_row, current_col, direction[0], direction[1]}]
			// If the key exists
			if ok {
				return -1
			}
			positions_dir[[4]int{current_row, current_col, direction[0], direction[1]}] = struct{}{}
			positions[[2]int{current_row, current_col}] = struct{}{}
		}
	}

	return len(positions)
}

func read() [][]rune {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil
	}
	defer file.Close()

	var grid [][]rune
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		grid = append(grid, []rune(line))
	}

	return grid
}

func main() {
	grid := read()

	var current_row, current_col int
	var direction [2]int
	for row := 0; row < len(grid); row++ {
		for col := 0; col < len(grid[0]); col++ {
			elem := grid[row][col]
			if _, ok := DIRECTIONS[elem]; ok {
				current_row, current_col = row, col
				direction = DIRECTIONS[elem]
				break
			}
		}
	}

	start := time.Now()
	visited := execute_route(grid, current_row, current_col, direction)
	fmt.Printf("Unique Positions Visited: %d. Solved in %.3fs\n", visited, time.Since(start).Seconds())

	// Brute Force all the way with goroutines
	start = time.Now()
	loopPositions := 0
	var wg sync.WaitGroup
	resultChan := make(chan int, len(grid)*len(grid[0]))

	for row := 0; row < len(grid); row++ {
		for col := 0; col < len(grid[0]); col++ {
			if grid[row][col] == '.' {
				wg.Add(1)
				go func(r, c int) {
					defer wg.Done()

					grid_copy := make([][]rune, len(grid))
					for i := range grid {
						grid_copy[i] = make([]rune, len(grid[i]))
						copy(grid_copy[i], grid[i])
					}
					grid_copy[r][c] = '#'
					visited := execute_route(grid_copy, current_row, current_col, direction)
					if visited == -1 {
						resultChan <- 1
					} else {
						resultChan <- 0
					}
				}(row, col)
			}
		}
	}

	wg.Wait()
	close(resultChan)

	for result := range resultChan {
		loopPositions += result
	}

	fmt.Printf("Loop Positions: %d. Solved in %.3fs\n", loopPositions, time.Since(start).Seconds())
}
