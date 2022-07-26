""""day 2"""

def main():
    test = input()
    for cha in test:
        if cha.isupper():
            print(chr(65 - ord(cha)+90, end="")
            elif cha.islower():
            print(chr(97 - ord(cha)+122, end="")
                else:
            print(cha,end="")

main()
