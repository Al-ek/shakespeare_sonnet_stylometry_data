import re

with open("allsonnets.txt", "r", encoding="utf-8") as f:
    text = f.read()

parts = re.split(r'^\s*([IVXLCDM]+)\s*$', text, flags=re.MULTILINE)

parts = parts[1:]

for i in range(0, len(parts), 2):
    numeral = parts[i]
    sonnet_text = parts[i + 1].strip()

    filename = f"individualSonnets/sonnet_{i//2 + 155}.txt"
    with open(filename, "w", encoding="utf-8") as out:
        out.write(numeral + "\n\n")
        out.write(sonnet_text)

print("Done! Sonnets split into individual files.")

