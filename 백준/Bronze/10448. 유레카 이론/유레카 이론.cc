#include <bits/stdc++.h>

using namespace std;

vector<int> eureka;
int N, test_case, total;

// 1000 이하의 삼각수 계산
void preCalculate(void) {
    N = 1;

    while (N * (N + 1) / 2 < 1000) {
        eureka.push_back(N * (N + 1) / 2);
        N++;
    }
}

// 삼각수 세개로 만들 수 있는 숫자인지 판별
bool triangleSum(int total) {
    for (int i = 0; i < eureka.size(); i++) {
        for (int j = 0; j < eureka.size(); j++) {
            for (int k = 0; k < eureka.size(); k++) {
                if (eureka[i] + eureka[j] + eureka[k] == total) {
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    cin >> test_case;
    preCalculate();

    for (int i = 0; i < test_case; i++) {
        cin >> total;

        cout << triangleSum(total) << "\n";
    }

    return 0;
}
