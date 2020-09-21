class Solution:
    def carPooling(self, trips, capacity):
        # Sorted list of events
        event_times = [(x[1],x[0]) for x in trips] + [(x[2],-x[0]) for x in trips]
        event_times.sort(key = lambda x: x[0])
        current = 0
        prev = None
        for time,change in event_times:
            if time != prev and current > capacity:
                return False
            prev = time
            current += change
        if current > capacity:
            return False
        return True
