import pypass.auth as auth
import pypass.cli as cli

def main():
    print("PyPass")
    while not auth.authenticate_user():
        pass
    password = cli.prompt_generate_password()
    username = cli.prompt_username()
    print(f"{username}: {password}")
    cli.store_password(username, password)


if __name__ == "__main__":
    main()
