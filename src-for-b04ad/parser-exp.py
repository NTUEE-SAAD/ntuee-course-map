import csv

with open("../dat/exp.csv", 'r') as infile: #10選2
    data = csv.reader(infile)
    f = open("../result/exp.md", 'w')
    for course in data:
        f.write("> " + str(course[0]) + "\n\n")
        f.write("* 開課教授：" + str(course[1]) + "\n")
        f.write("* 推薦同時修習的課程：" + str(course[2]) + "\n")
        f.write("* 推薦預先修習的課程：" + str(course[3]) + "\n")
        f.write("* 課程小卦：\n")
        k = 1
        for i in range(4,len(course)):
            if course[i] != '':
                tmp = course[i].replace('\n', '')
                f.write("  {}. ".format(k) + tmp + "\n")
                k += 1
        f.write("\n")
    f.close()