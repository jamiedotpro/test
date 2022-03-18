입력 데이터는 텍스트 파일을 통해 읽어옴  

문제의 조건에 따라 첫번째 그룹의 더한 값을 짝수로 하기 위해  
첫번째 숫자를 포함하는 짝수 그룹을 먼저 생성  
짝수 그룹에 이어서 생성될 홀수 그룹을 생성  
위의 과정을 반복하여, 더이상 그룹이 추가되지 않으면 짝수홀수그룹 생성 완료  
숫자의 인덱스를 키로 하는 딕셔너리에 그룹을 저장함  
even_num:  {0: [[11, 2, 17], [11, 2, 17, 13, 1], [11, 2, 17, 13, 1, 15, 3]], 4: [[1, 15]]}  
odd_num:   {3: [[13], [13, 1, 15]], 5: [[15]], 6: [[3]]}  

조건을 만족하는 그룹의 수를 세기 위해  
첫 짝수그룹 이후에 다음 그룹들을 리스트에 넣어서 반복  
마지막 숫자가 포함된 그룹까지 짝수홀수 조건을 만족한 것을 확인하면  
그룹 수를 키로 가지는 딕셔너리에 카운트 증가 처리  
리턴되는 값은 키의 최대값(그룹의 수).  

두번째 테스트 셋의 결과값은 5.  
시작을 짝수그룹으로 하려면 생성되는 첫 그룹은 아래의 3개.  
[11, 2, 17], [11, 2, 17, 13, 1], [11, 2, 17, 13, 1, 15, 3]  

11, 2, 17 | 13 | 1, 15 | 3 -> 4개의 그룹  
11, 2, 17, 13, 1 | 15 | 3 (x 마지막 숫자가 짝수 아님)  
11, 2, 17, 13, 1, 15, 3 -> 1개의 짝수그룹  
이어서 그룹의 수가 가장 많은 4로 출력함.  
