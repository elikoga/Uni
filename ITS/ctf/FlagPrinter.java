import org.apache.logging.log4j.Logger;
import java.util.Scanner;
import org.apache.logging.log4j.LogManager;

// 
// Decompiled by Procyon v0.6.0
// 

public class FlagPrinter
{
    public static void main(final String[] array) {
        try {
            final Logger logger = LogManager.getLogger((Class)FlagPrinter.class);
            System.out.println("Hello, please give us your flag for printing.");
            System.out.print("> ");
            final String next = new Scanner(System.in).next();
            if (next == System.getenv().getOrDefault("FLAG", null)) {
                System.out.println("Here is your flag: " + next);
            }
            else if (next.toLowerCase().contains("jndi")) {
                System.out.println("That is not your flag and hacking detected!!!");
                System.out.println("Nice try, but we are blocking `jndi` to prevent nasty logging exploits.");
                logger.warn("Stopped log4j exploit attempt, payload not logged for security reasons.");
            }
            else {
                System.out.println("That is not your flag! This incident will be logged!");
                logger.error("Wrong password: {}", (Object)next);
            }
        }
        catch (final Exception x) {
            System.err.println(x);
        }
    }
}
