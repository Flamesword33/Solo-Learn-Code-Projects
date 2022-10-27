/** 19 Loan Calculator.java
 * by Nathan Pelletier 
 * October 26, 2022
 *
 * You take a loan from a friend and need to calculate how much you will owe him after 3
 * months. You are going to pay him back 10% of the remaining loan amount each month.
 * 
 * Create a program that takes the loan amount as input, calculates and outputs the
 * remaining amount after 3 months.
 * 
 * Sample Input:
 * 20 000
 * 
 * Sample Output:
 * 14 580
 * 
 * Here is the monthly payment schedule:
 * Month 1
 * Payment: 10% of 20 000 = 2000
 * Remaining amount: 18 000
 * Month 2
 * Payment: 1800
 * Remaining amount: 16200
 * Month 3
 * payment: 1620
 * remaining amount: 14580 
 */
 

public class LoanCalculator{
  public static void main(String[] args){
      double starting_amount = 20000;
      double current_amount = starting_amount;

      for(int i = 0; i < 3; i++){
            current_amount = pay_bills(current_amount);
      }

      System.out.print(current_amount);
  }//main
}//LoanCalculator

