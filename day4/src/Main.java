
public class Main {
    public static void main(String[] args) {
        DataFormatter d = new DataFormatter("data.txt");

        Board[] boards = d.getBoards();
        int[] callerNums = d.getCallerList();

        for(int i : callerNums){
            for(Board b : boards){
                if(b.markAndCheck(i)){
                    int sumUnmarked = b.getSumUnmarked();
                    System.out.println(sumUnmarked * i);
                    System.exit(0);
                }
            }
        }
    }
}
