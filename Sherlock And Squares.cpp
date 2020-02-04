#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int t,d,a,b,count;
    cin>>t;
    while(t--){
        cin>>a>>b;
        count=0;
        d=ceil(sqrt(a));
        while((d*d)<=b){
            count++;
            d++;
        }
        cout<<count<<endl;
    }
    
        return 0;
}

