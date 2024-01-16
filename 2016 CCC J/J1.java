/*
Name: Nrushanth Suthaharan
Description: 2016 CCC J1
*/
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int month = input.nextInt();
    int day = input.nextInt();

    if(month < 2){
      System.out.print("Before");   
    }
    else if(month>2){
      System.out.print("After");
    }
    else{
      if(day<18){
        System.out.print("Before");
      }
      else if(day>18){
        System.out.print("After");
      }
      else{
        System.out.print("Special");
      }
    }
  }
}