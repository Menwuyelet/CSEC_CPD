#include<iostream>
using namespace std;
int main(){
int n;
cin>>n;
while(n--){
    char s;
    cin>>s;
    if(s=='F'||s=='B'){
        cout<<"yes";

    }
    else if((s=='B'&&s=='B')&&(s=='F'||s=='F')){
        cout<<"no";
    }
    cout<<endl;
}
return 0;
}