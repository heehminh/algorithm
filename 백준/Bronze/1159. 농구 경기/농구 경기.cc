#include <bits/stdc++.h>
using namespace std;
int N;
vector<string> players;
string player, key;
map<string, int> mp;
bool isSelect;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	isSelect = false; 
	cin >> N;
	for (int i=0; i<N; i++) {
		cin >> player;
		players.push_back(player);
	}
	
	for(int i=0; i<N; i++) {
		// key의 맨 앞 한글자만 따서 mp 에 넣기 
		// value +1 
		key = players[i].substr(0, 1);
		if (mp.find(key) != mp.end()) {
			mp[key]++;
		} else {
			mp[key] = 1;
		}
	}
	
	
	for(auto it=mp.begin(); it != mp.end(); it++) {
		if (it->second > 4) {
			cout << it->first;
			isSelect=true;
		} 
	}
	
	if(isSelect==false) {
		cout << "PREDAJA";
	}
	// PREDAJA
	
	return 0;
}