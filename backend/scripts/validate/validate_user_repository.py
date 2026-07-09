from validators.user_repository_validator import UserRepositoryValidator


def main() -> None:

    validator = UserRepositoryValidator()

    validator.run()


if __name__ == "__main__":
    main()
