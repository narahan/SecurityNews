


# flask 모듈에서 Flask 클래스 임포트
from doctest import DocTestFailure
from flask import Flask, render_template
from sqlite3 import connect
from mk import getMkData
from boannews import getBoanData
from dailysecu import getDailyData


# Flask 객체의 인스턴스를 만들고 'app'에 할당
app = Flask(__name__)

# 매일경제 크롤링 데이터
mk_data = getMkData()

# 데일리시큐 크롤링 데이터
daily_data = getDailyData()

# 보안뉴스 크롤링 데이터
boan_data = getBoanData()






@app.route('/mk')
def mk():
	return render_template('mk.html', data = mk_data)

@app.route('/boan')
def boan():
	return render_template('boan.html', data = boan_data)

@app.route('/daily')
def daily():
        return render_template('daily.html', data = daily_data)




# 배포판에서는 하단 삭제
# if __name__ == '__main__':
	# app.run(debug=True)
	# app.run(host="127.0.0.1", port="4000", debug=True)

# host 등을 직접 지정하고 싶다면
if __name__ == '__main__':
	# app.run(port=5000, debug=True)
	app.run(host="127.0.0.1", port="4000", debug=True)


