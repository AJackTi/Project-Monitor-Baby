package com.nguyennhan.smartbaby;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.FragmentManager;
import android.util.Log;
import android.view.View;
import android.support.v4.view.GravityCompat;
import android.support.v7.app.ActionBarDrawerToggle;
import android.view.MenuItem;
import android.support.design.widget.NavigationView;
import android.support.v4.widget.DrawerLayout;

import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.widget.Toast;

import com.nguyennhan.smartbaby.services.ApiUtils;
import com.nguyennhan.smartbaby.services.Camera;
import com.nguyennhan.smartbaby.services.DataClient;
import com.nguyennhan.smartbaby.services.Motion;
import com.nguyennhan.smartbaby.services.Sound;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MenuMainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    DataClient dataClient;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        NavigationView navigationView = findViewById(R.id.nav_view);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();
        navigationView.setNavigationItemSelectedListener(this);

        if(savedInstanceState == null)
        {
            dataClient = ApiUtils.getData();
            Call<List<Motion>> call = dataClient.getMotions();
            call.enqueue(new Callback<List<Motion>>() {
                @Override
                public void onResponse(Call<List<Motion>> call, Response<List<Motion>> response) {
                    List<Motion> k = response.body();
                    Log.e("tag1", "Ket qua"+ k);
                    ArrayList<Integer> qty = new ArrayList<>();
                    ArrayList<String> arrDate = new ArrayList<>();
                    String s = "";
                    for (Motion m : k) {
                        qty.add(m.getQuantity());
                        s = m.getTimeStart().substring(0, 19);
                        arrDate.add(s);
                    }

                    ChartMotionFragment fragment = new ChartMotionFragment();
                    Bundle bundle = new Bundle();
                    bundle.putString("nhan", "Nguyen Thanh Nhan");
                    bundle.putIntegerArrayList("dlQty",qty);
                    bundle.putStringArrayList("dlDate",arrDate);
                    fragment.setArguments(bundle);

                    getSupportFragmentManager().beginTransaction().replace(R.id.flMain, fragment).commit();
                    navigationView.setCheckedItem(R.id.nav_motion);
                }

                @Override
                public void onFailure(Call<List<Motion>> call, Throwable t) {
                    Log.e("tab1", "onFailure: " + t.getLocalizedMessage() );
                }
            });
            //getSupportFragmentManager().beginTransaction().replace(R.id.flMain, new ChartMotionFragment()).commit();

        }
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_motion) {
            dataClient = ApiUtils.getData();
            Call<List<Motion>> call = dataClient.getMotions();
            call.enqueue(new Callback<List<Motion>>() {
                @Override
                public void onResponse(Call<List<Motion>> call, Response<List<Motion>> response) {
                    List<Motion> k = response.body();
                    Log.e("tag1", "Ket qua"+ k);
                    ArrayList<Integer> qty = new ArrayList<>();
                    ArrayList<String> arrDate = new ArrayList<>();
                    String s = "";
                    for (Motion m : k) {
                        qty.add(m.getQuantity());
                        s = m.getTimeStart().substring(0, 19);
                        arrDate.add(s);
                    }

                    ChartMotionFragment fragment = new ChartMotionFragment();
                    Bundle bundle = new Bundle();
                    bundle.putString("nhan", "Nguyen Thanh Nhan");
                    bundle.putIntegerArrayList("dlQty",qty);
                    bundle.putStringArrayList("dlDate",arrDate);
                    fragment.setArguments(bundle);

                    getSupportFragmentManager().beginTransaction().replace(R.id.flMain, fragment).commit();
                }

                @Override
                public void onFailure(Call<List<Motion>> call, Throwable t) {
                    Log.e("tab1", "onFailure: " + t.getLocalizedMessage() );
                }
            });

           // getSupportFragmentManager().beginTransaction().replace(R.id.flMain, new ChartMotionFragment()).commit();
        } else if (id == R.id.nav_sound) {
            dataClient = ApiUtils.getData();
            Call<List<Sound>> call = dataClient.getSounds();
            call.enqueue(new Callback<List<Sound>>() {
                @Override
                public void onResponse(Call<List<Sound>> call, Response<List<Sound>> response) {
                    List<Sound> ds = response.body();
                    Log.e("tag1", "Ket qua"+ ds);
                    ArrayList<Integer> para = new ArrayList<>();
                    ArrayList<String> arrDate = new ArrayList<>();
                    String s = "";
                    for (Sound m : ds) {
                        para.add(m.getParameter());
                        s = m.getTimeStart().substring(0, 19);
                        arrDate.add(s);
                    }

                    ChartSoundFragment fragment = new ChartSoundFragment();
                    Bundle bundle = new Bundle();
                    bundle.putIntegerArrayList("dlPara",para);
                    bundle.putStringArrayList("dlDate",arrDate);
                    fragment.setArguments(bundle);
                    getSupportFragmentManager().beginTransaction().replace(R.id.flMain, fragment).commit();
                }

                @Override
                public void onFailure(Call<List<Sound>> call, Throwable t) {
                    Log.e("tab1", "onFailure: " + t.getLocalizedMessage() );
                }
            });

        } else if (id == R.id.nav_camera) {

            dataClient = ApiUtils.getData();
            Call<List<Camera>> call = dataClient.getCameras();
            call.enqueue(new Callback<List<Camera>>() {
                @Override
                public void onResponse(Call<List<Camera>> call, Response<List<Camera>> response) {
                    List<Camera> ds = response.body();
                    Log.e("tag1", "Ket qua"+ ds);
                    ArrayList<Integer> para = new ArrayList<>();
                    ArrayList<String> arrDate = new ArrayList<>();
                    String s = "";
                    for (Camera m : ds) {
                        para.add(m.getParameter());
                        s = m.getTimeStart().substring(0, 19);
                        arrDate.add(s);
                    }

                    ChartCameraFragment fragment = new ChartCameraFragment();
                    Bundle bundle = new Bundle();
                    bundle.putIntegerArrayList("dlPara",para);
                    bundle.putStringArrayList("dlDate",arrDate);
                    fragment.setArguments(bundle);
                    getSupportFragmentManager().beginTransaction().replace(R.id.flMain, fragment).commit();
                }

                @Override
                public void onFailure(Call<List<Camera>> call, Throwable t) {
                    Log.e("tab1", "onFailure: " + t.getLocalizedMessage() );
                }
            });

        } else if (id == R.id.nav_tools) {

        } else if (id == R.id.nav_share) {

        } else if (id == R.id.nav_send) {

        }

        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
