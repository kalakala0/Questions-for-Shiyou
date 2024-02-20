def replace_duplicate_chars(input_str, k):
    result = ""
    seen_chars = set()
    #将不允许重复出现的字符定义为一个集合
    for i, char in enumerate(input_str):
        if char in seen_chars:
            result += '-'
        else:
            result += char

        if i >= k:
            seen_chars.discard(input_str[i - k])
            #移除集合中第k个前的字符

        seen_chars.add(char)
        #将新字符加入到集合中
    return result

user_input = input("请输入字符串和 k: ")
input_list = user_input.split()
if len(input_list) == 2:
    input_string, k_value = input_list
    try:
        k_value = int(k_value)
        output_string = replace_duplicate_chars(input_string, k_value)
        print("替换后的字符串:", output_string)
    except ValueError:
        print("k 必须是一个非负整数。")
else:
    print("输入格式不正确，请按照 'string k' 的格式输入。")
