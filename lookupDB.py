import pymysql

# 데이터베이스에 연결
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='0000',
    db='njDB',
    charset='utf8'
)

try:
    with conn.cursor() as cur:
        # 데이터 조회 쿼리 실행
        cur.execute("SELECT * FROM userTable")

        # 모든 행을 가져옴
        rows = cur.fetchall()

        # 각 행을 출력
        for row in rows:
            print(row)

finally:
    conn.close()
