import re

# 3位数字-3到8个数字 \d{3}-\d{3,8}

mr = re.match(r'\d{3}-\d{3,8}', '010-223456')
print(mr.string)

# 分组
m = re.match(r'(\d{3})-(\d{3,8})$', '010-223456')
print(m.groups())
print(m.group(0))   #原始字段
print(m.group(1))   #第一段
print(m.group(2))   #第二段

t = '20:25:45'
re.match(r'^0[0-9]|1[0-9]|2[0-3]|[0-9]\:(0[0-9])')

# 分割字符串
p = re.complie(r'\d+')
print(p.split('one1two2three3four4'))
