import os


def main():
    out = open("detailed_report.csv", "w+")
    list_of_buildings = []
    list_of_calls = []

    out.write("building, calls file, avg_time, uncompleted_calls, certificate\n")
    for root, dirs, files in os.walk("Ex1_Buildings"):
        for file in files:
            list_of_buildings.append(os.path.join(root, file))
    for root, dirs, files in os.walk("Ex1_Calls"):
        for file in files:
            list_of_calls.append(os.path.join(root, file))
    i = 0
    for b in list_of_buildings:
        for c in list_of_calls:
            if os.system("python3 Ex1.py {} {} out.csv".format(b, c)):
                raise "help"
            if os.system("java -jar Ex1_checker_V1.2_obf.jar 319645735,208640326 {} out.csv out.log".format(b)):
                raise "help"
            avg_time, uncompleted_calls, certificate = analyze_log()
            out.write("{},{},{},{},{}\n".format(b, c, avg_time, uncompleted_calls, certificate))
            i += 1
    print(i)
    out.close()


def analyze_log():
    with open('out.log', 'r') as f:
        last_line = f.readlines()[-1].split(",")
        avg_time = last_line[1].split(":")[1].strip()
        uncompleted_calls = last_line[3].strip()
        certificate = last_line[5].strip()
    return avg_time, uncompleted_calls, certificate


if __name__ == "__main__":
    main()
