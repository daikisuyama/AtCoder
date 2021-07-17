package main
import "fmt"

func main(){
	var x,y int
	fmt.Scan(&x,&y)
	s := map[int]struct{}{
		0: struct{}{},
		1: struct{}{},
		2: struct{}{},
	}
	delete(s,x)
	if x==y{
		fmt.Println(x)
	}else{
		delete(s,y)
		for ans,_ := range s{
			fmt.Println(ans)
		}
	}
}