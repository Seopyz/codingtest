from random import randint
import time
#배열에 10000개의 정수 삽입
array = []
for _ in range(10000):
    #1부터 100까지 랜덤한 정수
    array.append(randint(1, 100))

#선택정렬 프로그램 성능 측정
start_time = time.time()

#선택정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[min_index], array[i] = array[i], array[min_index]

end_time = time.time()
print("선택정렬 성능측정 : ", end_time - start_time)

array = []
for _ in range(10000):
    array.append(randint(1, 100))
start_time = time.time()
array.sort()
end_time = time.time()
print("기본라이브러리 정렬 성능측정 : ", end_time - start_time)