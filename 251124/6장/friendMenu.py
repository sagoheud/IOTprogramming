menu = 0
friends = []
while menu != 9:
    print(" ")
    print("="*20)
    print("1. 친구 리스트")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")
    print("="*20)
    menu = int(input("메뉴 선택: "))
    match menu:
        case 1:
            print("\n",friends)
        case 2:
            name = input("\n추가할 이름: ")
            friends.append(name)
        case 3:
            name = input("\n삭제할 이름: ")
            if name in friends:
                friends.remove(name)
            else:
                print("\n리스트에 없습니다.\n")
        case 4:
            old_name = input("\n변경할 이름: ")
            if old_name in friends:
                new_name = input("\n새로운 이름: ")
                index = friends.index(old_name)
                friends[index] = new_name
            else:
                print("\n리스트에 없습니다.\n")
        case 9:
            print("\n프로그램을 종료합니다.\n")
        case _:
            print("\n다시 시도하세요.\n")
            
''' 
    if menu == 1:
        print("\n",friends)
    elif menu == 2:
        name = input("\n추가할 이름: ")
        friends.append(name)
    elif menu == 3:
        name = input("\n삭제할 이름: ")
        if name in friends:
            friends.remove(name)
        else:
            print("\n리스트에 없습니다.\n")
    elif menu == 4:
        old_name = input("\n변경할 이름: ")
        if old_name in friends:
            new_name = input("\n새로운 이름: ")
            index = friends.index(old_name)
            friends[index] = new_name
        else:
            print("\n리스트에 없습니다.\n")
    elif menu == 9:
        print("\n프로그램을 종료합니다.\n")
    else:
        print("\n다시 시도하세요.\n")
'''