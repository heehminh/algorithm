#include <bits/stdc++.h>
using namespace std;

int main() { 
	int N;                                
	string word;                          
	int count = 0;                        

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> word;
        
		
		bool alphabet[26] = { false, };        
		alphabet[(int)(word[0]) - 97] = true;  

		for (int i = 1; i < word.size(); i++) {
        
			
			if (word[i] == word[i - 1]) {
				continue;
			}
            
			
			else if(word[i] != word[i - 1] 
            		&& alphabet[(int)(word[i]) - 97] == true){
				count++;	
				break;
			}
            
			
			else {
				alphabet[(int)(word[i]) - 97] = true;
			}
		}
	}

	
	cout << N - count;

	return 0;
}

// 아스킷 코드 사용 
// a: 97