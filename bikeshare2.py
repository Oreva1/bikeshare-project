import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('\nWould you like to see data for Chicago, New york city or Washington? ').lower()
    while city not in CITY_DATA:
        print('Invalid city name provided, please select a valid city name')
        city = input('\nWould you like to see data for Chicago, New york city or Washington? ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'april', 'may', 'june', 'all']
    while True:
        month = input('\nWould you like to filter by month? If month, January, February, April, May, June or all? ').lower()
        if month not in months:
            print('Invalid month provided, please select a valid month')
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while True:
        day = input('\nWould you like to filter by day? Select a day or choose all. ').lower()
        if day not in days:
            print('Invalid day selected, please select a valid day')
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert the start time column to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month and day of the week from start time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #filter by month if applicable
    if month != 'all':
        #use the index of the months list to get the correct integer
        months = ['january', 'february', 'april', 'may', 'june']
        month = months.index(month) + 1

    #filter by month to create the new dataframe
        df = df[df['month'] == month]
    #filter by day of the week if applicable
    if day != 'all':
    #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('The most common month is', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('The common day of week is', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = (df['Start Station'] + '-' + df['End Station']).mode()[0]
    print('The most common trip is', common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time is', total_travel)

    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print('The mean travel time is', travel_mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender

        gender = df['Gender'].value_counts()
        print('\nGender:\n', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('\nThe earliest birth year is', earliest_birth_year)
        recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year is', recent_birth_year)
        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common birth year is', common_birth_year)
    else:
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays rows of raw data according to user input."""
    #TO DO: Display raw data

    i=0
    view_data = input('\nWould you like to see 5 rows of raw data? Please select Yes or No ').lower()
    while True:
        if view_data.lower() == 'yes':
            print(df.iloc[i:i+5])
            i += 5
            view_data = input('\nWould you like to see 5 more rows of raw data? Please select Yes or No ').lower()
            i += 5
        if view_data.lower() == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
