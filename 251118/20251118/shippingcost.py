price = int(input("상품의 가격: "))
if price > 20000:
    shippingCost = 0
    print("VIP고객님",end=" ")
else:
    shippingCost = 3000
    print("고객님",end=" ")
print(f"배송비는 {shippingCost} 입니다.")
