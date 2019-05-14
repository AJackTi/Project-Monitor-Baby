package com.nguyennhan.smartbaby.services;

public class Camera {
    private int ID;
    private int Parameter;
    private String CodeCamera;
    private String VideoLink;
    private String TimeStart;
    private String TimeEnd;

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public int getParameter() {
        return Parameter;
    }

    public void setParameter(int parameter) {
        Parameter = parameter;
    }

    public String getCodeCamera() {
        return CodeCamera;
    }

    public void setCodeCamera(String codeCamera) {
        CodeCamera = codeCamera;
    }

    public String getVideoLink() {
        return VideoLink;
    }

    public void setVideoLink(String videoLink) {
        VideoLink = videoLink;
    }

    public String getTimeStart() {
        return TimeStart;
    }

    public void setTimeStart(String timeStart) {
        TimeStart = timeStart;
    }

    public String getTimeEnd() {
        return TimeEnd;
    }

    public void setTimeEnd(String timeEnd) {
        TimeEnd = timeEnd;
    }

    public Camera() {
    }

    public Camera(int ID, int parameter, String codeCamera, String videoLink, String timeStart, String timeEnd) {
        this.ID = ID;
        Parameter = parameter;
        CodeCamera = codeCamera;
        VideoLink = videoLink;
        TimeStart = timeStart;
        TimeEnd = timeEnd;
    }

    @Override
    public String toString() {
        return "Camera{" +
                "ID=" + ID +
                ", Parameter=" + Parameter +
                ", CodeCamera='" + CodeCamera + '\'' +
                ", VideoLink='" + VideoLink + '\'' +
                ", TimeStart='" + TimeStart + '\'' +
                ", TimeEnd='" + TimeEnd + '\'' +
                '}';
    }
}
