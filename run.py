from app import app
import sys


def main(args: list) -> None:
    app.run(debug=True)


if __name__ == "__main__":
    args = sys.argv[1:]

    main(args)
