# 學生名字對應分數的字典
score_sheet = {"Amy": 90, "Billy": 55, "Cindy": 72}

# 我們今天要查這位同學
student = "Billy"
# 查詢分數
score = score_sheet[student]
if score >= 60:
    print(f"{student}及格了，分數是{score}分")
else:
    print(f"{student}不及格，分數是{score}分")