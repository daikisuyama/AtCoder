// inputに入力データ全体が入る
function Main(input) {
    // 1行目がinput[0], 2行目がinput[1], …に入る
    input = input.split("\n");
    let a,b;[a,b]=input[0].split(" ");
    console.log(a^b)
}

//標準入出力から一度に読み込み、Mainを呼び出す
Main(require("fs").readFileSync("/dev/stdin", "utf8"));