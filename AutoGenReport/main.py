import sys
import get_csv.csv_main as csv_main


def main():
    print("starting Sheets parser")
    args = sys.argv[1:]
    print(f"running with args: {args}")
    if len(args) < 1:
        print("Error: no command provided")
        return
    if args[0] == "loadCSV":
        if len(args) < 2:
            print("Error: no file location provided")
            return
        csv_main.get_csv_runner(args[1])


if __name__ == "__main__":
    main()
