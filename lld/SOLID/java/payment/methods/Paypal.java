package methods;

import interfaces.*;

public class Paypal implements Processable, Refundable, Validatable {

    @Override
    public void process() {
        System.out.println("methods.Paypal processing");
    }

    @Override
    public void refund() {
        System.out.println("methods.Paypal refund");
    }

    @Override
    public void validate() {
        System.out.println("methods.Paypal validate");
    }
}
