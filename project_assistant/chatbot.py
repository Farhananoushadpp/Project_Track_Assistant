
import pymysql
from werkzeug.utils import secure_filename
import re, math
con=pymysql.connect(host="localhost",port=3306,user="root",password="",db="chatbot",cursorclass=pymysql.cursors.DictCursor)
cmd=con.cursor()
def cb(qus):
    WORD = re.compile(r'\w+')
    qus=qus.lower()

    from collections import Counter
    def text_to_vector(text):
        words = WORD.findall(text)
        return Counter(words)

    def get_cosine(vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
        sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    vector1 = text_to_vector(qus)
    cmd.execute("select Question,lid from dataset")
    sss=cmd.fetchall()
    print("s--" ,sss)
    res = []
    for d in sss:
        vector2 = text_to_vector(str(d['Question']).lower())
        cosine = get_cosine(vector1, vector2)
        # print("cosine",cosine)

        res.append(cosine)

    print("res---" ,res)

    ss = 0
    cnt = -1
    i = 0
    for s in res:
        if s > 0.3:
            if ss <= float(s):
                cnt = i
                ss = s
        i = i + 1

    print("ss", ss)
    print("cnt", cnt)
    if cnt!=-1:
        cmd.execute("select * from dataset where lid='" + str(sss[cnt]['lid']) + "'")
        aa = cmd.fetchone()
        print(aa,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        if aa is None:
            return "I can not understand the question"
        else:
            return aa['Answer']
    else:
        return "I can not understand the question"

