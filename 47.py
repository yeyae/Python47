#프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
#readline 함수 사용하기
#readline.py
f = open("C:/doit/새파일.txt", 'r')
while True:
   line = f.readline()
   if not line:break
   print(line)
   f.close()


#read 함수 사용하기
f = open("C:/doit/새파일.txt",'r')
data = f.read()
print(data)
f.close()

#f.read() : 파일의 내용 전체를 문자열로 돌려줌


#파일에 새로운 내용 추가하기
with open("foo.txt", "w") as f:
   f.write("Life is too short, you need python")
  
