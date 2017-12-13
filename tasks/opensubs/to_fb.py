import sys

if __name__ == '__main__':
    source = sys.argv[1]
    target = sys.argv[2]
    
    with open(source) as s:
        with open(target, "w") as t:
            for line in s:
                if line.startswith("U"):
                    t.write("1 " + line[3:-1])
                elif line.startswith("S"):
                    t.write("\t" + line[3:])
