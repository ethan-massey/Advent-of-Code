import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;

public class HeightMap {
    private Point[][] heights;
    private ArrayList<Point> lowPoints;

    public HeightMap(int[][] nums){
        this.initHeights(nums);
        this.findLowPoints();
    }

    private void initHeights(int[][] nums){
        heights = new Point[nums.length][nums[0].length];
        for(int r = 0; r < nums.length; r++){
            for(int c = 0; c < nums[0].length; c++){
                heights[r][c] = new Point(r, c, nums[r][c]);
            }
        }
    }

    public int getRiskSum(){
        int total = 0;
        for(Point p : lowPoints){
            total += p.getValue() + 1;
        }
        return total;
    }

    // recursively get basin size from a low point
    public int getBasinSize(int r, int c){
        if(!isValidPoint(r,c)){
            return 0;
        }
        if(heights[r][c].getValue() == 9){
            return 0;
        }
        if(heights[r][c].isMarked()){
            return 0;
        }
        heights[r][c].setMarked(true);
        return 1 + getBasinSize(r+1, c) + getBasinSize(r-1, c) + getBasinSize(r, c+1) + getBasinSize(r, c-1);
    }

    private boolean isValidPoint(int r, int c){
        if(r < 0 || r >= heights.length){
            return false;
        }
        else if(c < 0 || c >= heights[0].length){
            return false;
        }
        return true;
    }

    private void findLowPoints(){
        ArrayList<Point> lp = new ArrayList<Point>();
        Point coord;

        for(int r = 0; r < heights.length; r++){
            for(int c = 0; c < heights[0].length; c++){
                coord = new Point(r, c, heights[r][c].getValue());
                if(isLowPoint(r, c)){
                    lp.add(coord);
                }
            }
        }
        lowPoints = lp;
    }

    private ArrayList<Point> getValidNeighbors(int r, int c){
        // get valid comparable coords
        ArrayList<Point> valid = new ArrayList<Point>();

        if(r-1 >= 0){
            valid.add(new Point(r-1, c, heights[r-1][c].getValue()));
        }
        if(c-1 >= 0){
            valid.add(new Point(r, c-1, heights[r][c-1].getValue()));
        }
        if(c+1 < heights[0].length){
            valid.add(new Point(r, c+1, heights[r][c+1].getValue()));
        }
        if(r+1 < heights.length){
            valid.add(new Point(r+1, c, heights[r+1][c].getValue()));
        }

        return valid;
    }

    private boolean isLowPoint(int r, int c){
        int curVal = heights[r][c].getValue();
        // get valid comparable coords
        ArrayList<Point> valid = getValidNeighbors(r, c);

        for(Point p : valid){
            if(curVal >= heights[p.getR()][p.getC()].getValue()){
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        // get data
        ArrayList<String> lines = new ArrayList<String>();
        try{
            Scanner scanner = new Scanner(new File("data.txt"));
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

        // PART 2
        int max1 = 0;
        int max2 = 0;
        int max3 = 0;
        // get 3 largest basins
        for(Point p: hm.lowPoints){
            int basinSize = hm.getBasinSize(p.getR(), p.getC());
            if(basinSize > max1){
                max2 = max1;
                max1 = basinSize;
            }else if(basinSize > max2){
                max3 = max2;
                max2 = basinSize;
            }else if(basinSize > max3){
                max3 = basinSize;
            }
        }
        System.out.println(max1 * max2 * max3);
    }
}
