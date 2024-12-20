package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func isSafe(s []int) bool {
	if len(s) <= 1 {
		return true
	}

	isAsen := true
	if s[0] > s[1] {
		isAsen = false
	}

	i := 0

	for i+1 < len(s) {

		if isAsen {

			r := s[i+1] - s[i]

			if !(0 < r && r <= 3) {
				return false
			}

		} else {

			r := s[i] - s[i+1]

			if !(0 < r && r <= 3) {
				return false
			}

		}

		i += 1
	}

	return true
}

func isSafe2(s []int) bool {
	if len(s) <= 1 {
		return true
	}

	isAsen := true
	if s[0] > s[1] {
		isAsen = false
	}

	i := 0

	// remove single occrance
	for i+1 < len(s) {

		if isAsen {

			if s[i] >= s[i+1] {
				s = append(s[:i+1], s[i+2:]...)
				break
			}

		} else {

			if s[i] <= s[i+1] {
				s = append(s[:i+1], s[i+2:]...)
				break
			}

		}

		i += 1

	}

	c := 0

	i = 0

	for i+1 < len(s) {

		if isAsen {

			r := s[i+1] - s[i]

			if !(0 < r && r <= 3) {
				return false
			}

		} else {

			// if s[i+1] >= s[i] {
			// 	c += 1
			// 	i += 1
			// 	continue
			// }

			r := s[i] - s[i+1]

			if !(0 < r && r <= 3) {
				return false
			}

		}

		i += 1
	}

	return c <= 1
}

func main() {

	inputFile, err := os.Open("./input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer inputFile.Close()

	scanner := bufio.NewScanner(inputFile)

	scanner.Split(bufio.ScanLines)

	c := 0

	for scanner.Scan() {
		s := strings.Split(scanner.Text(), " ")

		i := []int{}

		for _, v := range s {
			iv, _ := strconv.Atoi(v) // handel err
			i = append(i, iv)
		}

		if isSafe2(i) {
			c += 1
		}

	}

	fmt.Println(c)

}
