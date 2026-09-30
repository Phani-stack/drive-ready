public class BoothActivity {

    private int wallet;

    BoothActivity(int wallet) {
        this.wallet = wallet;
    }


    public void registerStudent() {
        if (!isStudentValid()) {
            System.out.println("Student is not eligible to participate");
        }
        System.out.println("Student registered");
    }


    public boolean isStudentValid() {
        return true;
    }

    public void deduct(int amount) {
        wallet -= amount;
        System.out.println("Amount detected");
    }

    public void assignToken() {
        System.out.println("Token assigned");
    }

    public void storeRecord() {
        System.out.println("Record stored in database");
    }

    public void generatedReceipt() {
        System.out.println("Receipt generated");
    }

    public void sendMail() {
        System.out.println("Email sent to student email");
    }

}
