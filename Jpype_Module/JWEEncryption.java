//package com.JWE;


import java.security.Key;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.xml.bind.DatatypeConverter;

//import org.apache.log4j.BasicConfigurator;
//import org.json.simple.parser.JSONParser;
import org.json.simple.JSONObject;
import org.jose4j.jwa.AlgorithmConstraints;
import org.jose4j.jwe.JsonWebEncryption;
import org.jose4j.jwx.CompactSerializer;
import org.jose4j.keys.AesKey;
import org.jose4j.lang.JoseException;
import org.json.simple.parser.ParseException;
import py4j.*;
public class JWEEncryption {
	/*-----UAT KEY-----------*/
	private static final String PRIVATE_KEY_STRING = "BECEDE9F047E88314D6A9347B90E2BECF2AF3805F5DCE0DC2DA33713884A1D9A";
	/*-----UAT KEY-----------*/
    
    
    public static void encryptRequest(JSONObject jsonObject) throws JoseException {
        Key key = new AesKey(DatatypeConverter.parseHexBinary(PRIVATE_KEY_STRING));
        JsonWebEncryption jwe = new JsonWebEncryption();
        jwe.setPayload(jsonObject.toJSONString());
        jwe.setAlgorithmHeaderValue("A256KW");
       
        jwe.setEncryptionMethodHeaderParameter("A128CBC-HS256");
        jwe.setKey(key);
        String serializedJwe = jwe.getCompactSerialization();
        String[] components = CompactSerializer.deserialize(serializedJwe);

        Map<String, Object> map = new HashMap<String, Object>();
        map.put("protected", components[0]);
        map.put("ciphertext", components[3]);
        map.put("iv", components[2]);
        map.put("tag", components[4]);

        Map<String, String> encryptedKey = new HashMap<String, String>();
        encryptedKey.put("encrypted_key", components[1]);

        map.put("recipients", Arrays.asList(new Map[]{encryptedKey}));
        System.out.println("Encrypted Text: " + JSONObject.toJSONString(map));
    }

    public static void decryptRequest(JSONObject jsonObject) throws JoseException {
        List<?> recipients = (List<?>) jsonObject.get("recipients");
        Map<?, ?> keyMap = (Map<?, ?>) recipients.get(0);
        String serializedJwe = CompactSerializer.serialize(new String[]{(String) jsonObject.get("protected"), (String) keyMap.get("encrypted_key"),
            (String) jsonObject.get("iv"), (String) jsonObject.get("ciphertext"), (String) jsonObject.get("tag")});
        Key key = new AesKey(DatatypeConverter.parseHexBinary(PRIVATE_KEY_STRING));
        JsonWebEncryption jwe = new JsonWebEncryption();
        jwe.setAlgorithmConstraints(
                new AlgorithmConstraints(AlgorithmConstraints.ConstraintType.WHITELIST, new String[]{"A256KW"}));
        jwe.setContentEncryptionAlgorithmConstraints(
                new AlgorithmConstraints(AlgorithmConstraints.ConstraintType.WHITELIST, new String[]{
            "A128CBC-HS256"}));
        jwe.setKey(key);
        jwe.setCompactSerialization(serializedJwe);
        System.out.println( "Decrypted Text: " + jwe.getPayload());
    }
    
    public static void main (String [] args) throws ParseException, JoseException {
       // JSONParser jsonParser = new JSONParser();
        /*String s = "{  \r\n" +
        		"   \"gatewayRequest\":{  \r\n" +
        		"      \"request\":{  \r\n" +
        		"         \"customerID\":\"100631746\",\r\n" +
        		"         \"accountNumber\":\"07925400000499\"\r\n" +
        		"      },\r\n" +
        		"      \"header\":{  \r\n" +
        		"         \"timeStamp\":\"1519731538269\",\r\n" +
        		"         \"sVersion\":\"20\",\r\n" +
        		"         \"serReqId\":\"ESBAccountBalanceEnquiry\",\r\n" +
        		"         \"apiVersion\":\"1.0\",\r\n" +
        		"         \"requestUUID\":\"895547860909\",\r\n" +
        		"         \"languageId\":1,\r\n" +
        		"         \"isEnc\":\"N\",\r\n" +
        		"         \"channelId\":\"XOMIC\",\r\n" +
        		"         \"cifId\":\"100631569\"\r\n" +
        		"      }\r\n" +
        		"   }\r\n" +
        		"}";
        
        String s1 = "{\r\n" + 
        		"    \"recipients\": [\r\n" + 
        		"        {\r\n" + 
        		"            \"encrypted_key\": \"BmtXPoa9kwJL0A16mfpmT6Hulblxz35JHNpScRTo6wnEoVgs7XgplA\"\r\n" + 
        		"        }\r\n" + 
        		"    ],\r\n" + 
        		"    \"protected\": \"eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiQTI1NktXIn0\",\r\n" + 
        		"    \"ciphertext\": \"ytpzTAuvlF9KnToKZ0XjSqbduFCISCAyN6Q1oflmPanCJN9AAzkSkkzuc3i16Hd6grbtsMQ15th44kaNjxJt_GsQvWSCi1y_vjL-GH0X5NY6G-zlhn-OUvvXy82YfS4G4SeDC5u32vdj8OC9xR1BKg\",\r\n" + 
        		"    \"iv\": \"dpYB5Qcr8rsZBJm1nrYRIg\",\r\n" + 
        		"    \"tag\": \"iEo7pVPJQbAVJ5OYZhFaxg\"\r\n" + 
        		"}";
        */
        //JSONObject jsonObject = (JSONObject)jsonParser.parse(s);
        //JSONObject jsonObject1 = (JSONObject)jsonParser.parse(s1);
        //encryptRequest(jsonObject);
        //decryptRequest(jsonObject1);

        JWEEncryption JWEEnc = new JWEEncryption();
        GatewayServer server = new GatewayServer(JWEEnc);
        server.start();
        System.out.println("Working");
   }
}
