import pandas as pd
import numpy as np

class course():
    def __init__(self, category, name, prof):
        self.category = category
        self.name = name
        self.prof = prof
        self.comments = []
    def addComment(self, comment):
        self.comments.append(comment)
    def addPrereq(self, prereq):
        self.prereq = str(prereq)
    def addAlsoTake(self, alsoTake):
        self.alsoTake = str(alsoTake)
    def dump(self, f):
        f.write('\n')
        f.write('> {}\n'.format(self.name))
        f.write('\n')
        f.write('* 開課教授：{}\n'.format(self.prof))
        if self.alsoTake != 'nan':
            f.write('* 推薦同時修習的課程：{}\n'.format(self.alsoTake))
        if self.prereq != 'nan':
            f.write('* 推薦預先修習的課程：{}\n'.format(self.prereq))
        f.write('* 課程小卦：\n')
        for comm in self.comments:
            f.write(' - {}\n'.format(comm))


data = np.array(pd.read_csv('../dat/compulsory.csv', header=None))

courses = []

for row in data:
    course_i = course(row[0], row[1], row[2])
    #if row[3] != 'nan':
    course_i.addAlsoTake(row[3])
    #if row[4] != 'nan':
    course_i.addPrereq(row[4])
    for i in range(5,10):
        if str(row[i]) == 'nan':
            break
        else:
            course_i.addComment(row[i])
    courses.append(course_i)

with open('../result/compulsory.md', 'w') as f:
    f.write('# 必修\n')
    for course_i in courses:
        course_i.dump(f)


