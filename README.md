 1. 데이터 가져오기
 2. db에 저장
 3. 웹앱에 불러오기
 4. 웹서버, db aws나 gcp로 운영
 	- docker, kubernetes 활용 cloud system 활용

- 서버 실행 코드
0.0.0.0은 외부접속 허용
python manage.py runserver 0.0.0.0:80

2021-05-10
pymysql.err.InterfaceError: (0, '')
에러 발생

2021-05-11
django - html 연결함
html에서 db 값 정렬한 상태로 나와야됨

mysql model.py에서 연결
https://myjamong.tistory.com/102
위에 있는 거 다 했음
admin 페이지 접속 성공

2021-05-12
Mysql 에서 Django로 값 안불러와짐(HTML로) - 해결




[troubleshootings]
https://angel-jinsu.tistory.com/5
https://stackoverflow.com/questions/47121046/django-str-returned-non-string-type-nonetype/56304121
https://lsjsj92.tistory.com/480 -- 기존에 만든 db djang로 가져오기