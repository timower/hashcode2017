params = input().split(' ')
V = int(params[0])
E = int(params[1])
R = int(params[2])
C = int(params[3])
X = int(params[4])

min_vid_size = 0
video_sizes = list(map(lambda x: int(x), input().split(' ')))
assert len(video_sizes) == V
min_vid_size = min(video_sizes)

#print(sum(video_sizes))

cache_info = {}
endpoints = []
for i in range(E):
    line = input().split(' ')
    L_d = int(line[0])
    K = int(line[1])
    caches = []
    for j in range(K):
        line = input().split(' ')
        cache = int(line[0])
        L_c = int(line[1])
        caches.append((cache, L_c))
        if cache in cache_info:
            cache_info[cache][i] = L_c
        else:
            cache_info[cache] = {i: L_c}
    endpoints.append((L_d, caches))

video_reqs = dict()
endpoint_reqs = dict()

for i in range(R):
    line = input().split(' ')
    
    video_id = int(line[0])
    endpoint_id = int(line[1])
    requests = int(line[2])
    
    if endpoint_id in endpoint_reqs:
        endpoint_reqs[endpoint_id].append((video_id, requests))
    else:
        endpoint_reqs[endpoint_id] = [(video_id, requests)]

    if video_id in video_reqs:
        video_reqs[video_id].append((endpoint_id, requests))
    else:
        video_reqs[video_id] = [(endpoint_id, requests)]


print(C)
for c in range(C):
    s = 0
    res = []
    i = 0
    while s < X and i < V:
        size = video_sizes[i]
        if size != -1 and s + size < X:
            video_sizes[i] = -1
            s += size
            res.append(str(i))
        i += 1
    print(str(c) + " " + " ".join(res))
    