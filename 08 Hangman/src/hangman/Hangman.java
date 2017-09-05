/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hangman;

import java.util.ArrayList;
import java.util.Scanner;
public class Hangman {

    private final char[] password;
    private char[] result;
    static int chance;
    
    public ArrayList<Character> fault;
    
    public Hangman(){
        //password = new char["example".length()];
        password = "example".toUpperCase().toCharArray();
        //result = new char["example".length()];
        result = setRes(password.length);
        chance = 7;
        fault = new ArrayList();
    }
    
    private char[] setRes(int len){
        char[] c = new char[len];
        for(int i = 0 ; i < c.length ; i++)
            c[i] = '*';
        return c;
    }
    /*
    public Hangman(String pw){
        password = new String(pw);
        len = pw.length();
        chance = 11;
    }
    */
    
    public void printResult(){
    System.out.println(result);
    
    }
    
    public void printPassword(){
        System.out.println(password);
    }
    
    public void printFault(){
        System.out.println(fault.toString());
    }
    
    public int getChance(){
        return chance;
    }
    
    public boolean checkCharacter(char c){
        int count = 0;
        for(int i = 0; i < this.password.length ; i++ )
        {
            if( this.password[i] == c)
            {
                count+= 1;
                this.result[i] = c;
            }
            
        }
        return count != 0;
    }
    
    public boolean isSolved(){
        int count = 0;
        for( int i = 0 ; i < this.getLen() ; i++)
            if( password[i] == result[i])
                count++;
        if(count == this.getLen())
            return true;
        else
            return false;
    }
    
    public int getLen(){
        return password.length;
    }
    public static void main(String[] args) {
        Hangman hang = new Hangman();
        Scanner reader = new Scanner(System.in);
        System.out.println("Hello in Hangman Game! Write your letter!");
        
        
        while( hang.chance != 0 && hang.isSolved() != true)
        { 
            char c = reader.nextLine().charAt(0);
            c = Character.toUpperCase(c);
            while( hang.fault.contains(c) == true )
            {
                System.out.println("Write another letter, fault array:\n");
                
                c = reader.nextLine().charAt(0);
                c = Character.toUpperCase(c);
                
            }
            
            if ( hang.checkCharacter(c) == false)
            {
                System.out.println("Wrong letter");
                boolean toAdd = hang.fault.add(c);
                Hangman.chance-=1;
            }
            System.out.print("Your result is: ");
            hang.printResult();
            
            System.out.println("Number of chances: " + hang.getChance());
            System.out.println("Array of faults letter:");
            hang.printFault();

        }
        if(hang.isSolved())
            System.out.println("Good job, you win");
        else
            System.out.println("You lose");
        
        System.out.println("Your type:");
        hang.printResult();        
        System.out.println("Password:");
        hang.printPassword();
        
        
        
    }
    
}
