public class Point {
    private int r;
    private int c;
    private boolean isMarked;
    private int value;

    public Point(int r, int c, int value){
        this.r = r;
        this.c = c;
        this.value = value;
        this.isMarked = false;
    }

    public void setMarked(boolean marked) {
        isMarked = marked;
    }

    public boolean isMarked() {
        return isMarked;
    }

    public int getC() {
        return c;
    }

    public int getR() {
        return r;
    }

    public int getValue() {
        return value;
    }

    @Override
    public String toString() {
        String ret = "";
        ret += "[" + this.getR() + "]";
        ret += "[" + this.getC() + "]";
        ret += " value: " + this.getValue() + "\n";
        return ret;
    }
}
