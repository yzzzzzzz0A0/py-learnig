command = "A"
match command:
    case "A":
        print("發動攻擊！")
    case "D":
        print("防禦姿態！")
    case "H":
        print("使用補血！")
    case _:
        print("無效的指令！")
