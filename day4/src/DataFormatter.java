import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;

class DataFormatter{

    private Board[] boards;
    private int[] callerList;


    public DataFormatter(String filename){
        processFile(filename);
    }

    private void processFile(String filename){
        ArrayList<String> lines = new ArrayList<String>();
        try{
            Scanner scanner = new Scanner(new File(filename));
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                lines.add(line);
            }
        }catch (Exception e){
            System.out.println(e);
        }

        // Get caller list
        String[] stringCallerList = lines.get(0).split(",");
        callerList = new int[stringCallerList.length];
        for(int i = 0; i < callerList.length; i++){
            callerList[i] = Integer.parseInt(stringCallerList[i]);
        }

        // format board nums into single int array
        lines = new ArrayList<String>(lines.subList(2, lines.size()));
        String linesAsString = "";
        for(int i = 0; i < lines.size(); i++){
            linesAsString += lines.get(i).length() == 0 ? " " : lines.get(i) + " ";
        }
        String[] stringNums = linesAsString.split("\\s+");
        int[] allBoardNums = new int[stringNums.length];
        for(int i = 0; i < stringNums.length; i++){ allBoardNums[i] = Integer.parseInt(stringNums[i]); }

        // make boards
        int numBoards = allBoardNums.length / 25;
        this.boards = new Board[numBoards];

        for(int i = 0; i < numBoards; i++){
            this.boards[i] = new Board(Arrays.copyOfRange(allBoardNums, i * 25, (i*25) + 25));
        }

    }

    public Board[] getBoards() {
        return boards;
    }

    public int[] getCallerList() {
        return callerList;
    }

    @Override
    public String toString() {
        String ret = "";

        for(int i : callerList){
            ret += i + ", ";
        }
        ret += "\n\n";

        for(Board b : boards){
            ret += b.toString() + "\n";
        }

        return ret;
    }
}