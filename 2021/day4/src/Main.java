
public class Main {
    public static void main(String[] args) {
        DataFormatter d = new DataFormatter("data.txt");
        Board[] boards = d.getBoards();
        int[] callerNums = d.getCallerList();

        // PART 1
        int partOne = Board.getPartOneProduct(boards, callerNums);
        System.out.println(partOne);

        // PART 2
        int partTwo = Board.getLastWinnerProduct(boards, callerNums);
        System.out.println(partTwo);

    }
}
