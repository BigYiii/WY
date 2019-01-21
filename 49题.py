#给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
str = "{}()([])"
list = []
if str == "":
    print("The string is null")
else:
    for i in str:

        if i == '{' or i == '(' or i == '[':
            list.append(i)
        if i == '}' and list[len(list) - 1] == '{':
            del list[len(list) - 1]
        if i == ']' and list[len(list) - 1] == '[':
            del list[len(list) - 1]
        if i == ')' and list[len(list) - 1] == '(':
            del list[len(list) - 1]
    if list:
        print("The string is error")
    else:
        print("The string is right")

