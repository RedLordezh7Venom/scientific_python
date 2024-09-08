def towersofhanoi(n,source,auxiliary,target):
    if n == 0:
        return 

    towersofhanoi(n-1,source,target,auxiliary)
    print(f'Move disk {n} from {source} to {target}')
    towersofhanoi(n-1,auxiliary,source,target)

print(towersofhanoi(3,'A','B','C'))