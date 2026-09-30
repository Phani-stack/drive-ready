public class Main {
    public static void main(String[] args) {
        Student student1 = new Student.Builder().name("Phani").age(20).build();

        Student student2 = new Student(student1);

        System.out.println(student1);

        System.out.println(student2);

        student1.setName("Surya");

        System.out.println(student1);

        System.out.println(student2);
    }
}
