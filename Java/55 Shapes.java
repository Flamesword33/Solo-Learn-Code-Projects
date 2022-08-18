/** 55 Shapes.java
 * by Nathan Pelletier 
 * worked with Peter Lewis
 * August 18 2022
 *
 You are working on a graphical app, which includes multiple 
 different shapes. The given code declares a base Shape class 
 with an abstract area() method and a width attribute. You 
 need to create two Shape subclasses, Square and Circle, which 
 initialize the width attribute using their constructor, and 
 define their area() methods. 
 */
 
import java.util.Scanner;

abstract class Shape{
    int width;
    abstract void area();
}
//your code here

public class Square extends Shape{
    
        public Square(int length){
                this.width=length;
        }
        @override
	public double area(int width){
		return width*width;
	}//area
}//Square

public class Circle extends Shape{
    
        public Circle(int radius){
                this.width=radius;
        }
        
        @override
	public double area(int radius){
		return (Math.PI*width*width);
	}//area
}//Circle

public class Program{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();
    int y = sc.nextInt();
    
    Square a = new Square(x);
    Circle b = new Circle(y);
    a.area();
    b.area();
  }
}