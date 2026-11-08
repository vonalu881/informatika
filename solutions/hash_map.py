class HashMap:
    def __init__(self, size=10):
        self.size_buckets = size
        self.buckets = []
        for _ in range(self.size_buckets):
            self.buckets.append([])
        
        self.count = 0

    def __len__(self):
        return self.count

    def put(self, key, value):
        bucket_idx = hash(key) % self.size_buckets
        bucket = self.buckets[bucket_idx]
        
        for i in range(len(bucket)):
            kv_pair = bucket[i]
            if kv_pair[0] == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        bucket_idx = hash(key) % self.size_buckets
        bucket = self.buckets[bucket_idx]
        
        for kv_pair in bucket:
            if kv_pair[0] == key:
                return kv_pair[1]
        raise KeyError

    def remove(self, key):
        bucket_idx = hash(key) % self.size_buckets
        bucket = self.buckets[bucket_idx]
        
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self.count -= 1
                return
        raise KeyError

    def contains(self, key):
        bucket_idx = hash(key) % self.size_buckets
        bucket = self.buckets[bucket_idx]
        
        for kv_pair in bucket:
            if kv_pair[0] == key:
                return True
        return False
