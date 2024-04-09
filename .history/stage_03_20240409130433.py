
with open('artifacts_01.txt','r') as f:
    text1 = f.read()

with open('artifacts_02.txt','w') as f:
    text2 = f.write(text1 + "artifcats 2 added ")

print(text2)