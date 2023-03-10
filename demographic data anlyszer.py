import pandas as pd

def demographic_data_analyzer(filepath):
    # read in the csv file to a Pandas dataframe
    df = pd.read_csv(filepath)
    
    # How many people of each race are represented in this dataset?
    race_counts = df['race'].value_counts()
    
    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    
    # What is the percentage of people who have a Bachelor's degree?
    bachelors_percent = len(df[df['education'] == "Bachelors"]) / len(df) * 100
    
    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_edu = df[df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    advanced_edu_over_50k = len(advanced_edu[advanced_edu['salary'] == ">50K"]) / len(advanced_edu) * 100
    
    # What percentage of people without advanced education make more than 50K?
    not_advanced_edu = df[~df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    not_advanced_over_50k = len(not_advanced_edu[not_advanced_edu['salary'] == ">50K"]) / len(not_advanced_edu) * 100
    
    # What is the minimum number of hours a person works per week?
    min_hours_per_week = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_workers = df[df['hours-per-week'] == min_hours_per_week]
    min_hours_over_50k = len(min_hours_workers[min_hours_workers['salary'] == ">50K"]) / len(min_hours_workers) * 100
    
    # What country has the highest percentage of people that earn >50K and what is that percentage?
    over_50k = df[df['salary'] == ">50K"]
    country_percentages = over_50k['native-country'].value_counts() / len(over_50k) * 100
    highest_earning_country = country_percentages.idxmax()
    highest_earning_percent = country_percentages.max()
    
    # Identify the most popular occupation for those who earn >50K in India.
    india_over_50k = over_50k[over_50k['native-country'] == "India"]
    popular_occupation = india_over_50k['occupation'].value_counts().idxmax()
    
    return {
        'race_counts': race_counts,
        'average_age_men': average_age_men,
        'bachelors_
