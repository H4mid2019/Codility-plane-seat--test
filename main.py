import re


# B C  D E F G H  J K 



def helper(ls):
    lst = ''.join(ls)
    if 'D' and 'G' not in lst or 'H' and 'E' not in lst:
        return 0
    if 'B' and 'K' not in lst or 'C' and 'J' not in lst and 'D' and 'E' and 'F' and 'G' and 'H' in lst:
        return 1
    tc = 0
    for i in ls:
        if i == 'O':
            tc = 0
        if tc == 4:
            break
        tc += 1
        
    lc = 0
    if tc == 4:
        lc = 1
        
    return lc



def solution(N, S):
    st = re.sub('[\d][A]|[\d][L]','',S)
    si = st.strip().split(' ')
    sii = [x for x in si if x != ""]
    m=[[] for i in range(N)]

    for ls in range(N):
        l = list ((str(ls+1),'B'))
        lj = ''.join(l)
        m[ls].append(lj)
        l = list ((str(ls+1),'C'))
        lj = ''.join(l)
        m[ls].append(lj)
        l = list ((str(ls+1),'D'))
        lj = ''.join(l)
        m[ls].append(lj)
        l = list ((str(ls+1),'E'))
        lj = ''.join(l)
        m[ls].append(lj)
        l = list ((str(ls+1),'F'))
        lj = ''.join(l)
        m[ls].append(lj)
        l = list ((str(ls+1),'G'))
        lj = ''.join(l)
        m[ls].append(lj)
        l = list ((str(ls+1),'H'))
        lj = ''.join(l)
        m[ls].append(lj)
        l = list ((str(ls+1),'J'))
        lj = ''.join(l)
        m[ls].append(lj)
        l = list ((str(ls+1),'K'))
        lj = ''.join(l)
        m[ls].append(lj)
    
    for ii in range(N):
        for nn, iin in enumerate(m[ii]):
            if iin in sii:
                m[ii][nn] = 'O'
    
    counter = {}
    cc = 0
    for iii in m:
        counter[cc] = helper(iii)
        cc += 1




    return sum(counter.values())

print(solution(2,"1D 1G 2K"))
