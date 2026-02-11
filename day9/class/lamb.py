numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))
print(result)

import pandas as pd

marks = pd.Series([50, 65, 80, 90])

result = marks.apply(lambda x: x + 5)
print(result)

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [70, 55, 85]
})

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 60 else "Fail")

print(df)

#A lambda function is a small, anonymous (unnamed) function written in a single line.
square = lambda x: x * x
print(square(5))

#in list 
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))
print(result)

#in pandas series
import pandas as pd

marks = pd.Series([50, 65, 80, 90])

result = marks.apply(lambda x: x + 5)
print(result)

#apply conditional logic
grades = marks.apply(lambda x: "Pass" if x >= 60 else "Fail")
print(grades)

# Lambda in Dataframe
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [70, 55, 85]
})

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 60 else "Fail")

print(df)