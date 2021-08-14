// inputに入力データ全体が入る
function Main(input) {
    // 1行目がinput[0], 2行目がinput[1], …に入る
    input = input.split("\n");
    let s,t;[s,t]=input[0].split(" ").map((x)=>parseInt(x,10));
    let ans=0;
    for(let a=0;a<=s;a++){
        for(let b=0;b<=s;b++){
            for(let c=0;c<=s;c++){
                if(a+b+c<=s && a*b*c<=t){
                    ans++;
                }
            }
        }
    }
    console.log(ans);
}

//標準入出力から一度に読み込み、Mainを呼び出す
Main(require("fs").readFileSync("/dev/stdin", "utf8"));