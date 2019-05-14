package com.nguyennhan.smartbaby.services;

public class Sound {
    private int ID;
    private int Parameter;
    private String CodeSound;
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

    public String getCodeSound() {
        return CodeSound;
    }

    public void setCodeSound(String codeSound) {
        CodeSound = codeSound;
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

    public Sound() {
    }

    public Sound(int ID, int parameter, String codeSound, String timeStart, String timeEnd) {
        this.ID = ID;
        Parameter = parameter;
        CodeSound = codeSound;
        TimeStart = timeStart;
        TimeEnd = timeEnd;
    }

    @Override
    public String toString() {
        return "Sound{" +
                "ID=" + ID +
                ", Parameter=" + Parameter +
                ", CodeSound='" + CodeSound + '\'' +
                ", TimeStart='" + TimeStart + '\'' +
                ", TimeEnd='" + TimeEnd + '\'' +
                '}';
    }
}
