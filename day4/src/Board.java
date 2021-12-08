import java.util.ArrayList;

class Board {

    private Number[][] numbers;
    private boolean isWinningBoard;

    // takes array of 25 nums and puts them in board
    public Board(int[] nums){
        isWinningBoard = false;
        numbers = makeBoard(nums);
    }

    private Number[][] makeBoard(int[] nums){
        Number[][] retNums = new Number[5][5];

        for(int r = 0; r < 5; r++){
            for(int c = 0; c < 5; c++){
                retNums[r][c] = new Number(nums[(r * 5) + c]);
            }
        }

        return retNums;
    }

    // mark number and check if winning board
    public boolean markAndCheck(int i){
        for(int r = 0; r < 5; r++){
            for(int c = 0; c < 5; c++){
                if(numbers[r][c].getValue() == i){
                    numbers[r][c].setMarked(true);
                    this.isWinningBoard = checkWinning();
                }
            }
        }
        return isWinningBoard;
    }

    private boolean checkWinning(){
        int rowMarks = 0;
        int colMarks = 0;

        for(int r = 0; r < 5; r++){
            for(int c = 0; c < 5; c++){
                if(numbers[r][c].isMarked()){
                    rowMarks++;
                    if(rowMarks == 5){ return true; }
                }
            }
            boolean f;
            rowMarks = 0;
        }

        for(int c = 0; c < 5; c++){
            for(int r = 0; r < 5; r++){
                if(numbers[r][c].isMarked()){
                    colMarks++;
                    if(colMarks == 5){ return true; }
                }
            }
            colMarks = 0;
        }
        return false;
    }

    private ArrayList<Integer> getUnmarked(){
        ArrayList<Integer> ret = new ArrayList<Integer>();

        for(int r = 0; r < 5; r++){
            for(int c = 0; c < 5; c++){
                if(!numbers[r][c].isMarked()){
                    ret.add(numbers[r][c].getValue());
                }
            }
        }
        return ret;
    }

    public int getSumUnmarked(){
        int sum = 0;
        ArrayList<Integer> um = this.getUnmarked();

        for(Integer i : um){
            sum += i;
        }

        return sum;
    }

    @Override
    public String toString() {
        String ret = "";
        for(int r = 0; r < numbers.length; r++){
            ret += "[ ";
            for(int c = 0; c < numbers[0].length; c++){
                ret += numbers[r][c] + ", ";
            }
            ret += " ]\n";
        }
        return ret;
    }
}
