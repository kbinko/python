import java.lang.Math;

public class Lab3Z4 {
    public static void main(String[] args) {
        double x = 5.5, y = 3.5;

        System.out.println("abs: " + Math.abs(x));
        System.out.println("addExact: " + Math.addExact((int)x, (int)y));
        System.out.println("copySign: " + Math.copySign(x, y));
        System.out.println("decrementExact: " + Math.decrementExact((int)x));
        System.out.println("expm1: " + Math.expm1(x));
        System.out.println("floorDiv: " + Math.floorDiv((int)x, (int)y));
        System.out.println("floorMod: " + Math.floorMod((int)x, (int)y));
        System.out.println("getExponent: " + Math.getExponent(x));
        System.out.println("hypot: " + Math.hypot(x, y));
        System.out.println("IEEERemainder: " + Math.IEEEremainder(x, y));
        System.out.println("incrementExact: " + Math.incrementExact((int)x));
        System.out.println("max: " + Math.max(x, y));
        System.out.println("min: " + Math.min(x, y));
        System.out.println("multiplyExact: " + Math.multiplyExact((int)x, (int)y));
        System.out.println("negateExact: " + Math.negateExact((int)x));
        System.out.println("nextDown: " + Math.nextDown(x));
        System.out.println("nextUp: " + Math.nextUp(x));
        System.out.println("nextAfter: " + Math.nextAfter(x, y));
        System.out.println("random: " + Math.random());
        System.out.println("rint: " + Math.rint(x));
        System.out.println("scalb: " + Math.scalb(x, (int)y));
        System.out.println("signum: " + Math.signum(x));
        System.out.println("subtractExact: " + Math.subtractExact((int)x, (int)y));
        System.out.println("toDegrees: " + Math.toDegrees(x));
        System.out.println("toIntExact: " + Math.toIntExact((long)x));
        System.out.println("toRadians: " + Math.toRadians(x));
        System.out.println("ulp: " + Math.ulp(x));
    }
}
