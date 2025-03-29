# 字符串中的转义字符
print("---------------------------------")
str1 = 'D:\nothing'
print(str1)

# 不需要转义字符生效的时候在字符串前面加上r
print("---------------------------------")
str2 = r'D:\nothing'
print(str2)

# 字符串的切片操作
# str[arg1:arg2:arg3]
# arg1:起始位置，若省略，默认为0
# arg2:结束位置，若省略，默认为字符串长度
# arg3:步长，若省略，默认为1
print("---------------------------------")
str3 = "0123456789"
# 正序切片 ———— 步长默认为1，不填[::]第三个参数也可以，可以省略
# 正序的索引范围：0 - n-1
print(str3[0:5])                    # 0-5 不包括5
print(str3[:])                      # 从头到尾
print(str3[0:])                     # 从头到尾
print(str3[0:10:2])                 # 从头到尾，步长为2
print(str3[::2])                    # 从头到尾，步长为2
# 倒序切片 ———— 步长为-1，不能省略
# 倒序的索引范围：-1 - -n
print(str3[::-1])                   # 从尾到头
print(str3[-1::-1])                 # 从尾到头 
print(str3[-1:-4:-1])               # -1 —— -4 不包括-4
print(str3[:-5:-1])                 # -1 —— -5 不包括-5


# 字符串的拼接
# 直接相加
print("---------------------------------")
str4 = "hello"
str5 = "world"
print(str4 + str5)

# 字符串相关的函数和方法
print("---------------------------------")
str6 = "hello world"
# len()函数
print(len(str6))


# ord()函数
# 返回字符对应的unicode编码
a = ord("a")
print(a)
print(ord("a"))


# title()
# 将字符串中每个单词的首字母大写
str7 = "hello world"
print(str7.title())

# upper()
# 将字符串中所有字母转换为大写
print(str7.upper())

# lower()
# 将字符串中所有字母转换为小写
str8 = "HELLO WORLD"
print(str8.lower())

# rstrip()
# 去掉字符串末尾的空格
str9 = "hello world    "
print(str9.rstrip())

# strip()
# 去掉字符串首尾的空格
str10 = "    hello world    "
print(str10.strip())


# 字符串大小比较
# 比较规则：
# 按照unicode编码逐个比较 只要有不同的字符就以这个不同字符的比较结果作为返回结果
print("azz" < "bbcc")  # True
# 若一个字符串是另一个字符串的前缀，则谁长谁大
print("azz" > "az")

