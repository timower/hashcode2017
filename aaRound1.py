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

# print(sum(video_sizes))

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

endpoint_total_reqs = [0] * R

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
    
    endpoint_total_reqs[i] += requests

print(C)

video_cahces = []
for i in range(V):
    video_cahces.append(set())

sorted_caches = list(range(C))
sorted_caches.sort(key = lambda c: sum([0.85 * cache_info[c][x] * endpoint_total_reqs[x] for x in cache_info[c]])  / len(cache_info[c]) * R)

# per cache
for i in sorted_caches:
    # endpoints die verbonden zijn:
    cache_ends = cache_info[i]
    videos = [0] * V

    for endpoint_id in cache_ends:
        latency = cache_ends[endpoint_id]
        # endpoint moet request maken:
        if endpoint_id not in endpoint_reqs:
            continue
        # voor elke request voeg aantal requests toe aan bijhorende video
        for request in endpoint_reqs[endpoint_id]:
            video_id = request[0]
            caches_this_endpoint = endpoints[endpoint_id][1]
            ass = True
            for c in video_cahces[video_id]:
                info = cache_info[c]
                if endpoint_id in info:
                    L = info[endpoint_id]
                    if L < latency:
                        ass = False
                        break
            if ass:
                videos[video_id] += request[1] * (endpoints[endpoint_id][0] - latency)
    for v in range(V):
        videos[v] = (v, video_sizes[v], videos[v] / video_sizes[v])
    videos.sort(key = lambda x: x[2])
    result = []
    s = 0
    while s < X and len(videos) > 0 and X - s > min_vid_size:
        vid = videos.pop()
        if s + vid[1] > X:
            continue
        s += vid[1]
        result.append(vid[0])
    for video in result:
        video_cahces[video].add(i)
    print(str(i) + " " + " ".join(map(lambda x: str(x), result)))
        