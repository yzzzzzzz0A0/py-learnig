# 測試資料，你可以試著改成 ["Get", "Gold", 100] 或 ["System", "Save"] 來跑跑看
user_command = ["Get", "Potion", 5]
match user_command:
    case ["System", "Save"]:
        print("存檔成功！")
    case ["Get", item_name, count]:
        print(f"獲得 {item_name} 共 {count} 個")
    case ["Move", direction]:
        print(f"正在往 {direction} 前進")
    case _:
        print("無效的指令！")