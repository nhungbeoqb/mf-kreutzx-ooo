import os

ENTRY = "I'm out of office until Monday \u2014 my laptop caught fire, my phone is at 2%, and this auto-reply is being sent from the smoke alarm."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
