# Ex1 OOP class - ariel CS

## brief overview

In this assigment we were requested to make an offline algorithm for a building with elevators. We were given a tester,
and some scenarios to try. Our algorithm used the same techniques as our
[online algorithm](https://github.com/Daniel-Ros/ex0/) from Ex0. It was a greedy algorithm that estimated the cost of
every call on every elevator, and the call would be given to the elevator that will loss less time.

## Folder Structure

The workspace contains two folders by default, where:

- `Ex1_Buildings`: the folder with all the building to the scenarios
- `Ex1_Calls`: the folder with all the calls files
- `.`: the folder with the code itself and the tester

## Testing

this project was test using the UniTest library. the tests can be run by an IDE of choice.

## Running the simulation

Make sure you have java (tested on 1.8.0_292) and python 3 install and configured on you machine. clone the project:

    git clone https://github.com/Daniel-Ros/OOP2.git
    python3 Ex1.py B1.json C2.csv out.csv
    java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 B1.json out.csv out.log

> you will have to change the B1.json C2.csv to a building/calls of you choice

or use the python script that runs all the results:

    git clone https://github.com/Daniel-Ros/OOP2.git
    python3 run_all.py

## Results

These are the final results that I was able to get
> There were some stages that I got a bit more, but really hurted other stages, soI had to balance it

|Case | Uncompleted calls | average waiting time per call|
|---|-------------------|------------------------------|
|0|0|23.19897426188186|
|1|4|34.79897426188186|
|2|5|51.09792822120195|
|3|2|42.5963457108327|
|4|2|42.07291073728415|
|5|17|72.77212115705177|
|6|15|55.12788209694845|
|7|47|224.5331211570514|
|8|23|131.51088209694842|
|9|5|46.30134007431241|

## Assigment Instructions

Google doc:[here](https://docs.google.com/document/d/1D4aW2vRaKjwtSBY1gDyCC6SNRE5TRGwMerGIXUMkI_Y/edit?usp=sharing)

Testing jar:[here](https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex1/libs)

GitHub: [project files](https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex1)

Google
Form: [here](https://docs.google.com/forms/d/e/1FAIpQLSffojCP9ftLSlk58_opDf-OpcLXvmuYzoQ3N_EQGtfozXjfjA/viewform?usp=sf_link)

Reported results (by
students) : [here](https://docs.google.com/spreadsheets/d/1fyFWvU_8d8UeaiUdyDujfgvt2dMs2mzzLd9QgUb33Wc/edit?usp=sharing)