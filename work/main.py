import difflib

def fuzzy_match(pattern, sentences):
    matches = []
    for sentence in sentences:
        similarity = difflib.SequenceMatcher(None, pattern, sentence).ratio()
        if similarity > 0.6:  # 设置相似度的阈值
            matches.append((sentence, round(similarity, 2)))
    
    return matches, similarity

# 示例句子列表
print("输入原文的路径：")
ori_name = input()
print("输入待检测文章路径：")
la_name = input()
f = open(ori_name, mode="r", encoding="utf-8")
f_1 = open(la_name, mode="r", encoding="utf-8")

line = f.readline().strip()           #原文
line_1 = f_1.readline().strip()       #待检测文章
temp = []
temp_1 = []
temp.append(line)
temp_1.append(line_1)
while line != "":
    line = f.readline().strip()
    temp.append(line)

while line_1 != "":
    line_1 = f_1.readline().strip()
    temp_1.append(line_1)

result = ''.join(temp)
result_1 = ''.join(temp_1)

sentences = []
sentences.append(result)

# 模糊匹配
pattern = result_1
matches = fuzzy_match(pattern, sentences)[0]
Sim_num = fuzzy_match(pattern, sentences)[1]

# 打印匹配结果
for match in matches:
    print(f"Pattern: {pattern}, Match: {match[0]}, Similarity: {match[1]:.2f}")

f_2 = open("Result.txt", mode="w", encoding="utf-8")
Sim_num = format(Sim_num, ".2f")
Sim_num = str(Sim_num)
f_2.write(Sim_num)