def run_atm(transactions, balance):
    # --- 請在這裡開始寫你的迴圈與 match-case 邏輯 ---
    for transaction in transactions:
        
        # 直接把一整包 transaction 丟進去 match
        match transaction:
            
            # 如果形狀是 ["Deposit", 一個數字]
            case ["Deposit", amount]:
                balance += amount
                
            # 如果形狀是 ["Withdraw", 一個數字]
            case ["Withdraw", amount]:
                if amount > balance:
                    print("餘額不足")
                else:
                    balance -= amount
                    
            # 如果形狀只有 ["Exit"]
            case ["Exit"]:
                print("結束交易")
                break
  
    return balance # 最後回傳算完的餘額

# --- 測試資料 ---
my_transactions = [
    ["Deposit", 1000],    # 存 1000
    ["Withdraw", 500],    # 領 500
    ["Withdraw", 2000],   # 領 2000 (這裡應該要印出餘額不足)
    ["Exit"],             # 結束迴圈
    ["Deposit", 300]      # 因為已經 Exit，這筆不該被執行到
]
initial_balance = 1000

# 呼叫函式
final_balance = run_atm(my_transactions, initial_balance)
print(f"最終餘額: {final_balance}")     
