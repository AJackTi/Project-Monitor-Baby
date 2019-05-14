package com.nguyennhan.smartbaby.services;

public class Information {
    private int ID;
    private String Username;
    private String Password;
    private String CodeInfo;

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public String getUsername() {
        return Username;
    }

    public void setUsername(String username) {
        Username = username;
    }

    public String getPassword() {
        return Password;
    }

    public void setPassword(String password) {
        Password = password;
    }

    public String getCodeInfo() {
        return CodeInfo;
    }

    public void setCodeInfo(String codeInfo) {
        CodeInfo = codeInfo;
    }

    public Information(int ID, String username, String password, String codeInfo) {
        this.ID = ID;
        Username = username;
        Password = password;
        CodeInfo = codeInfo;
    }

    public Information() {
    }

    @Override
    public String toString() {
        return "Information{" +
                "ID=" + ID +
                ", Username='" + Username + '\'' +
                ", Password='" + Password + '\'' +
                ", CodeInfo='" + CodeInfo + '\'' +
                '}';
    }
}
