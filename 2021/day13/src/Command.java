public class Command {
    public String dir;
    public int val;

    public Command(String dir, int val){
        this.dir = dir;
        this.val = val;
    }

    @Override
    public String toString() {
        return dir + " -> " + val;
    }
}
