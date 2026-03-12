# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Perform exploratory data analysis on the netflix_data.csv data
durations = {}

# A movie is considered short if it is less than 90 minutes.
# Count the number of short action movies released in the 2000s and save this integer as short_movie_count
short_movie_count = 0
for lab, row in netflix_df.iterrows():
    if row['type'] == "Movie" and 2000 <= row['release_year'] <= 2009:
        duration = int(row['duration'].split()[0])
        if duration < 90 and 'Action' in row['listed_in']:
            short_movie_count += 1
        if duration in durations:
            durations[duration] += 1
        else:
            durations[duration] = 1

# Visualize the distribution of movie durations
plt.bar(durations.keys(), durations.values())
plt.title('Distribution of Movie Durations in the 2000s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

# Find the most frequent movie duration in the 2000s
# Save an answer as an integer called duration
max = 0
duration = 0
for d, c in durations.items():
    if c > max:
        max = c
        duration = d

print(f'The most frequent movie duration in the 2000s was {duration} min')
print(f'The number of short action movies released in the 2000s was {short_movie_count}')
