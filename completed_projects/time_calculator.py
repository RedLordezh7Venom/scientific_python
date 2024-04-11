def add_time(start, duration, start_day=None):
    x = start
    hours = 0
    minutes = 0
    
    if x[-2] == 'P':
        hours+=12
    
    idx = x.find(':')
    hours += int(x[:idx])
    stripped = x.find(' ')
    minutes+=int(x[idx+1:stripped])
    
    add_hours = 0
    add_minutes = 0
    
    x=duration
    
    idx = x.find(':')
    add_hours+=int(x[:idx])
    add_minutes+=int(x[idx+1:])
    
    new_time_hours = hours+add_hours
    new_time_minutes = minutes+add_minutes

    if new_time_minutes > 59:
        new_time_hours+=new_time_minutes//60
        new_time_minutes = new_time_minutes%60

    days = new_time_hours//24
    new_time_hours = new_time_hours%24
    
    meridian = new_time_hours//12
    new_time_hours = new_time_hours%12
    
    meri = ""
    if new_time_hours == 0:
        new_time_hours = 12
    if meridian == 0:
        meri = "AM"
    else:
        meri = "PM"
    
    
    new_time = f'{new_time_hours}:{new_time_minutes:02d} {meri}'
    if start_day:
        # Define a list of days of the week
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        # Find the index of the start day in the list
        start_day_index = days_of_week.index(start_day.capitalize())
        # Calculate the new day after adding the number of days
        new_day_index = (start_day_index + days) % 7
        new_day = days_of_week[new_day_index]
        new_time += f', {new_day}'
    if days == 0:
        pass
    else:
        if days == 1:
            new_time+= ' (next day)'                                                                                                                           
        else:
            new_time += f' ({days} days later)'

    return new_time
