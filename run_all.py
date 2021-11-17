import os


def main():
    list_of_buildings = []
    list_of_calls = []

    for root, dirs, files in os.walk("Ex1_Buildings"):
        for file in files:
            list_of_buildings.append(os.path.join(root, file))
    for root, dirs, files in os.walk("Ex1_Calls"):
        for file in files:
            list_of_calls.append(os.path.join(root, file))
    with open("detailed_report.csv", "w+") as out:
        out.write("building, calls file, avg_time, uncompleted_calls, certificate\n")
        for b in list_of_buildings:
            for c in list_of_calls:
                if os.system("python3 Ex1.py {} {} out.csv".format(b, c)):
                    raise "help"
                if os.system("java -jar Ex1_checker_V1.2_obf.jar 319645735,208640326 {} out.csv out.log".format(b)):
                    raise "help"
                avg_time, uncompleted_calls, certificate, sig = analyze_log()
                good_sig = '"' + sig.replace("\n", " ") + '"'
                print(sig)
                print(sig.__class__)
                out.write("{},{},{},{},{},{}\n".format(b, c, avg_time, uncompleted_calls, certificate, good_sig))


def analyze_log():
    with open('out.log', 'r') as f:
        sig = f.readlines()[-2:]
        last_line = sig[-1].split(",")
        avg_time = last_line[1].split(":")[1].strip()
        uncompleted_calls = last_line[3].strip()
        certificate = last_line[5].strip()
    return avg_time, uncompleted_calls, certificate, "".join(sig)

if __name__ == "__main__":
    main()
