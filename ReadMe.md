# Basketball Game Simulator

This is a command-line application for managing a basketball game simulator. You can create and manage teams and players, and simulate games between teams using this CLI.

## Features

- Create, delete, and list teams.
- Create, delete, and list players.
- Assign players to teams.
- Simulate games between teams.
- List all simulated games.
- Find teams and players by their IDs.

## Setup

1. Install dependencies:
    ```sh
    pipenv install
    ```

2. Activate the virtual environment:
    ```sh
    pipenv shell
    ```

3. Initialize the database:
    ```sh
    python -m app.cli init-db
    ```


### Team Management

- Create a team:
    ```sh
    python -m app.cli create-team-cmd
    ```

- List all teams:
    ```sh
    python -m app.cli list-teams-cmd
    ```

- Delete a team:
    ```sh
    python -m app.cli delete-team-cmd
    ```

### Player Management

- Create a player:
    ```sh
    python -m app.cli create-player-cmd
    ```

- List all players:
    ```sh
    python -m app.cli list-players-cmd
    ```

- Delete a player:
    ```sh
    python -m app.cli delete-player-cmd
    ```

### Game Management

- Simulate a game between two teams:
    ```sh
    python -m app.cli create-game-cmd
    ```

- List all games:
    ```sh
    python -m app.cli list-games-cmd
    ```

## Example Commands

- Create a team:
    ```sh
    python -m app.cli create-team-cmd
    ```
    Follow the prompts to enter the team's name and city.

- List all teams:
    ```sh
    python -m app.cli list-teams-cmd
    ```
    This will display a list of all teams with their IDs, names, and cities.

- Create a player:
    ```sh
    python -m app.cli create-player-cmd
    ```
    Follow the prompts to enter the player's name, position, and team ID.

- Simulate a game:
    ```sh
    python -m app.cli create-game-cmd
    ```
    Follow the prompts to enter the IDs of the two teams that will play the game.


## Concusion

---

By following these instructions, you should be able to manage your basketball teams, players, and simulate games using the command-line interface.

## Acknowledgements

-  TM Nancy Umutoniwase
