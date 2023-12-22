import re
import csv
# 读取并处理原始数据文件
with open('/Users/popo/Library/CloudStorage/Dropbox/bigdata_econ_2023/data/assignment_wosparse/qje2014_2023.txt', 'r', encoding='utf-8') as file:
    data = file.read()


# 使用re.split函数分割原始数据
rows = re.split(r'\n', data)
columns = re.split(r'\t', rows[0])
values = [re.split(r'\t', row) for row in rows[1:] if row.strip() != '']


# 提取表格1-论文基本信息
selected_columns = ['UT', 'PY', 'SO', 'SN', 'DI', 'VL', 'IS']
selected_values = [[row[columns.index(column)] for column in selected_columns] for row in values if len(row) >= len(columns)]

# 生成表格1并保存到CSV文件
with open('qje2014_2023table1.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(selected_columns)
    writer.writerows(selected_values)

# 提取表格2-论文摘要
selected_columns = ['UT', 'AB']
selected_values = [[row[columns.index(column)] for column in selected_columns] for row in values if len(row) >= len(columns)]

# 生成表格2并保存到CSV文件
with open('qje2014_2023table2.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(selected_columns)
    writer.writerows(selected_values)

# 提取表格3-论文标题
selected_columns = ['UT', 'TI']
selected_values = [[row[columns.index(column)] for column in selected_columns] for row in values if len(row) >= len(columns)]

# 生成表格3并保存到CSV文件
with open('qje2014_2023table3.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(selected_columns)
    writer.writerows(selected_values)



# 提取表格6-论文参考文献
selected_columns = ['UT', 'CR', 'NR']
selected_values = [[row[columns.index(column)] for column in selected_columns] for row in values if len(row) >= len(columns)]

# 生成表格6并保存到CSV文件
with open('qje2014_2023table6.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(selected_columns)
    writer.writerows(selected_values)


# 提取表格4-论文作者
# 提取UT和AF变量的索引
ut_index = columns.index('UT')
af_index = columns.index('AF')

# 提取UT和AF变量，并拆分AF中的人名
authors = []
for row in values:
    if len(row) > max(ut_index, af_index):
        ut = row[ut_index]
        af = row[af_index]
        author_names = af.split('; ')
        for i, author_name in enumerate(author_names):
            name_parts = author_name.strip().split(', ')
            given_name = name_parts[1].rsplit(' ', 1)[0]
            family_name = ', '.join(name_parts[:1])
            author = {
                'UT': ut,
                'Author_Number': i + 1,
                'Full_Name': author_name,
                'Family_Name': family_name,
                'Given_Name': given_name
            }
            authors.append(author)

# 生成表格并保存到CSV文件
columns = ['UT', 'Author_Number', 'Full_Name', 'Family_Name', 'Given_Name']
with open('qje2014_2023table4.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(authors)


# 提取表格5-论文作者与单位
selected_columns = ['UT', 'C1']
selected_values = [[row[columns.index(column)] for column in selected_columns] for row in values if len(row) >= len(columns)]

# 生成表格5并保存到CSV文件
with open('qje2014_2023table5.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(selected_columns)
    writer.writerows(selected_values)


