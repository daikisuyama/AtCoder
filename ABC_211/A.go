package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scin := bufio.NewReader(os.Stdin)
	prout := bufio.NewWriter(os.Stdout)
	defer prout.Flush()

	// code
	var a, b float64
	fmt.Fscan(scin, &a, &b)
	fmt.Println((a + 2*b) / 3)
}
