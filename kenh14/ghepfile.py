import os

list_file = os.listdir("ghep")
print(len(list_file))
list_data = []
for i in list_file:
    list_data.append("\n")
    with open("ghep/"+i, "r", encoding='utf-8') as file:
        lines = file.readlines()
        list_data.extend(lines)
# for i in range(0,100):
#     list_data[i].strip()
#     str(list_data[i]).replace("\t", "").replace("\n", "").replace("  ","")
#     print(list_data[i])
with open("data_w2v_bao_final.txt","w",encoding='utf-8') as file:
    for i in list_data:
        file.write(i)
