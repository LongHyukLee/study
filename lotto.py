# 실습3. 로또번호추천 챗봇 만들기
# 1. 외장함수 random을 불러오기
import random
# 2. 1~45 숫자가 저장된 numbers 배열 만들기
numbers = range(1,46)
# 3. 외장함수 random을 활용하여 numbers 배열에서 번호 6개 추출하여 1otto에 저장하기
lotto = random.sample(numbers, 6) # 배열이름 안에 있는 요소 중에 '숫자 갯수만큼 랜덤으로 뽑아주는 메소드'
# 4. lotto 출력하기 
print("로또: ", lotto)