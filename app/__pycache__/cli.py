import click
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import (
    create_team,
    get_teams,
    get_team,
    delete_team,
    create_player,
    get_players,
    get_player,
    delete_player,
    create_game,
    get_games
)

@click.group()
def cli():
    pass

@cli.command()
def create_team():
    """Create a new team."""
    db: Session = SessionLocal()
    name = click.prompt('Team name')
    city = click.prompt('Team city')
    team = create_team(db, name=name, city=city)
    click.echo(f'Team created: ID={team.id}, Name={team.name}, City={team.city}, Score={team.score}')

@cli.command()
def list_teams():
    """List all teams."""
    db: Session = SessionLocal()
    teams = get_teams(db)
    for team in teams:
        click.echo(f'ID={team.id}, Name={team.name}, City={team.city}, Score={team.score}')

@cli.command()
def delete_team():
    """Delete a team by ID."""
    db: Session = SessionLocal()
    team_id = click.prompt('Team ID', type=int)
    team = delete_team(db, team_id)
    click.echo(f'Team deleted: ID={team.id}, Name={team.name}, City={team.city}, Score={team.score}')

@cli.command()
def create_player():
    """Create a new player."""
    db: Session = SessionLocal()
    name = click.prompt('Player name')
    position = click.prompt('Player position')
    team_id = click.prompt('Team ID', type=int)
    player = create_player(db, name=name, position=position, team_id=team_id)
    click.echo(f'Player created: ID={player.id}, Name={player.name}, Position={player.position}, Team ID={player.team_id}')

@cli.command()
def list_players():
    """List all players."""
    db: Session = SessionLocal()
    players = get_players(db)
    for player in players:
        click.echo(f'ID={player.id}, Name={player.name}, Position={player.position}, Team ID={player.team_id}')

@cli.command()
def delete_player():
    """Delete a player by ID."""
    db: Session = SessionLocal()
    player_id = click.prompt('Player ID', type=int)
    player = delete_player(db, player_id)
    click.echo(f'Player deleted: ID={player.id}, Name={player.name}, Position={player.position}, Team ID={player.team_id}')

@cli.command()
def create_game():
    """Simulate a new game."""
    db: Session = SessionLocal()
    team1_id = click.prompt('Team 1 ID', type=int)
    team2_id = click.prompt('Team 2 ID', type=int)
    game = create_game(db, team1_id, team2_id)
    click.echo(f'Game created: ID={game.id}, Team 1 ID={game.team1_id} Score={game.team1_score}, Team 2 ID={game.team2_id} Score={game.team2_score}, Winner ID={game.winner}')

@cli.command()
def list_games():
    """List all games."""
    db: Session = SessionLocal()
    games = get_games(db)
    for game in games:
        click.echo(f'ID={game.id}, Team 1 ID={game.team1_id} Score={game.team1_score}, Team 2 ID={game.team2_id} Score={game.team2_score}, Winner ID={game.winner}')

if __name__ == '__main__':
    cli()
