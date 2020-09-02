class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # O(N) one-pass solution based on buckets with size t + 1
        if k <= 0 or t < 0:
            return False
        from collections import deque
        bucket_cache = deque([],k)
        bucket_dict = {}
        # O(N) one pas
        for i in range(len(nums)):
            # We calculate a bucket index containing nums[i]
            remainder = nums[i] % (t + 1)
            bucket = (nums[i] - remainder) / (t+1)
            # Checking cache for duplicates
            if bucket in bucket_dict:
                return True # We found two values in the same bucket
            if bucket - 1 in bucket_dict and abs(nums[i] - bucket_dict[bucket - 1]) <= t:
                return True # Two values in adjacent buckets and nearby values
            if bucket + 1 in bucket_dict and abs(nums[i] - bucket_dict[bucket + 1]) <= t:
                return True # Two values in adjacent buckets and nearby values
            # Adding new bucket to cache
            if i >= k: # Maximal cache size is equal to k
                bucket_to_remove = bucket_cache.popleft()
                del bucket_dict[bucket_to_remove]
            bucket_cache.append(bucket)
            bucket_dict[bucket] = nums[i]
            #print(bucket_cache)
            #print(bucket_dict)
        return False
