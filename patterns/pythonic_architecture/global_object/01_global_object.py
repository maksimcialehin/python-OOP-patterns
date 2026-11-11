DATABASE_PORT = 5432
active_users = 0


def update_config(data: dict) -> None:
    global active_users
    new_active_users = data.get('active_users')
    if new_active_users >= 0:
        active_users = new_active_users
