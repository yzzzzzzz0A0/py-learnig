# 每月存款紀錄 (有正有負)
month_records = [2000, 1500, -500, 3000, 1000, 2000]
# 存錢目標
my_goal = 6000
# 計算累積存款
def calculate_savings(records,target):
    total_savings = 0
    for amount in records:
        if amount < 0:
            continue
        total_savings += amount
        if total_savings >= target: 
            break
    return total_savings
# 呼叫函式並印出結果
final_savings = calculate_savings(month_records, my_goal)
print("最終存款金額:", final_savings)