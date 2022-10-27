/** 9 Time Converter.java
 * by Nathan Pelletier 
 * October 26, 2022
 *
 * You need a program to convert days to seconds.
 * The given code takes the amount of days as input.
 * Complete the code to convert it to seconds and output the result.
 * 
 * Sample Input:
 * 12
 * 
 * Sample Output:
 * 1036800
 */
 

public class TimeConverter{
  public static void main(String[] args){
        int seconds = days_to_seconds(8);
        System.out.print(seconds);
  }//main

  public static int days_to_seconds(int days){
        int hours = 0;
        int minutes = 0;
        int seconds = 0;

        hours = days * 24;
        minutes = hours * 60;
        seconds = minutes * 60;

        return seconds;
  }//days_to_seconds
}//Time_Converter

