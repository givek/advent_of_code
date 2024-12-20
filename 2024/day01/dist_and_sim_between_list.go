package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

// var l1 = []int{
// 	3,
// 	4,
// 	2,
// 	1,
// 	3,
// 	3,
// }
//
// var l2 = []int{
// 	4,
// 	3,
// 	5,
// 	3,
// 	9,
// 	3,
// }

func distBetweenLists(l1 []int64, l2 []int64) int64 {
	slices.Sort(l1)
	slices.Sort(l2)

	dist := int64(0)

	for i := range len(l1) {
		dist += int64(math.Abs(float64(l1[i] - l2[i])))
	}

	return dist
}

func count(s []int64, n int64) int64 {
	count := int64(0)

	for _, v := range s {
		if v == n {
			count += 1
		}
	}

	return count
}

func similarityBetweenLists(l1 []int64, l2 []int64) int64 {
	simScr := int64(0)

	for _, v := range l1 {
		c := count(l2, v)

		simScr += c * v
	}

	return simScr
}

func main() {

	inputFile, err := os.Open("./input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer inputFile.Close()

	scanner := bufio.NewScanner(inputFile)

	scanner.Split(bufio.ScanLines)

	l1 := []int64{}
	l2 := []int64{}

	for scanner.Scan() {
		s := strings.Split(scanner.Text(), "   ")

		s1, _ := strconv.Atoi(strings.TrimSpace(s[0])) // handle err
		s2, _ := strconv.Atoi(strings.TrimSpace(s[1])) // handle err

		l1 = append(l1, int64(s1))
		l2 = append(l2, int64(s2))
	}

	fmt.Println(distBetweenLists(l1, l2))

	fmt.Println(similarityBetweenLists(l1, l2))
}
