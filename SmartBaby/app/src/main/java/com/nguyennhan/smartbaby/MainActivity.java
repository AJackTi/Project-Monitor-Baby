package com.nguyennhan.smartbaby;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.nguyennhan.smartbaby.services.ApiUtils;
import com.nguyennhan.smartbaby.services.DataClient;
import com.nguyennhan.smartbaby.services.Information;
import com.nguyennhan.smartbaby.services.Success;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";
    DataClient dataClient;

    TextView txtUser, txtPass;
    Button btnLogin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dataClient = ApiUtils.getData();

        addControls();

    }

    private void addControls() {
        txtUser = findViewById(R.id.txtUserName);
        txtPass = findViewById(R.id.txtPassword);
        btnLogin = findViewById(R.id.btnLogin);
    }

    public void XuLyLogin(View view) {
        String user = txtUser.getText().toString();
        String pass = txtPass.getText().toString();
        Call<Success> call = dataClient.getinfo(user,pass);
        call.enqueue(new Callback<Success>() {
            @Override
            public void onResponse(Call<Success> call, Response<Success> response) {
                Log.e(TAG ,"onRespose: "+ response.body());
                Success dl = response.body();
                if(dl.getStatus().equalsIgnoreCase("success")){
                    Intent i = new Intent(MainActivity.this, MenuMainActivity.class);
                    startActivity(i);
                    Toast.makeText(MainActivity.this, getString(R.string.login_success), Toast.LENGTH_SHORT).show();
                    finish();
                }
                else{
                    Toast.makeText(MainActivity.this, getString(R.string.login_fail), Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<Success> call, Throwable t) {
                Log.e(TAG, "onFailure: " + t.getLocalizedMessage() );
            }
        });
    }
}
