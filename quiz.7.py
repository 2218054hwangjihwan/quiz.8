tree = int(input("Tree 의 높이를 입력하세요 : "))

for x in range(1, tree * 2, 2):
        print((" " * ( (tree * 2 - 1 - x) // 2 )) + ("*" * x))
