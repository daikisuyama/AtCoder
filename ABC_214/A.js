// 21:19~
// inputに入力データ全体が入る
function Main(input) {
    // 1行目がinput[0], 2行目がinput[1], …に入る
    input = input.split("\n");
    let n= parseInt(input[0],10);
    if(1<=n && n<=125){
        console.log(4);
    }else if(126<=n && n<=211){
        console.log(6);
    }else{
        console.log(8);
    }
}

//標準入出力から一度に読み込み、Mainを呼び出す
Main(require("fs").readFileSync("/dev/stdin", "utf8"));