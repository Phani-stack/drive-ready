
package methods;

public class Paytm implements Processable, Refundable, Validatable {

    @Override
    public void process() {
        System.out.println("methods.Paytm processing");
    }

    @Override
    public void refund() {
        System.out.println("methods.Paytm refunding");
    }

    @Override
    public void validate() {
        System.out.println("methods.Paytm validating");
    }
}
