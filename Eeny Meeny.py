
def main():
    l = len(list(map(str, input().split())))
    
    team1 = []
    team2 = []
    n = int(input())
    players = []
    
    for _ in range(n):
        players.append(input())

    toggle = True
    i = 0
    while players:
        size = len(players)
        if toggle:
            team1.append(players[(i + l - 1) % size])
            toggle = False
        else:
            team2.append(players[(i + l - 1) % size])
            toggle = True
        players.remove(players[(i + l - 1) % size])            
        i = (i + l - 1) % size

    print(len(team1))
    for player in team1:
        print(player)
    print(len(team2))
    for player in team2:
        print(player)
        
if __name__=="__main__":
    main()
