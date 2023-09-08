#include <bits/stdc++.h>
using namespace std;
string s, temp;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	cin >> s;
	temp = s;
	reverse(temp.begin(), temp.end()); 
	if (temp == s) cout << 1 << "\n"; // 뒤집은 문자열과 원래 문자열이 같은지 
	else cout << 0 << "\n";
	
	return 0;
}