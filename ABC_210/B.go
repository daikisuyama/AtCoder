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
	var n int
	fmt.Fscan(scin, &n)
	var s string
	fmt.Fscan(scin, &s)
	for i := 0; i < n; i++ {
		if s[i] == '1' {
			var t string
			if i%2 == 0 {
				t = "Takahashi"
			} else {
				t = "Aoki"
			}
			fmt.Fprintln(prout, t)
			break
		}
	}
}
