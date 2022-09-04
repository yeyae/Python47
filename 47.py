#프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
#readline 함수 사용하기
#readline.py
f = open("C:/doit/새파일.txt", 'r')
while True:
   line = f.readline()
   if not line:break
   print(line)
   f.close()


#이부분에 대해서는 다시 공부할 것
