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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter City name").lower()
        if city not in ["chicago", "new york city", "washington"]:
            print("please write exactly either 'chicago' or 'new york city' or 'washington'")
        else:
            print(f"{city} chosen")
            break  
    

    #get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter Month name").lower()
        if month not in ["all", "january", "february","march", "april","may" ,"june"]:
            print("please write exactly either 'chicago' or 'new york city' or 'washington'")
        else:
            print(f"{month} chosen")
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter Day name").lower()
        if day not in ["all", "monday", "tuesday","wednesday","thursday","friday","saturday","sunday"]:
            print("please write exactly either 'chicago' or 'new york city' or 'washington'")
        else:
            print(f"{day} chosen")
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    # extract day from the Start Time column to create an day column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(f"most common month is: {df['month'].mode()[0]} and it occurred {df['month'].value_counts()[0]} times")

    # TO DO: display the most common day of week
    print(f"most common day is: {df['day_of_week'].mode()[0]} and it occurred {df['day_of_week'].value_counts()[0]} times")

    # TO DO: display the most common start hour
    print(f"most common start hour is: {df['hour'].mode()[0]} and it occurred {df['hour'].value_counts()[0]} times")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"most common start station is: {df['Start Station'].mode()[0]} and it occurred {df['Start Station'].value_counts()[0]} times")

    # TO DO: display most commonly used end station
    print("most common End station is: "+df['End Station'].mode()[0]+" and it occurred "+df['End Station'].value_counts()[0]+" times")

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is : " + str((df['Start Station'] + "||" + df['End Station']).mode()[0].split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time from the given fitered data is: " + str(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("The mean travel time from the given fitered data is: " + str(df['Trip Duration'].mean()))

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
    if city == 'chicago' or city == 'new_york_city':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth from the given fitered data is: {}\n'.format(earliest_birth))
        print('Most recent birth from the given fitered data is: {}\n'.format(most_recent_birth))
        print('Most common birth from the given fitered data is: {}\n'.format(most_common_birth) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
