import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;

public class HeightMap {
    private int[][] heights;
    private ArrayList<Integer[]> lowPoints;

    public HeightMap(int[][] nums){
        heights = nums;
        this.findLowPoints();
    }

    public int getRiskSum(){
        int total = 0;
        for(Integer[] coord : lowPoints){
            total += heights[coord[0]][coord[1]] + 1;
        }
        return total;
    }

    // recursively get basin size from a low point
//    public int getBasinSize(int r, int c){
//        if(heights[r][c] == 9){
//            return 0;
//        }
//        if(heights[r][c].isMarked()){
//            return 0;
//        }
//        return 1 + getBasinSize(r+1, c) + getBasinSize(r-1, c) + getBasinSize(r, c+1) + getBasinSize(r, c-1);
//    }

    private void findLowPoints(){
        ArrayList<Integer[]> lp = new ArrayList<Integer[]>();
        Integer[] coord;

        for(int r = 0; r < heights.length; r++){
            for(int c = 0; c < heights[0].length; c++){
                coord = new Integer[2];
                coord[0] = r;
                coord[1] = c;
                if(isLowPoint(r, c)){
                    lp.add(coord);
                }
            }
        }
        lowPoints = lp;
    }

    private ArrayList<Integer[]> getValidNeighbors(int r, int c){
        Integer[] above = {r-1, c};
        Integer[] left = {r, c-1};
        Integer[] right = {r, c+1};
        Integer[] below = {r+1, c};

        // get valid comparable coords
        ArrayList<Integer[]> valid = new ArrayList<Integer[]>();

        if(above[0] >= 0){
            valid.add(above);
        }
        if(left[1] >= 0){
            valid.add(left);
        }
        if(right[1] < heights[0].length){
            valid.add(right);
        }
        if(below[0] < heights.length){
            valid.add(below);
        }

        return valid;
    }

    private boolean isLowPoint(int r, int c){
        int curVal = heights[r][c];
        // get valid comparable coords
        ArrayList<Integer[]> valid = getValidNeighbors(r, c);

        for(Integer[] coord : valid){
            if(curVal >= heights[coord[0]][coord[1]]){
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        // get data
        ArrayList<String> lines = new ArrayList<String>();
        try{
            Scanner scanner = new Scanner(new File("test.txt"));
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                lines.add(line);
            }
        }catch (Exception e){
            System.out.println(e);
        }
        int[][] heights = new int[lines.size()][lines.get(0).length()];
        for(int r = 0; r < lines.size(); r++){
            for(int c = 0; c < lines.get(0).length(); c++){
                heights[r][c] = Integer.parseInt(lines.get(r).substring(c, c+1));
            }
        }

        HeightMap hm = new HeightMap(heights);

        // PART 1
        System.out.println(hm.getRiskSum());

    }
}
