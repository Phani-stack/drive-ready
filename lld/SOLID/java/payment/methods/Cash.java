package methods;

import interfaces.Processable;
import interfaces.Validatable;

public class Cash implements Processable, Validatable {

    @Override
    public void process() {
        System.out.println("methods.Cash processing");
    }

    @Override
    public void validate() {
        System.out.println("methods.Cash Validating");
    }
}
