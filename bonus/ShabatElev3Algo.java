package ex0.algo;

import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;

import ex0.Building;
import ex0.CallForElevator;
import ex0.Elevator;
import ex0.simulator.Elevator_A;


/**
 * A bit better than ShabatElev2Algo: randomly spread the elevators in the init
 * stage, allocate the "closest" elevator..
 */
public class ShabatElev3Algo implements ElevatorAlgo {

    private final Building building;
    private final ElevatorSupreviser[] eQueue;
    private int lastPos [];
    private Boolean[] isUp;
    private int lastStop = 0;

    public ShabatElev3Algo(Building b) {
        isUp = new Boolean[b.numberOfElevetors()];
        lastPos = new int[b.numberOfElevetors()];
        isUp[0] = true;
        building = b;
        eQueue = new ElevatorSupreviser[building.numberOfElevetors()];
        for (int i = 0; i < building.numberOfElevetors(); i++) {
            lastPos[i] = b.getElevetor(i).getPos();
            eQueue[i] = new ElevatorSupreviser();
                isUp[i] = false;
        }

        //load the csv
        loadData("out.csv");
        drawCanvas();
    }
    private final double TOP = 0.495 , BOTTOM = 0 , LEFT =0.1 ,RIGHT =0.9 , CENTER=0.5;

    private void drawCanvas(){
        double floors=building.maxFloor()-building.minFloor();
        double zero=0-building.minFloor();
        double numelev= (double) building.numberOfElevetors();
        StdDraw.setCanvasSize(1800, 900);
        //-------- SKY ------
        StdDraw.setPenColor(StdDraw.BOOK_LIGHT_BLUE);
        StdDraw.filledRectangle(CENTER,CENTER,1,1);
        //StdDraw.picture(0.05,0.9,"sunny.png",0.3,0.3);  //can be moved to proper folder
        //---- GRASS------
        StdDraw.setPenColor(StdDraw.GREEN);
        StdDraw.setPenRadius(0.04);
        StdDraw.filledRectangle(CENTER ,0.1, 0.5 ,0.1); /// should be heighted to around ground 0 floor
        //----BUILDING FILL-----
        StdDraw.setPenColor(StdDraw.GRAY);
        StdDraw.filledRectangle(CENTER,TOP,0.4 ,TOP);
        StdDraw.setPenRadius(0.0025);
        //----FLOOORS
        double dist=1/floors;
        double doorlocation=0;
        for (double i = 0; i<floors-1 ; i++){
            StdDraw.setPenColor(StdDraw.BLACK);
            if (floors<50) StdDraw.text(LEFT-0.025,0.01+i*dist,"Floor #"+(int) (i-zero)); //if too much floors text look like crap
            if (i==zero) {
                //-----DOOR & GROUND ZERO---- // door not working properly but there is the line doorlocation=0.01+dist;
                StdDraw.setPenColor(StdDraw.GREEN);
            } else StdDraw.setPenColor(StdDraw.BOOK_RED);
            StdDraw.line(LEFT,i*dist,RIGHT,i*dist);
        }
        //----ELEVATORS----
        StdDraw.setPenColor(StdDraw.BLACK);
        dist=(0.8/numelev); // 0.8 is working i guess because of width LEFT to RIGHT
        for (double i = 1; i < numelev+1; i++) {
            StdDraw.line(LEFT+dist*(i-1),BOTTOM,LEFT+dist*(i-1),TOP*2);
        }

        StdDraw.picture(0.05,0.3,"trees.png",0.1,0.3);
        StdDraw.picture(0.955,0.3,"trees.png",0.1,0.3);

    }

    @Override
    public Building getBuilding() {
        return building;
    }

    @Override
    public String algoName() {
        return "D^2 algo";
    }

    private ArrayList<Integer> elevator_alloc;
    private int idex; //באיזה מעלית אנחנו עכשיו


    private void loadData(String csv) {
        elevator_alloc = new ArrayList<Integer>();
        try (BufferedReader br = new BufferedReader(new FileReader(csv))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] lines = line.split(",");
                elevator_alloc.add(Integer.valueOf(lines[5]));
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    /**
     * this function allocates an elevator by calculating how much each elevator
     * would the to finish the job and picking this one
     */
    @Override
    public int allocateAnElevator(CallForElevator c) { return elevator_alloc.get(idex++);}

    /**
     * send each elevator to its next stop and checks if given elevator can stop on
     * its way there
     */
    @Override
    public void cmdElevator(int elev) {
        Elevator_A e = (Elevator_A) building.getElevetor(elev);
        double floors=building.maxFloor()-building.minFloor();
        int draw_id = e.getID();
        int draw_pos = e.getPos();
        double dist=(0.8/building.numberOfElevetors()); //

        for (var c:e.get_curr_calls()) {
            if(c.getState() == CallForElevator.GOING2SRC){
                StdDraw.setPenColor(StdDraw.BLUE);
                StdDraw.filledRectangle(LEFT+dist*(1+(draw_id*2))/2,BOTTOM + (1+((c.getSrc()-building.minFloor())*2))/(2*floors),(dist/(3)),(1/(floors)/3));
            }else{
                StdDraw.setPenColor(StdDraw.YELLOW);
                StdDraw.filledRectangle(LEFT+dist*(1+(draw_id*2))/2,BOTTOM + (1+((c.getDest()-building.minFloor())*2))/(2*floors),(dist/(3)),(1/(floors)/3));
            }
        }

        StdDraw.setPenColor(StdDraw.GRAY);
        StdDraw.filledRectangle(LEFT+dist*(1+(draw_id*2))/2,BOTTOM + (1+((lastPos[draw_id]-building.minFloor())*2))/(2*floors),(dist/(3)),(1/(floors)/3));
        StdDraw.setPenColor(StdDraw.GREEN);
        StdDraw.filledRectangle(LEFT+dist*(1+(draw_id*2))/2,BOTTOM + (1+((draw_pos-building.minFloor())*2))/(2*floors),(dist/(3)),(1/(floors)/(3)));
        lastPos[draw_id] = draw_pos;


        var calls = e.get_curr_calls();
        if (isUp[e.getID()]){
            ArrayList<Integer> floors_to_go = new ArrayList<Integer>();
            for (var c : calls) {
                int floor = c.getState() == CallForElevator.GOING2SRC ? c.getSrc() : c.getDest();
                if(floor > e.getPos())
                    floors_to_go.add(floor);
            }
            if(floors_to_go.size() == 0 && calls.size() != 0 ){
                isUp[e.getID()] = false;
            }
            if(floors_to_go.size() == 0){
                return;
            }
            floors_to_go.sort(Comparator.naturalOrder());
            if(e.getState() == Elevator.UP){
                e.stop(floors_to_go.get(0));
            }else{
                e.goTo(floors_to_go.get(0));
            }
        }else{
            ArrayList<Integer> floors_to_go = new ArrayList<Integer>();
            for (var c : calls) {
                int floor = c.getState() == CallForElevator.GOING2SRC ? c.getSrc() : c.getDest();
                if(floor < e.getPos())
                    floors_to_go.add(floor);
            }
            if(floors_to_go.size() == 0 && calls.size() != 0 ){
                isUp[e.getID()] = true;
            }
            if(floors_to_go.size() == 0){
                return;
            floors_to_go.sort(Comparator.reverseOrder());
            if(e.getState() == Elevator.UP){
                e.stop(floors_to_go.get(0));
            }else{
                e.goTo(floors_to_go.get(0));
            }
        }

    }
}


