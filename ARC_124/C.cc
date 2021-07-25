//嘘解法です、参考にしないでください

//Codeforcesで128bit整数を使いたいとき
//→__int128_tを使う&GNU C++17 (64)で提出する

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

//イテレーション
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
#define FORA(i,I) for(const auto& i:I)
//x:コンテナ
#define ALL(x) x.begin(),x.end() 
#define SIZE(x) ll(x.size()) 
//定数
#define INF32 2147483647 //2.147483647×10^{9}:32bit整数のinf
#define INF64 9223372036854775807 //9.223372036854775807×10^{18}:64bit整数のinf
#define MOD 1000000007 //問題による
//略記
#define F first
#define S second
//出力(空白区切りで昇順に)
#define coutALL(x) for(auto i=x.begin();i!=--x.end();i++)cout<<*i<<" ";cout<<*--x.end()<<endl;

//aをbで割る時の繰上げ,繰り下げ
ll myceil(ll a,ll b){return (a+(b-1))/b;}
ll myfloor(ll a,ll b){return a/b;}

signed main(){
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n;
    ll x,y;cin>>x>>y;
    deque<pair<ll,ll>> now;
    now.push_back({x,y});
    REP(i,n-1){
        ll a,b;cin>>a>>b;
        REP(i,SIZE(now)){
            ll x=now.front().F;
            ll y=now.front().S;
            now.pop_front();
            ll l1=lcm(gcd(x,a),gcd(y,b));
            ll l2=lcm(gcd(x,b),gcd(y,a));
            if(l1>l2){
                x=gcd(x,a);
                y=gcd(y,b);
                now.push_back({x,y});
            }else if(l1<l2){
                x=gcd(x,b);
                y=gcd(y,a);
                now.push_back({x,y});
            }else{
                ll x1,x2,y1,y2;
                x1=gcd(x,a);
                y1=gcd(y,b);
                x2=gcd(x,b);
                y2=gcd(y,a);
                if(x1==x2 && y1==y2){
                    now.push_back({x1,y1});
                }else{
                    now.push_back({x1,y1});
                    now.push_back({x2,y2});
                }
            }
        }
    }
    ll ans=0;
    FORA(i,now){
        if(lcm(i.F,i.S)>ans){
            ans=lcm(i.F,i.S);
        }
    }
    cout<<ans<<endl;
}