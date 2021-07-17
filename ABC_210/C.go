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
	var n, k int
	fmt.Fscan(scin, &n, &k)
	c := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(scin, &c[i])
	}
	check := make(map[int]int)
	for i := 0; i < k; i++ {
		check[c[i]]++
	}
	ans := len(check)
	now := len(check)
	for i := 0; i < n-k; i++ {
		check[c[i]]--
		if check[c[i]] == 0 {
			now--
		}
		check[c[i+k]]++
		if check[c[i+k]] == 1 {
			now++
		}
		if ans < now {
			ans = now
		}
	}
	fmt.Fprintln(prout, ans)
}
