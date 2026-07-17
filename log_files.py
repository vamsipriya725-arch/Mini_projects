from datetime import datetime
def record_login(username: str, status: str) -> None:
    timestamp = datetime.now().isoformat(timespec="seconds")

    log_message = (
        f"{timestamp} | username={username} | status={status}\n"
    )

    with open("login_activity.log", "a", encoding="utf-8") as file:
        file.write(log_message)
record_login("Priya ", "SUCCESS")
record_login("sanju", "FAILED")
