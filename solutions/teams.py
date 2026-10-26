def team_weights(weights):
    team1 = sum(weights[::2])
    team2 = sum(weights[1::2])
    return (team1, team2)
