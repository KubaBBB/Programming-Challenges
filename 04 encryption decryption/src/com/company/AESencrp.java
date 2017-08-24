package com.company;
/**
 * Created by Jakub on 2017-08-22.
 */
import java.security.*;
import java.security.spec.InvalidKeySpecException;
import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;
import sun.misc.*;

public class AESencrp {
    private static final String Alg = "AES";
    private static final byte[] keyValue = new byte[]{'T', 'h', 'e', 'B', 'e', 's', 't',
            'S', 'e', 'c', 'r','e', 't', 'K', 'e', 'y'};

    public static Key generateKey() throws Exception{
        Key key = new SecretKeySpec(keyValue,Alg);
        return key;
    }

    public static String encrypt(String Data) throws Exception{
        Key key = generateKey();
        Cipher cipher = Cipher.getInstance(Alg);
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encVal = cipher.doFinal(Data.getBytes());
        String encryptedValue = new BASE64Encoder().encode(encVal);
        return encryptedValue;
    }

    public static String decrypt(String encryptedData) throws Exception{
        Key key = generateKey();
        Cipher cipher = Cipher.getInstance(Alg);
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decordedValue = new BASE64Decoder().decodeBuffer(encryptedData);
        byte[] decVal = cipher.doFinal(decordedValue);
        String decryptedValue = new String(decVal);
        return decryptedValue;
    }

}
