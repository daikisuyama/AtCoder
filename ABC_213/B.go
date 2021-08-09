package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type x struct {
	c, d int
}

func main() {
	scin := bufio.NewReader(os.Stdin)
	prout := bufio.NewWriter(os.Stdout)
	defer prout.Flush()

	// code
	var n int
	fmt.Fscan(scin, &n)
	var a []x = make([]x, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(scin, &a[i].c)
		a[i].d = i + 1
	}
	sort.Slice(a, func(i, j int) bool { return a[i].c > a[j].c })
	fmt.Fprintln(prout, a[1].d)
}
