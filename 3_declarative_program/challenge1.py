def wins_by_team(matches):
    teams = {winner for winner, _ in matches}
    return {team: {looser for winner, looser in matches if winner == team}
            for team in teams}
