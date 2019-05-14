package com.nguyennhan.smartbaby.services;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

public interface DataClient {

    //Lay dui lieu thong tin dang nhap
    @GET("informations")
    Call<List<Information>> getinfos();

    @GET("information/{user}/{pass}")
    Call<Success> getinfo(@Path("user") String user, @Path("pass") String pass);

    //Lay du lieu chuyen dong
    @GET("sensormotions")
    Call<List<Motion>> getMotions();

    @GET("sensormotion/{TimeStart}/{TimeEnd}")
    Call<List<Motion>> getSelectMotions(@Path("TimeStart") String tstart, @Path("TimeEnd") String tend);

    //Lay du lieu Am Thanh
    @GET("sensorsounds")
    Call<List<Sound>> getSounds();

    @GET("sensorsound/{TimeStart}/{TimeEnd}")
    Call<List<Sound>> getSelectSounds(@Path("TimeStart") String tstart, @Path("TimeEnd") String tend);

    //Lay du lieu Camera
    @GET("cameras")
    Call<List<Camera>> getCameras();

    @GET("camera/{TimeStart}/{TimeEnd}")
    Call<List<Camera>> getSelectCameras(@Path("TimeStart") String tstart, @Path("TimeEnd") String tend);


}
