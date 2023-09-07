// ** 알파벳의 개수: 26개  ** 
// ** 소문자 a의 아스키코드: 97 ** 

#include <bits/stdc++.h>
using namespace std;

string s;
int alphabet[26]; // 알파벳 개수를 담은 배열 

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	// 1. 소문자로만 이루어진 단어 입력 
	cin >> s;
	for (int i=0; i<s.size(); i++) {
		alphabet[s[i]-97]++;
	}
	
	// 2. 단어에 포함되어 있는 알파벳 개수 출력 
	for (int i : alphabet) {
		cout << i << " ";
	}
	
	return 0;
}