package com.company;
public class Main {

    public static void main(String[] args) throws Exception{

        String password = "programmingchallenges";
        String passwordEnc = AESencrp.encrypt(password);
        String passwordDec = AESencrp.decrypt(passwordEnc);

        System.out.println("Text to encrypt : " + password);
        System.out.println("Encrypted Text : " + passwordEnc);
        System.out.println("Decrypted Text : " + passwordDec);
    }
}
