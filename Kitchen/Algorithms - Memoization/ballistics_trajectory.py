#Please ignore this it may seem weird
#Also this is NOT accurate
import math
from runtime_utils import track_time

@track_time
def calculate_firing_angle(target_distance, temp_celsius, wind_speed_mps):
    """
    Calculate a naive firing angle based on distance, temperature, and wind.
    Assumptions:
    - Constant initial velocity (say 100 m/s)
    - Adjustments based on environmental effects
    - Output in degrees
    """
    g = 9.81  # gravity (m/s^2)
    v = 100   # initial velocity (m/s)
    # Basic angle without wind/temp correction (no air resistance)
    inside = (g * target_distance) / (v**2)
    if inside > 1:
        return None  # unreachable with current velocity

    base_angle_rad = 0.5 * math.asin(inside)
    base_angle_deg = math.degrees(base_angle_rad)
    temp_modifier = (temp_celsius - 15) * 0.1    # warmer air = more range
    wind_modifier = wind_speed_mps * 0.3         # tailwind = overshoot risk
    correction = temp_modifier - wind_modifier
    final_angle = base_angle_deg - correction
    return round(final_angle, 2)

cache = {}
@track_time
def calculate_memoized_firing_angle(target_distance, temp_celsius, wind_speed_mps):
    """
    Calculate a naive firing angle based on distance, temperature, and wind.
    Assumptions:
    - Constant initial velocity (say 100 m/s)
    - Adjustments based on environmental effects
    - Output in degrees
    """
    key = (target_distance,temp_celsius,wind_speed_mps)
    if key in cache:#Retrieve computed values from cache
        return cache[key]
    else:
    
        g = 9.81  # gravity (m/s^2)
        v = 100   # initial velocity (m/s)
        # Basic angle without wind/temp correction (no air resistance)
        inside = (g * target_distance) / (v**2)
        if inside > 1:
            return None  # unreachable with current velocity

        base_angle_rad = 0.5 * math.asin(inside)
        base_angle_deg = math.degrees(base_angle_rad)
        temp_modifier = (temp_celsius - 15) * 0.1    # warmer air = more range
        wind_modifier = wind_speed_mps * 0.3         # tailwind = overshoot risk
        correction = temp_modifier - wind_modifier
        final_angle = base_angle_deg - correction
        
        cache[key] =  round(final_angle, 2)
        return cache[key]
    
target_distance = 12 #<1020
temp_celsius = 12
wind_speed_mps = 22
print(calculate_firing_angle(target_distance,temp_celsius,wind_speed_mps)) #Ignore: typing
print(calculate_memoized_firing_angle(target_distance,temp_celsius,wind_speed_mps))
print(calculate_memoized_firing_angle(target_distance,temp_celsius,wind_speed_mps))