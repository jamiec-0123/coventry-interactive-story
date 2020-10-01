filepath = 'dataDump.txt'
with open(filepath, 'r', encoding='utf8') as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
#output eg. Line 2: The Fly on Doritos
