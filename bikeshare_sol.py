import pandas as pd
from datetime import datetime
from datetime import timedelta
import time

## Filenames
#chicago = 'chicago.csv'
#new_york_city = 'new_york_city.csv'
#washington = 'washington.csv'

# find out the city #
def get_city():

    city = ''
    while city.lower() not in ['chi', 'nyc', 'was']:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or'
                     ' Washington?\n')
        if city.lower() == 'chi':
            return 'chicago.csv'
        elif city.lower() == 'nyc':
            return 'new_york_city.csv'
        elif city.lower() == 'was':
            return 'washington.csv'
        else:
            print('Sorry, I do not understand your input. Please input either '
                  'Chicago, New York, or Washington.')
# find out for which time period #
def get_time_period():

    time_period = ''
    while time_period.lower() not in ['month', 'day', 'none']:
        time_period = input('\nWould you like to filter the data by month, day,'
                            ' or not at all? Type "none" for no time filter.\n')
        if time_period.lower() not in ['month', 'day', 'none']:
            print('Sorry, I do not understand your input.')
    return time_period
# find out for which month #
def get_month():

    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nWhich month? Please choose as suggest: january, february, march, april, may, or june?\n')
        if month_input.lower() not in months_dict.keys():
            print('Sorry, I do not understand your input. Please type in a '
                  'month between january and june')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))
# find out for which day #
def get_day():

    this_month = get_month()[0]
    month = int(this_month[5:])
    valid_date = False
    while valid_date == False:
        is_int = False
        day = input('\nWhich day? Please type your response as an integer.\n')
        months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
        while is_int == False:
            try:
                day = int(day)
                is_int = True
            except ValueError:
                print('Sorry, I do not understand your input. Please type your'
                      ' response as an integer.')
                day = input('\nWhich day? Please type your response as an integer.\n')
        try:
            start_date = datetime(2017, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))
# TO DO: display the most common month #
def common_month(df):

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    index = int(df['start_time'].dt.month.mode())
    most_comm_month = months[index - 1]
    print('The most common month is {}.'.format(most_comm_month))
# TO DO: display the most common day #
def common_day(df):

    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                    'saturday', 'sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_comm_day = days_of_week[index]
    print('The most common day of week for start time is {}.'.format(most_comm_day))
# TO DO: display the most common hour #
def common_hour(df):

    most_comm_hour = int(df['start_time'].dt.hour.mode())
    if most_comm_hour == 0:
        am_pm = 'am'
        comm_hour_readable = 12
    elif 1 <= most_comm_hour < 13:
        am_pm = 'am'
        comm_hour_readable = most_comm_hour
    elif 13 <= most_comm_hour < 24:
        am_pm = 'pm'
        comm_hour_readable = most_comm_hour - 12
    print('The most common hour of day for start time is {}{}.'.format(comm_hour_readable, am_pm))
# TO DO: Dispaly the trip duration #
def trip_duration(df):

    total_duration = df['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))
    average_duration = round(df['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))
# TO DO: display the most common Start and End Station #
def common_stations(df):

    comm_start = df['start_station'].mode().to_string(index = False)
    comm_end = df['end_station'].mode().to_string(index = False)
    print('The most common start station is {}.'.format(comm_start))
    print('The most common end station is {}.'.format(comm_end))
# TO DO: display the most common hour #
def common_trip(df):

    most_comm_trip = df['journey'].mode().to_string(index = False)
    # The 'journey' column is created in the statistics() function.
    print('The most common trip is {}.'.format(most_comm_trip))
# TO DO: Display counts of user types
def users(df):

    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))
# TO DO: Display counts of gender
def gender(df):

    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Male"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))
# TO DO: Display earliest, most recent, and most common year of birth
def birth_years(df):

    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))
 # TO DO: Display raw data
def display_data(df):
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nDo you like to see some raw data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry, I do not understand your input. Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
        # prints every column except the 'journey' column created in statistics()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nDo you like to see more raw data?'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, I do not understand your input. Please type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break
# Repeat
def repeat():

    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    print('Loading data...')
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])

    # change all column names to lowercase letters and replace spaces with underscores
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels

    # increases the column width so that the long strings in the 'journey'
    # column can be displayed fully
    pd.set_option('max_colwidth', 100)

    # creates a 'journey' column that concatenates 'start_station' with
    # 'end_station' for the use common_trip() function
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == 'none':
        df_filtered = df
    elif time_period == 'month' or time_period == 'day':
        if time_period == 'month':
            filter_lower, filter_upper = get_month()
        elif time_period == 'day':
            filter_lower, filter_upper = get_day()
        print('Filtering data...')
        df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]
    print('\nCalculating the first statistic...')

    if time_period == 'none':
        start_time = time.time()

        # What is the most common month for start time?
        common_month(df_filtered)
        print("\nNext statistic coming up...")

    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        # What is the most common day of week (Monday, Tuesday, etc.) for start time?
        common_day(df_filtered)
        print("\nNext statistic coming up...")
        start_time = time.time()

    # What is the most common hour of day for start time?
    common_hour(df_filtered)
    print("\nNext statistic coming up...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    trip_duration(df_filtered)
    print("\nNext statistic coming up...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    common_stations(df_filtered)
    print("\nNext statistic coming up...")
    start_time = time.time()

    # What is the most common trip?
    common_trip(df_filtered)
    print("\nNext statistic coming up...")
    start_time = time.time()

    # What are the counts of each user type?
    users(df_filtered)

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print("\nNext statistic coming up...")
        start_time = time.time()

        # What are the counts of gender?
        gender(df_filtered)
        print("\nNext statistic coming up...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest
        # user), and most common birth years?
        birth_years(df_filtered)

        # Display five lines of raw data
    display_data(df_filtered)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    while restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        repeat()


if __name__ == "__main__":
	repeat()
