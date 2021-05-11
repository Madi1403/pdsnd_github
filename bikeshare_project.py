import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york', 'washington']
month_titles = ['all','january','february','march','april','may','june']
day_titles = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('For what city would you like to see the data? Chicago, New York or Washington:\n').lower()
    while True:
        if city not in cities:
            city = input('Sorry, unfortunately your input was incorrect. You can choose from the following cities: Chicago,New York and Washington. \nPlease note, that there is a space in the word New York.\n').lower()
            continue
        else:
            break
    print('Cool, you picked the following city:\n' + city.title())
    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input('For what month would you like to see the data? You can choose either from a month from January to June or all.\n').lower()
    while True:
        if month not in month_titles:
            month = input('Sorry, there was an error in your input. Please choose one of the following - January, February, March, April, May, June or all.\n').lower()
            continue
        else:  
            break
    print('Thank you for choosing this month:\n' + month.title())
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('For what day would you like to see the data? You can choose either all or a day from Monday to Sunday. \n').lower()
    while True:
        if day not in day_titles:
            day = input('Sorry, there was an error in your input. Please choose one of the following - all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or\nSunday.\n').lower()
            continue
        else:
            break
    print('Thank you that you chose this day:\n' + day.title())
                     
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day"""
    
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
                                      
    #extract month,weekday and start hour from the Start Time column to create new columns
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
        
                                      
    #filter by month if applicable
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+ 1
      
    #filter by month to create the new dataframe
        df = df[df['month'] == month]

    #filter by day if applicable
    if day != 'all':
        
    #filter by day of week to create the new dataframe
        df = df[df['weekday'] == day.title()]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: {}.'.format(common_month))

    # TO DO: display the most common day of week
    common_day = df['weekday'].mode()[0]
    print('The most common day is: {}.'.format(common_day))

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common starting hour is: {}.'.format(common_start_hour))

    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('\nThe most commonly used start Station is: {}.'.format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nThe most commonly used end Station is: {}.'.format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Common Combination'] = df['Start Station'] + ' and ' + df['End Station']
    most_frequent_combination = df['Common Combination'].value_counts().idxmax()
    print('\nThe most commonly used combination of start and end station is: {}.'.format(most_frequent_combination))

    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Trip Duration'] = df['Trip Duration'].mode()[0]

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time is {} days.'.format(total_travel))

    # TO DO: display mean travel time
    mean_travel = (df['Trip Duration'].mean()) / 60
    print('The mean travel time is {} minutes'.format(mean_travel))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
     user_type = df['User Type'].value_counts()
     print('Here is the total amount of each user type:\n{}\n'.format(user_type))

    # TO DO: Display counts of gender
     gender = df['Gender'].value_counts()
     print('Here is the count of each gender:\n',gender)

    # TO DO: Display earliest, most recent, and most common year of birth
     birth_year = df['Birth Year']
     print('\nThe earliest birth year is:', birth_year.min())
     print('The most recent birth year is:', birth_year.max())
     print('The most common birth year is:', birth_year.mode()[0])

    except KeyError:
     print('There is no gender and birth year data available for Washington.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_input(df):
    """Asks users for raw data."""
    
    print('\nAsking for raw data...\n')
    raw_data = 0
    while True:
        userinput = input('Would you like to see 5 rows of raw data? Please choose yes, if you would like to and no if you would not.\n').lower()
        if userinput not in ['yes', 'no']:
            userinput = input('Unfortunately your input is not correct. Could you please choose between yes and no.\n').lower()
        elif userinput == 'yes':
            print(df.iloc[raw_data : raw_data + 5])
            raw_data += 5
        elif userinput == 'no':
                return
            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()