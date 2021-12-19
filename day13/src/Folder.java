import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;

public class Folder {
    private Point[][] points;
    private ArrayList<Command> commands;
    private int maxX;
    private int maxY;

    public Folder(String filename){
        formatData(filename);
    }


    @Override
    public String toString() {
        String ret = "";
        for(int y = 0; y <= maxY; y++){
            for(int x = 0; x <= maxX; x++){
                ret += points[x][y];
            }
            ret += "\n";
        }
        return ret;
    }


    public int countPoints(){
        int total = 0;
        for(int x = 0; x <= maxX; x++){
            for(int y = 0; y <= maxY; y++){
                if(points[x][y].getValue().equals("#")){
                    total += 1;
                }
            }
        }
        return total;
    }


    public void fold(Command comm){
        if(comm.dir.equals("x"))
        {
            Point[][] newPoints = new Point[comm.val][maxY+1];
            for(int x = 0; x < comm.val; x++){
                for(int y = 0; y <= maxY; y++){
                    newPoints[x][y] = points[x][y];
                }
            }
            int newx = comm.val-1;
            for(int x = comm.val+1; x <= maxX; x++){
                for(int y = 0; y <= maxY; y++){
                    if(points[x][y].getValue() == "#"){
                        newPoints[newx][y] = new Point(newx, y, "#");
                    }
                }
                newx--;
            }
            this.points = newPoints;
            this.maxX = comm.val-1;

        }else if(comm.dir.equals("y"))
        {
            Point[][] newPoints = new Point[maxX+1][comm.val];
            for(int x = 0; x <= maxX; x++){
                for(int y = 0; y < comm.val; y++){
                    newPoints[x][y] = points[x][y];
                }
            }
            for(int x = 0; x <= maxX; x++){
                int newy = comm.val-1;
                for(int y = comm.val+1; y <= maxY; y++){
                    if(points[x][y].getValue() == "#"){
                        newPoints[x][newy] = new Point(x, newy, "#");
                    }
                    newy--;
                }
            }
            this.points = newPoints;
            this.maxY = comm.val-1;
        }
    }


    private void formatData(String datafile){
        // get data
        ArrayList<String> lines = new ArrayList<String>();
        ArrayList<Point> special_points = new ArrayList<Point>();
        try{
            Scanner scanner = new Scanner(new File("data.txt"));
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                lines.add(line);
            }
        }catch (Exception e){
            System.out.println(e);
        }
        // get points
        int i = 0;
        this.maxX = 0;
        this.maxY = 0;
        while(!lines.get(i).isEmpty()){
            int x = Integer.parseInt(lines.get(i).split(",")[0]);
            int y = Integer.parseInt(lines.get(i).split(",")[1]);
            special_points.add(new Point(x, y, "#"));

            this.maxX = x > maxX ? x : maxX;
            this.maxY = y > maxY ? y : maxY;
            i++;
        }
        // get commands
        this.commands = new ArrayList<Command>();
        for(i = i+1; i < lines.size(); i++){
            String dir = lines.get(i).substring(11, 12);
            int val = Integer.parseInt(lines.get(i).substring(13));
            this.commands.add(new Command(dir, val));
        }
        // load points in
        this.points = new Point[maxX+1][maxY+1];
        for(int x = 0; x <= maxX; x++){
            for(int y = 0; y <= maxY; y++){
                this.points[x][y] = new Point(x, y, ".");
            }
        }
        for(Point p : special_points){
            this.points[p.getX()][p.getY()] = p;
        }

    }


    public static void main(String[] args) {
        Folder f = new Folder("data.txt");
        for(Command c : f.commands){
            f.fold(c);
        }
        System.out.println(f);
    }
}
