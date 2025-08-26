#Please ignore this it may seem weird
#Also this is NOT accurate
import math
from runtime_utils import track_time
@track_time
def calculate_firing_angle():
    cache = {}
    def closure(d,temp,wind): #A closure function, kinda similar to a decorator
        key = (d, temp, wind)
        if key in cache:
            return cache[key]
        
        g, v = 9.81, 100
        inside = (g * d) / v**2
        if inside > 1:
            return None
        
        θ = 0.5 * math.asin(inside)
        deg = math.degrees(θ)
        correction = (temp - 15) * 0.1 - wind * 0.3
        angle = round(deg - correction, 2)
        cache[key] = angle
        return angle
    return closure

@track_time
def calculate_firing_angle_uncached(d, temp, wind):
    g, v = 9.81, 100
    inside = (g * d) / v**2
    if inside > 1:
        return None

    θ = 0.5 * math.asin(inside)
    deg = math.degrees(θ)
    correction = (temp - 15) * 0.1 - wind * 0.3
    angle = round(deg - correction, 2)
    return angle
d, temp, wind = 100, 20, 5
memoized = calculate_firing_angle()
print("Non-memoized:", calculate_firing_angle_uncached(d, temp, wind))
print("Memoized – first call:", memoized(d,temp,wind))
print("Memoized – second call:", memoized(d,temp,wind))