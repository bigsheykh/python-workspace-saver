import pandas

# Create a 2-dimensional array
array = [[1, 2, 3], [4, "hello", 6], [7, 8, 9]]

# Manipulate the values in the DataFrame
df_a = list(pandas.DataFrame(array, columns=['A', 2, 'C'])['A'] + 1)  # Multiply all values in column A by 2
df_2 = list(pandas.DataFrame(array, columns=['A', 2, 'C'])[2] * 2)  # Add 1 to all values in column B
df_c = list(pandas.DataFrame(array, columns=['A', 2, 'C'])['C'] ** 2)  # Square all values in column C

pandas.DataFrame.from_dict(pandas.DataFrame(array, columns=['A', 2, 'C']).to_dict()).info(null_counts=True)
