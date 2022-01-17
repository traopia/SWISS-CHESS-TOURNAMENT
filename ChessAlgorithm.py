#ASSIGNMENT 2

#from unit_tester import test

class player_result:
    def __init__(self, name: str, points: float, resistance_points: float, sonnenborn_berger: float, black: int):
        self.name = name
        self.points = points
        self.resistance_points = resistance_points
        self.sonnenborn_berger = sonnenborn_berger
        self.black = black

    def __str__(self):
        return 'player_result(name=\'' + self.name + '\', points=' + str(self.points) + ', resistance_points=' + \
               str(self.resistance_points) + ', sonnenborn_berger=' + str(self.sonnenborn_berger) + \
               ', black=' + str(self.black) + ')'

    def __eq__(self, other):
        return self.name == other.name and self.points == other.points and \
               self.resistance_points == other.resistance_points and \
               self.sonnenborn_berger == other.sonnenborn_berger and self.black == other.black

#function
def determine_output(input: str):
    s=inputt.split("\n\n")
    player_result.name=str(s[0]).split("\n")
    rounds=s[1:]
    res = []
    for el in rounds:
        sub = el.split(', ')
        res.append(sub)
        
    r=[]
    for el in res:
        for i in el:
            sub = i.split('\n')
            r.append(sub)  
    rr=[]
    for el in r:
        for i in el:
                sub = i.split(' ')
                rr.append(sub) 
    #rr is the input that can be managed            
    #points

    win={key: [] for key in player_result.name}
    tie={key: [] for key in player_result.name}
    lose={key: [] for key in player_result.name}

    for el in rr:
                for k,v in win.items():
                    if k==el[0]:
                        if el[2]=="1":
                            win[k].append(1)
                        else:
                            win[k].append(0)    
                    elif k==el[1]:
                        if el[3]=="1":
                            win[k].append(1)
                        else:
                            win[k].append(0)
    win={key:sum(l_values) for key, l_values in win.items()}                         
    for el in rr:
                for k,v in tie.items():
                    if k==el[0]:
                        if el[2]=="0.5":
                            tie[k].append(0.5)
                        else:
                            tie[k].append(0)    
                    elif k==el[1]:
                        if el[3]=="0.5":
                            tie[k].append(0.5)
                        else:
                            tie[k].append(0)
    tie={key:sum(l_values) for key, l_values in tie.items()}                       
    for el in rr:
                for k,v in lose.items():
                    if k==el[0]:
                        if el[2]=="0":
                            lose[k].append(0)
                        else:
                            lose[k].append(0)    
                    elif k==el[1]:
                        if el[3]=="0":
                            lose[k].append(0)
                        else:
                            lose[k].append(0) 
    lose={key:sum(l_values) for key, l_values in lose.items()}   

    points={key: [] for key in player_result.name}

    for k,v in win.items():
        for kk,vv in tie.items():
            for kkk,vvv in lose.items():
                for j,l in points.items():
                    if k==kk==kkk==j:
                        points[j]=v+vv+vvv
    print(points)

    #resistance
    rp={key: [] for key in player_result.name}


    for el in rr:
        for k,v in rp.items():
            if k==el[0]:
                rp[k].append(el[1])
            if k==el[1]:
                rp[k].append(el[0])
    vs=rp
    #print(vs)
    lrp=list(rp.items())

    for v in range(len(lrp)):
        for l in range(len(rounds)):
            for kk,vv in list(d.items()):
                if lrp[v][1][l]==kk:
                    lrp[v][1][l]=vv

    dlrp = {key:sum(l_values) for key, l_values in rp.items()}
    print(dlrp)

    #sonnenberg

    win1={key: [] for key in player_result.name}
    tie1={key: [] for key in player_result.name}
    lose1={key: [] for key in player_result.name}

    for el in rr:
                for k,v in win1.items():
                    if k==el[0]:
                        if el[2]=="1":
                            win1[k].append(el[1])
                        else:
                            win1[k].append(0)    
                    elif k==el[1]:
                        if el[3]=="1":
                            win1[k].append(el[0])
                        else:
                            win1[k].append(0)    

    for el in rr:
                for k,v in tie1.items():
                    if k==el[0]:
                        if el[2]=="0.5":
                            tie1[k].append(el[1])
                        else:
                            tie1[k].append(0)    
                    elif k==el[1]:
                        if el[3]=="0.5":
                            tie1[k].append(el[0]) 
                        else:
                            tie1[k].append(0)     
                
    for el in rr:
                for k,v in lose1.items():
                    if k==el[0]:
                        if el[2]=="0":
                            lose1[k].append(el[1])
                        else:
                            lose1[k].append(0)
                    elif k==el[1]:
                        if el[3]=="0":
                            lose1[k].append(el[0])
                        else:
                            lose1[k].append(0)    
     

    win1=list(win1.items())  
    tie1=list(tie1.items())
    lose1=list(lose1.items())


    for v in range(len(win1)):
        for l in range(len(rounds)):
            for kk,vv in list(d.items()):
                if win1[v][1][l]==kk:
                    win1[v][1][l]=vv
    win1=dict(win1)                
    win1 = {key:sum(l_values) for key, l_values in win1.items()}                
                    
    for v in range(len(tie1)):
        for l in range(len(rounds)):
            for kk,vv in list(d.items()):
                if tie1[v][1][l]==kk:
                    tie1[v][1][l]=0.5*vv
    tie1=dict(tie1)                
    tie1 = {key:sum(l_values) for key, l_values in tie1.items()}

    for v in range(len(lose1)):
        for l in range(len(rounds)):
            for kk,vv in list(d.items()):
                if lose1[v][1][l]==kk:
                    lose1[v][1][l]=0*vv 
    lose1=dict(lose1)                
    lose1 = {key:sum(l_values) for key, l_values in lose1.items()}                


    sb={key: [] for key in player_result.name}

    for k,v in win1.items():
        for kk,vv in tie1.items():
            for kkk,vvv in lose1.items():
                for j,l in sb.items():
                    if k==kk==kkk==j:
                        sb[j]=v+vv+vvv
    print(sb)

    #black
    black={key: [] for key in player_result.name}
    for el in rr:
        for k,v in black.items():
            if k==el[1]:
                black[k].append(1)
    black={key:sum(l_values) for key, l_values in black.items()} 

    print(black)

    return(points,dlrp, sb, black)






