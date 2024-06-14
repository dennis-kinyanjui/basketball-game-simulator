import click
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
import app.crud as crud
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
def cli():
    pass

@cli.command()
def init_db():
    """Initialize the database."""
    Base.metadata.create_all(engine)
    console.print("Database initialized.", style="cyan")

@cli.command()
def create_team_cmd():
    """Create a new team."""
    db: Session = SessionLocal()
    name = click.prompt('Team name')
    city = click.prompt('Team city')
    team = crud.create_team(db, name=name, city=city)
    console.print(f'Team created: [bold blue]ID={team.id}, Name={team.name}, City={team.city}, Score={team.score}[/bold blue]')

@cli.command()
def list_teams_cmd():
    """List all teams."""
    db: Session = SessionLocal()
    teams = crud.get_teams(db)
    
    table = Table(title="Teams", style="green")  # Setting title style to green
    table.add_column("ID", style="yellow")
    table.add_column("Name", style="cyan")
    table.add_column("City", style="green")
    table.add_column("Score", style="magenta")

    for team in teams:
        table.add_row(
            f"[yellow]{team.id}[/yellow]",
            f"[cyan]{team.name}[/cyan]",
            f"[green]{team.city}[/green]",
            f"[magenta]{team.score}[/magenta]"
        )

    console.print(table)

@cli.command()
def delete_team_cmd():
    """Delete a team by ID."""
    db: Session = SessionLocal()
    team_id = click.prompt('Team ID', type=int)
    team = crud.delete_team(db, team_id)
    if team:
        console.print(f'Team deleted: [bold blue]ID={team.id}, Name={team.name}, City={team.city}, Score={team.score}[/bold blue]')
    else:
        console.print(f'Team with ID={team_id} not found.', style="bold red")

@cli.command()
def create_player_cmd():
    """Create a new player."""
    db: Session = SessionLocal()
    name = click.prompt('Player name')
    position = click.prompt('Player position')
    team_id = click.prompt('Team ID', type=int)
    player = crud.create_player(db, name=name, position=position, team_id=team_id)
    console.print(f'Player created: [bold blue]ID={player.id}, Name={player.name}, Position={player.position}, Team ID={player.team_id}[/bold blue]')

@cli.command()
def list_players_cmd():
    """List all players."""
    db: Session = SessionLocal()
    players = crud.get_players(db)

    table = Table(title="Players", style="cyan")  # Setting title style to cyan
    table.add_column("ID", style="yellow")
    table.add_column("Name", style="cyan")
    table.add_column("Position", style="green")
    table.add_column("Team ID", style="magenta")

    for player in players:
        table.add_row(
            f"[yellow]{player.id}[/yellow]",
            f"[cyan]{player.name}[/cyan]",
            f"[green]{player.position}[/green]",
            f"[magenta]{player.team_id}[/magenta]"
        )

    console.print(table)

@cli.command()
def delete_player_cmd():
    """Delete a player by ID."""
    db: Session = SessionLocal()
    player_id = click.prompt('Player ID', type=int)
    player = crud.delete_player(db, player_id)
    if player:
        console.print(f'Player deleted: [bold blue]ID={player.id}, Name={player.name}, Position={player.position}, Team ID={player.team_id}[/bold blue]')
    else:
        console.print(f'Player with ID={player_id} not found.', style="bold red")

@cli.command()
def create_game_cmd():
    """Simulate a new game."""
    db: Session = SessionLocal()
    team1_id = click.prompt('Team 1 ID', type=int)
    team2_id = click.prompt('Team 2 ID', type=int)
    game = crud.create_game(db, team1_id, team2_id)
    console.print(f'Game created: [bold blue]ID={game.id}, Team 1 ID={game.team1_id} Score={game.team1_score}, Team 2 ID={game.team2_id} Score={game.team2_score}, Winner ID={game.winner}[/bold blue]')

@cli.command()
def list_games_cmd():
    """List all games."""
    db: Session = SessionLocal()
    games = crud.get_games(db)

    table = Table(title="Games", style="magenta")  # Setting title style to magenta
    table.add_column("ID", style="yellow")
    table.add_column("Team 1 Name", style="cyan")
    table.add_column("Team 1 Score", style="green")
    table.add_column("Team 2 Name", style="magenta")
    table.add_column("Team 2 Score", style="cyan")
    table.add_column("Winner Team Name", style="red")

    for game in games:
        team1_name = crud.get_team(db, game.team1_id).name if game.team1_id else "N/A"
        team2_name = crud.get_team(db, game.team2_id).name if game.team2_id else "N/A"
        winner_name = crud.get_team(db, game.winner).name if game.winner else "N/A"

        table.add_row(
            f"[yellow]{game.id}[/yellow]",
            f"[cyan]{team1_name}[/cyan]",
            f"[green]{game.team1_score}[/green]",
            f"[magenta]{team2_name}[/magenta]",
            f"[cyan]{game.team2_score}[/cyan]",
            f"[red]{winner_name}[/red]"
        )

    console.print(table)

@cli.command()
def delete_game_cmd():
    """Delete a game by ID."""
    db: Session = SessionLocal()
    game_id = click.prompt('Game ID', type=int)
    game = crud.delete_game(db, game_id)
    if game:
        console.print(f'Game deleted: [bold blue]ID={game.id}, Team 1 ID={game.team1_id}, Team 2 ID={game.team2_id}[/bold blue]')
    else:
        console.print(f'Game with ID={game_id} not found.', style="bold red")

if __name__ == '__main__':
    cli()
