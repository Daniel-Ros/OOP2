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

or use the python script that runs all the combination of building/calls that are in the correct folders:

    git clone https://github.com/Daniel-Ros/OOP2.git
    python3 run_all.py

then a file name `detailed_report.csv`will appear with all the building/calls combination runs
## Results

These are the final results that I was able to get
> There were some stages that I got a bit more, but really hurted other stages, soI had to balance it

|building| calls file| avg_time| uncompleted_calls| certificate|
|---|-----|----|----|----|
|Ex1_Buildings/B4.json|Ex1_Calls/Calls_d.csv|181.59887473199998|2|-1029780052|
|Ex1_Buildings/B4.json|Ex1_Calls/Calls_a.csv|21.39|0|-477245372|
|Ex1_Buildings/B4.json|Ex1_Calls/Calls_b.csv|182.77930438399991|8|-1029079617|
|Ex1_Buildings/B4.json|Ex1_Calls/Calls_c.csv|188.049190305|1|-1049811266|
|Ex1_Buildings/B3.json|Ex1_Calls/Calls_d.csv|538.7704245020027|97|-1988858225|
|Ex1_Buildings/B3.json|Ex1_Calls/Calls_a.csv|31.52|0|-507592314|
|Ex1_Buildings/B3.json|Ex1_Calls/Calls_b.csv|566.305679903997|123|-1821234212|
|Ex1_Buildings/B3.json|Ex1_Calls/Calls_c.csv|549.042974835004|147|-1768929484|
|Ex1_Buildings/B5.json|Ex1_Calls/Calls_d.csv|36.024|0|-524830233|
|Ex1_Buildings/B5.json|Ex1_Calls/Calls_a.csv|17.18|0|-459240568|
|Ex1_Buildings/B5.json|Ex1_Calls/Calls_b.csv|34.967|0|-517942067|
|Ex1_Buildings/B5.json|Ex1_Calls/Calls_c.csv|35.137|0|-521468334|
|Ex1_Buildings/B1.json|Ex1_Calls/Calls_d.csv|1841.6984976999543|950|-4422944342|
|Ex1_Buildings/B1.json|Ex1_Calls/Calls_a.csv|112.92|0|-254611173|
|Ex1_Buildings/B1.json|Ex1_Calls/Calls_b.csv|1784.2436402240376|963|-4812623036|
|Ex1_Buildings/B1.json|Ex1_Calls/Calls_c.csv|1839.3603121899735|958|-4474949366|
|Ex1_Buildings/B2.json|Ex1_Calls/Calls_d.csv|1840.5214976999544|950|-4427977959|
|Ex1_Buildings/B2.json|Ex1_Calls/Calls_a.csv|53.8|0|-315129308|
|Ex1_Buildings/B2.json|Ex1_Calls/Calls_b.csv|1783.2816402240373|963|-4813976071|
|Ex1_Buildings/B2.json|Ex1_Calls/Calls_c.csv|1838.0983121899735|958|-4470029667|

## Assigment Instructions

Google doc:[here](https://docs.google.com/document/d/1D4aW2vRaKjwtSBY1gDyCC6SNRE5TRGwMerGIXUMkI_Y/edit?usp=sharing)

Testing jar:[here](https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex1/libs)

GitHub: [project files](https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex1)

Google
Form: [here](https://docs.google.com/forms/d/e/1FAIpQLSffojCP9ftLSlk58_opDf-OpcLXvmuYzoQ3N_EQGtfozXjfjA/viewform?usp=sf_link)

Reported results (by
students) : [here](https://docs.google.com/spreadsheets/d/1fyFWvU_8d8UeaiUdyDujfgvt2dMs2mzzLd9QgUb33Wc/edit?usp=sharing)