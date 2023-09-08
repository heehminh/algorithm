#include <bits/stdc++.h>
using namespace std;
int A, B, C, a, l, cnt[110], res;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	cin >> A >> B >> C;
	
	// 1. 트럭 (도착시간, 떠난시간) 입력받기
	for (int i=0; i<3; i++) {
		cin >> a >> l;
		for (int j=a; j<l; j++) {
			cnt[j]++;
		}
	}
	
	for (int i=0; i<110; i++) {
		if (cnt[i]==1) {
			res += cnt[i]*A;
		} else if (cnt[i]==2) {
			res += cnt[i]*B;
		} else {
			res += cnt[i]*C;
		}
	}
	
	cout << res;
	
	return 0;
}