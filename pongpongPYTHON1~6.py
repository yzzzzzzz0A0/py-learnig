# 商品價格
menu = {"bubble_tea": 50, "green_tea": 30}
# VIP 名單
vips = {"Tony", "Amy", "Peng"}

# 當前顧客資訊
customer_name = "Tony"
item_name = "bubble_tea"
quantity = 2
# 計算總價
total_price = menu[item_name] * quantity
# 檢查是否為 VIP 並套用折扣
if customer_name in vips and total_price >= 100:
    total_price *= 0.9  # VIP 折扣 10%
# 輸出結果
print(f"Customer: {customer_name}")
print(f"Total Price: {total_price}")