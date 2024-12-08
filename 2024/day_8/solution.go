package main

import (
	"bufio"
	"fmt"
	"os"
)

type Point struct {
	row, col int
}

func (p Point) is_inside_grid(grid []string) bool {
	return p.row >= 0 && p.col >= 0 && p.row < len(grid) && p.col < len(grid[0])
}

func read() []string {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil
	}
	defer file.Close()

	var grid []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		grid = append(grid, line)
	}

	return grid
}

func get_antennas(grid []string) map[rune][]Point {
	antennas := make(map[rune][]Point)
	for row, line := range grid {
		for col, s := range line {
			if s != '.' {
				value, ok := antennas[s]
				if ok {
					value = append(value, Point{row, col})
					antennas[s] = value
				} else {
					antennas[s] = []Point{{row, col}}
				}
			}
		}
	}
	return antennas
}

func get_antinodes(grid []string, ref Point, other Point) <-chan Point {
	ch := make(chan Point)

	go func() {
		defer close(ch)
		drow := ref.row - other.row
		dcol := ref.col - other.col

		i := 1
		for {
			an := Point{ref.row + drow*i, ref.col + dcol*i}
			if an.is_inside_grid(grid) {
				ch <- an // Send the value to the channel
			} else {
				break
			}
			i++
		}
	}()

	return ch
}

func main() {
	grid := read()

	antennas := get_antennas(grid)
	antinodes := make(map[Point]struct{})

	for antenna_type := range antennas {
		antenna_list := antennas[antenna_type]
		for _, ref := range antenna_list {
			for _, other := range antenna_list {
				if ref != other {
					for an := range get_antinodes(grid, ref, other) { // Range over the channel
						antinodes[an] = struct{}{}
						break
					}
				}
			}
		}
	}
	fmt.Printf("First Part: Antinodes: %d\n", len(antinodes))
	fmt.Println("----------------------------------------------")

	for antenna_type := range antennas {
		antenna_list := antennas[antenna_type]
		for _, ref := range antenna_list {
			antinodes[ref] = struct{}{}
			for _, other := range antenna_list {
				antinodes[other] = struct{}{}
				if ref != other {
					for an := range get_antinodes(grid, ref, other) { // Range over the channel
						antinodes[an] = struct{}{}
					}
				}
			}
		}
	}
	fmt.Printf("Second Part: Antinodes: %d\n", len(antinodes))
}
