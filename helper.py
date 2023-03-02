def value_of_ride(row):
    #method for determine value of each fair
    # 
    cost_per_mile = 1.15
    cost_per_minute = 0.22
    service_fee = 1.75
    base_fare = 2.00
    min_fair = 5
    max_fair = 400
    
    distance_in_miles = row.ride_distance / 1609.344
    time_in_minutes = row.ride_duration / 60
    cost = (cost_per_mile * distance_in_miles 
            + cost_per_minute * time_in_minutes)
    
    return max(min(max_fair, cost), min_fair)