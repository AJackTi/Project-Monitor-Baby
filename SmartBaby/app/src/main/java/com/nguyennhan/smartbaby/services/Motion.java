package com.nguyennhan.smartbaby.services;

public class Motion {
    private int ID;
    private int quantity;
    private String TimeStart;
    private String TimeEnd;

    @Override
    public String toString() {
        return "Motion{" +
                "ID=" + ID +
                ", quantity=" + quantity +
                ", TimeStart='" + TimeStart + '\'' +
                ", TimeEnd='" + TimeEnd + '\'' +
                '}';
    }

    public Motion() {
    }

    public Motion(int ID, int quantity, String timeStart, String timeEnd) {
        this.ID = ID;
        this.quantity = quantity;
        TimeStart = timeStart;
        TimeEnd = timeEnd;
    }

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
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
}
