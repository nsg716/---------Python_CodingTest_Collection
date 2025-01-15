# Run Length Encoding
# 문자열 파싱 
# 파이썬 코드로 해결하기에 문제가 있는 코드 해당 코드는 조금 해결하기 힘든 케이스가 있음 
# 빈 문자열이 들어올 때, 공백일때 등등 경우의 수를 해결하기 힘든 경우가 많음 
# 해당 코드를 C++로 해결하였음.


#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
#include <string>

# using namespace std;
# int main()
# {
#     string line;
#     while (true)
#     {

#         if (cin.eof() == true)
#             break;
#         getline(cin, line);
#         for (string::iterator it = line.begin(); it != line.end(); )
#         {
#             int rep = 1;
#             while (rep < 9 && (it + rep) != line.end() && *it == *(it + rep))
#                 ++rep;
#             // A sequence of min(rep,9) identical characters starts at *it.
#             if (rep > 1)
#             {
#                 cout << rep << *it;
#                 it += rep;
#             }
#             else
#             {
#                 cout << 1;
#                 for (; it != line.end() && ((it + 1) == line.end() || *it != *(it + 1)); ++it)
#                 {
#                     cout << *it;
#                     if (*it == '1')
#                         cout << *it;
#                 }
#                 // Either a repetitive sequence begins at *it, or it reached the end of line.
#                 cout << 1;
#             }
#         }
#         cout << endl;
#     }
#     return 0;
# }


# 테스트 코드 (틀린 답)

# N = input()

# set_N = set(N)
# result = []

# for char in set_N:  # 고유 문자 집합에 대해 반복
#     count = N.count(char)  # 각 문자의 개수 세기
#     result.append(f"{count}{char}")  # 결과 리스트에 추가

# output = ''.join(result)  # 결과 리스트를 문자열로 변환
# print(output)  # 결과 출력
