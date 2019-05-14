package com.nguyennhan.smartbaby.services;

public class ApiUtils {
    public static final String Base_url = "https://192.168.193.2:5002/api/";

    // public static final String Base_url = "https://jsonplaceholder.typicode.com/";
    public static DataClient getData(){
        return RetrofitClient.getClient(Base_url).create(DataClient.class);
    }
}
