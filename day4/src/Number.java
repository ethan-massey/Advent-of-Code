public class Number {
    private boolean marked;
    private int value;

    public Number(int val){
        value = val;
        marked = false;
    }

    public int getValue() {
        return value;
    }

    public boolean isMarked() {
        return marked;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public void setMarked(boolean marked) {
        this.marked = marked;
    }

    @Override
    public String toString() {
        return String.valueOf(this.value);
    }
}