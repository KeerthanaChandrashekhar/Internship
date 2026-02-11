import pandas as pd

marks = pd.Series([78, 85, 92, 60, 88],
                  index=['A', 'B', 'C', 'D', 'E'])

print(marks)

mask = marks >= 80
print(mask)

print(marks[( marks >= 80) & (marks < 90) ])

marks[marks < 70] = 70
print(marks)