# authenticate.py


import click


@click.command()
def auth():
    """Provides user authenitcation."""
    username = click.prompt('username')
    password = click.prompt('password', hide_input=True, confirmation_prompt=True)

    if click.confirm('Are you and admin?'):
        admin_id = click.prompt('Admin ID', type=int, prompt_suffix='>')
        click.echo(f"Logging in admin {username} (ID = {admin_id})")
    else:
        click.echo(f"Logging in {username}")
