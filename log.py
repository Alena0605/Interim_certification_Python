from datetime import datetime as dt


def logg(text, result):
    date = dt.now().strftime('%Y-%m-%d %A %H:%M')
    with open("logg.csv", "a", encoding="utf-8") as f:
        f.write(f"{date}:  Operation: {text}  ->  Result: {result}\n")
