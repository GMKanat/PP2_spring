#include <bits/stdc++.h>
using namespace std;
vector<int> subset;
int n;
vector<int> v;
void search(int k){
	if(k == n + 1){
		for(int i = 0; i < (int)subset.size(); i++){
			cout << v[i] << " ";
		}
		cout << "\n";
	}
	else{
		subset.push_back(k);
		search(k + 1);
		subset.pop_back();
		search(k + 1);
	}
}


int main(){
	ios::sync_with_stdio(0); 
	cin.tie(0); 
	
	cin >> n;
	v.resize(n);
	for(int i = 0; i < n; i++){
		cin >> v[i];
	}


	search(1);

}