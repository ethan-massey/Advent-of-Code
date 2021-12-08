
class Board {

    private Number numbers[][];

    // takes array of 25 nums and puts them in board
    public Board(int[] nums){

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
