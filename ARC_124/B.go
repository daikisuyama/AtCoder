// 22:00~22:15
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	scin := bufio.NewReader(os.Stdin)
	prout := bufio.NewWriter(os.Stdout)
	defer prout.Flush()

	// code
	var n int
	fmt.Fscan(scin, &n)
	var a []int = make([]int, n)
	var b []int = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(scin, &a[i])
	}
	for i := 0; i < n; i++ {
		fmt.Fscan(scin, &b[i])
	}
	var y []int
	for i := 0; i < n; i++ {
		y = append(y, a[0]^b[i])
	}
	sort.Slice(y, func(i, j int) bool { return y[i] < y[j] })
	var ans []int
	for _, x := range y {
		var nowa []int = make([]int, n)
		var nowb []int = make([]int, n)
		copy(nowa, a)
		copy(nowb, b)
		for i := 0; i < n; i++ {
			nowa[i] ^= x
		}
		sort.Slice(nowa, func(i, j int) bool { return nowa[i] < nowa[j] })
		sort.Slice(nowb, func(i, j int) bool { return nowb[i] < nowb[j] })
		f := true
		for i := 0; i < n; i++ {
			if nowa[i] != nowb[i] {
				f = false
				break
			}
		}
		if f {
			if len(ans) == 0 {
				ans = append(ans, x)
			} else {
				if ans[len(ans)-1] != x {
					ans = append(ans, x)
				}
			}
		}
	}
	fmt.Fprintln(prout, len(ans))
	if len(ans) != 0 {
		for i := 0; i < len(ans); i++ {
			fmt.Fprintln(prout, ans[i])
		}
	}
}
