package com.nguyennhan.smartbaby;


import android.app.DatePickerDialog;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Toast;

import com.highsoft.highcharts.core.*;
import com.highsoft.highcharts.common.hichartsclasses.*;
import com.highsoft.highcharts.core.HIChartView;
import com.nguyennhan.smartbaby.services.ApiUtils;
import com.nguyennhan.smartbaby.services.DataClient;
import com.nguyennhan.smartbaby.services.Motion;
import com.nguyennhan.smartbaby.services.Sound;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


/**
 * A simple {@link Fragment} subclass.
 */
public class ChartSoundFragment extends Fragment {

    EditText txtTimeStart, txtTimeEnd;
    Button btnXView;

    HIChartView chartView;
    HIOptions options;
    DataClient dataClient;

    Calendar calendar = Calendar.getInstance();
    SimpleDateFormat sdf1 = new SimpleDateFormat("dd/MM/yyyy");
    public ChartSoundFragment() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        final View view = inflater.inflate(R.layout.fragment_chart_sound, container, false);
        chartView = view.findViewById(R.id.hc);
        dataClient = ApiUtils.getData();
        txtTimeStart = view.findViewById(R.id.txtTimeStart);
        txtTimeEnd = view.findViewById(R.id.txtTimeEnd);
        btnXView = view.findViewById(R.id.btnXem);


        ArrayList<Integer> dlPara = new ArrayList<>();
        ArrayList<String> dlDate = new ArrayList<>();
        Bundle bundle = getArguments();
        if(bundle != null)
        {
            dlPara = bundle.getIntegerArrayList("dlPara");
            dlDate = bundle.getStringArrayList("dlDate");
        }

        addEvents();
        BieuDo(dlPara, dlDate);

        return view;
    }

    private void BieuDo(ArrayList<Integer> dlPara, ArrayList<String> dlDate) {

        options = new HIOptions();

        HITitle title = new HITitle();
        title.setText(getString(R.string.menu_chart_sound));
        options.setTitle(title);

        HISubtitle subtitle = new HISubtitle();
        subtitle.setText(getString(R.string.subtitle));
        options.setSubtitle(subtitle);

        final HIXAxis xAxis = new HIXAxis();
        //String[] categoriesList = new String[] {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" };
        //xAxis.setCategories(new ArrayList<>(Arrays.asList(categoriesList)));
        xAxis.setCategories(new ArrayList<>(dlDate));
        xAxis.setCrosshair(new HICrosshair());
        options.setXAxis(new ArrayList<HIXAxis>(){{add(xAxis);}});

        HIYAxis yaxis = new HIYAxis();
        yaxis.setTitle(new HITitle());
        yaxis.getTitle().setText(getString(R.string.number_of_sound));
        options.setYAxis(new ArrayList<>(Collections.singletonList(yaxis)));

        HILegend legend = new HILegend();
        legend.setLayout("vertical");
        legend.setAlign("right");
        legend.setVerticalAlign("middle");
        options.setLegend(legend);

        HIPlotOptions plotoptions = new HIPlotOptions();
        plotoptions.setSeries(new HISeries());
        plotoptions.getSeries().setLabel(new HILabel());
        plotoptions.getSeries().getLabel().setConnectorAllowed(false);
       // plotoptions.getSeries().setPointStart(2010);
        options.setPlotOptions(plotoptions);



        HILine line1 = new HILine();
        line1.setName(getString(R.string.sound));
        line1.setData(new ArrayList(dlPara));
        //line1.setData(new ArrayList<>(Arrays.asList(12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111)));

        HIResponsive responsive = new HIResponsive();

        HIRules rules1 = new HIRules();
        rules1.setCondition(new HICondition());
        rules1.getCondition().setMaxWidth(500);
        HashMap<String, HashMap> chartLegend = new HashMap<>();
        HashMap<String, String> legendOptions = new HashMap<>();
        legendOptions.put("layout", "horizontal");
        legendOptions.put("align", "center");
        legendOptions.put("verticalAlign", "bottom");
        chartLegend.put("legend", legendOptions);
        rules1.setChartOptions(chartLegend);
        responsive.setRules(new ArrayList<>(Collections.singletonList(rules1)));
        options.setResponsive(responsive);

        options.setSeries(new ArrayList<HISeries>(Arrays.asList(line1)));

        chartView.setOptions(options);
    }

    private void addEvents() {
        txtTimeStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                DatePickerDialog.OnDateSetListener callback = new DatePickerDialog.OnDateSetListener() {
                    @Override
                    public void onDateSet(DatePicker view, int year, int month, int dayOfMonth) {
                        calendar.set(Calendar.YEAR,year);
                        calendar.set(Calendar.MONTH, month);
                        calendar.set(Calendar.DAY_OF_MONTH, dayOfMonth);
                        txtTimeStart.setText(sdf1.format(calendar.getTime()));
                    }
                };
                DatePickerDialog datePickerDialog = new DatePickerDialog(getActivity(),
                        callback,calendar.get(Calendar.YEAR),calendar.get(Calendar.MONTH),calendar.get(Calendar.DAY_OF_MONTH));

                datePickerDialog.show();
            }
        });

        txtTimeEnd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                DatePickerDialog.OnDateSetListener callback = new DatePickerDialog.OnDateSetListener() {
                    @Override
                    public void onDateSet(DatePicker view, int year, int month, int dayOfMonth) {
                        calendar.set(Calendar.YEAR,year);
                        calendar.set(Calendar.MONTH, month);
                        calendar.set(Calendar.DAY_OF_MONTH, dayOfMonth);
                        txtTimeEnd.setText(sdf1.format(calendar.getTime()));
                    }
                };
                DatePickerDialog datePickerDialog = new DatePickerDialog(getActivity(),
                        callback,calendar.get(Calendar.YEAR),calendar.get(Calendar.MONTH),calendar.get(Calendar.DAY_OF_MONTH));

                datePickerDialog.show();
            }
        });

        btnXView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (txtTimeStart.getText().toString().equalsIgnoreCase("Time Start") || txtTimeEnd.getText().toString().equalsIgnoreCase("Time End")) {
                    Toast.makeText(getActivity(), getString(R.string.notify_date_time), Toast.LENGTH_SHORT).show();
                }
                else if(txtTimeStart.getText().length()==10 && txtTimeEnd.getText().length() == 10) {
                    String timeStart = ChuyenDoiNgay(txtTimeStart.getText().toString());
                    String timeEnd = ChuyenDoiNgay(txtTimeEnd.getText().toString());
                    Call<List<Sound>> call = dataClient.getSelectSounds(timeStart, timeEnd);
                    call.enqueue(new Callback<List<Sound>>() {
                        @Override
                        public void onResponse(Call<List<Sound>> call, Response<List<Sound>> response) {
                            List<Sound> ds = response.body();
                            BieuDo1(ds);
                        }

                        @Override
                        public void onFailure(Call<List<Sound>> call, Throwable t) {
                            Log.e("tab1", "onFailure: " + t.getLocalizedMessage());
                            Toast.makeText(getActivity(), "Error: " + t.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
                        }
                    });
                }
            }
        });
    }

    private void BieuDo1(List<Sound> ds) {
        Number[] dl = new Number[ds.size()];
        ArrayList<String> arrDate = new ArrayList<>();
        if(ds!=null) {
            for (int i=0; i<ds.size();i++){
                dl[i] = ds.get(i).getParameter();
                arrDate.add(ds.get(i).getTimeStart());
            }
        }

        final HIXAxis xAxis = new HIXAxis();
        xAxis.setCategories(new ArrayList<>(arrDate));
        xAxis.setCrosshair(new HICrosshair());
        options.setXAxis(new ArrayList<HIXAxis>(){{add(xAxis);}});

        HILine line1 = new HILine();
        line1.setName(getString(R.string.sound));
        line1.setData(new ArrayList(Arrays.asList(dl)));

        options.setSeries(new ArrayList<HISeries>(Arrays.asList(line1)));

        chartView.update(options,true);
    }

    private String ChuyenDoiNgay(String time1) {
        String ngay = time1.substring(0,2);
        String thang = time1.substring(3,5);
        String nam = time1.substring(6,10);
        String tong = nam+"-"+thang+"-"+ngay;
        return tong;
    }



}
