nilapdrome = input()

cnt = 1

while nilapdrome != 'end':
    searched = nilapdrome[:cnt]
    while nilapdrome.find(searched, len(nilapdrome) - len(searched)) == -1 and cnt < len(nilapdrome) - 1:
        cnt += 1
        searched = nilapdrome[:cnt]

    core = nilapdrome[len(searched):len(nilapdrome) - len(searched)]
    if (searched + core + searched) == nilapdrome and len(core) != 0:
        print(core + searched + core)
    cnt = 1
    nilapdrome = input()
