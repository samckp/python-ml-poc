import pandas as pd 

# Create a dataframe with some sample data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Paris', 'London', 'Tokyo']}
df = pd.DataFrame(data)

print(df)

print('--------------------------------')
age = df[df['Age'] > 30 ]

print(age)