/*An approach using multiples instead of the modulus operator.*/
public class FizzBuzz{
    public static void main(String[] args){
        Object[] list = new Object[101];
        for (Integer i = 0; i < 101; i++){
            list[i] = i;
        }
        for (Integer i = 3; i < 101; i += 3){
            list[i] = "Fizz";
        }
        for (Integer i = 5; i < 101; i += 5){
            list[i] = (list[i] instanceof String) ? "FizzBuzz" : "Buzz";
        }
        for (Object e : list) {
            System.out.println(e);
        }
    }
}