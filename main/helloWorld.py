


# flask에서 Flask라는 클래스를 임포트 한 코드
from flask import Flask

# Flask라는 클래스의 객체를 생성하고 인자로 __name__을 입력
#[그림 3]과 같이 단일 모듈을 사용한다면, __name__을 인자로 사용해야 합니다. 
#왜냐하면 어플리케이션으로 시작되는지 혹은 모듈로 임포트 되는지에 따라 이름이 달라지기 때문
app =  Flask(__name__)


@app.route('/')
def hello():
        return 'testtestetst'

if __name__ == '__main__':
        app.run()