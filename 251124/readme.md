1. 기본 개념

PC에 Python 설치

VSC에 Python 확장(Extension) 설치

VSC에서 파이썬 파일을 만들고 실행

2. 설치 & 세팅 흐름
(1) 파이썬 설치

python.org 에서 Windows용 Python 설치

설치할 때 “Add Python to PATH” 체크

(2) VS Code 설치

code.visualstudio.com 에서 설치

(3) VSC에서 Python 확장 설치

VSC 실행 → 왼쪽 퍼즐모양(Extensions) 아이콘 클릭

검색창에 Python 검색 → Microsoft에서 만든 파이썬 확장 설치

3. 첫 파이썬 파일 만들어 실행하기

VSC에서 폴더 하나 열기 (예: D:\python_test)

새 파일 만들기 → 이름: test.py

코드 작성:

print("Hello, Python in VS Code!")


파일 안에서 우클릭 → "Run Python File in Terminal"
또는 상단에 뜨는 Run ▶ 버튼 클릭
→ 아래 터미널에 출력이 보이면 성공

4. VSC로 파이썬 쓸 때 좋은 점

자동완성: 함수/변수 이름 제안

오타/에러 표시: 빨간/노란 밑줄로 문법 에러, 경고 표시

디버깅: 중단점 찍고, 한 줄씩 실행하면서 변수 값 확인 가능

가상환경 연동: 프로젝트별로 다른 라이브러리 세트 관리 가능 (venv, conda 등)

5. 앞으로 익혀두면 좋은 사용 패턴

터미널 열기

Ctrl + ' (숫자1 왼쪽의 백틱키) → 내장 터미널 열림

여기서 python 파일이름.py 로 직접 실행도 가능

가상환경 + VSC 연동

python -m venv venv

VSC에서 인터프리터 선택: 좌측 하단 Python 버전 클릭 → .\venv\Scripts\python.exe 선택
