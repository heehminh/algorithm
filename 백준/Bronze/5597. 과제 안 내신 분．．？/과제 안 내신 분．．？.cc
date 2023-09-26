#include <bits/stdc++.h>
using namespace std;

int student;

int main() {
	// 30명, 2명이 제출안함 
	
	int arr[31] = { 0, };
	
	for (int i=0; i<28; i++) {
		cin >> student;
		arr[student] = 1;
	}
	
	for (int i=1; i<31; i++) {
		if (arr[i]==0) {
			cout << i << "\n";
		}
	}
	
	return 0;
}