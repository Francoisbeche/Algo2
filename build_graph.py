import pandas as pd

netflix_file_path = './netflix_titles_nov_2019.csv'

netflix_data = pd.read_csv(netflix_file_path)

##print(netflix_data);
def loopShit():
    for index, row in netflix_data.iterrows():
        print(row['show_id'], row['cast'])

loopShit()