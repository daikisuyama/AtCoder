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
	var n, a, x, y int
	fmt.Fscan(scin, &n, &a, &x, &y)
	if n <= a {
		fmt.Fprintln(prout, n*x)
	} else {
		fmt.Fprintln(prout, a*x+(n-a)*y)
	}
}
