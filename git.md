# git 명령어

## 초기 설정
```
git config --global user.name "유저네임" 
git config --global user.email "유저이메일"

git init #상위 폴더에서 1번만 실행(폴더 위치 확인시켜줌)(master)
```

## 내용 변경시
1. 내용 변경
2. 저장 !!!!!
3. git add 파일명(.)
4. git commit -m "변경 사항"

## 상태 확인
```
git status # 현재 상태 확인
git log # 커밋 내역 확인
```

## 로컬 저장소 -> 리모트 저장소
```
1. git remote add origin URL(옮길 주소)
2. git push origin master
```

## 리모트 저장소 -> 로컬 저장소
1. 옮기고 싶은 곳에서 git bash here를 누른다
2. git clone URL

### clone
1. 폴더생성
2. git init
3. git remote add
4. 버전, 파일 생성

### pull
- update한 정보를 받아야 할 때
명령어
```
git pull origin master
```