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

import com.highsoft.highcharts.common.hichartsclasses.HIArea;
import com.highsoft.highcharts.common.hichartsclasses.HIChart;
import com.highsoft.highcharts.common.hichartsclasses.HIHover;
import com.highsoft.highcharts.common.hichartsclasses.HILabels;
import com.highsoft.highcharts.common.hichartsclasses.HIMarker;
import com.highsoft.highcharts.common.hichartsclasses.HIOptions;
import com.highsoft.highcharts.common.hichartsclasses.HIPlotOptions;
import com.highsoft.highcharts.common.hichartsclasses.HISeries;
import com.highsoft.highcharts.common.hichartsclasses.HIStates;
import com.highsoft.highcharts.common.hichartsclasses.HISubtitle;
import com.highsoft.highcharts.common.hichartsclasses.HITitle;
import com.highsoft.highcharts.common.hichartsclasses.HITooltip;
import com.highsoft.highcharts.common.hichartsclasses.HIXAxis;
import com.highsoft.highcharts.common.hichartsclasses.HIYAxis;
import com.highsoft.highcharts.core.HIChartContext;
import com.highsoft.highcharts.core.HIChartView;
import com.highsoft.highcharts.core.HIFunction;
import com.highsoft.highcharts.core.HIFunctionInterface;
import com.nguyennhan.smartbaby.services.ApiUtils;
import com.nguyennhan.smartbaby.services.Camera;
import com.nguyennhan.smartbaby.services.DataClient;
import com.nguyennhan.smartbaby.services.Sound;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


/**
 * A simple {@link Fragment} subclass.
 */
public class ChartCameraFragment extends Fragment {
    EditText txtTimeStart, txtTimeEnd;
    Button btnXView;

    HIChartView chartView;
    HIOptions options;
    DataClient dataClient;

    Calendar calendar = Calendar.getInstance();
    SimpleDateFormat sdf1 = new SimpleDateFormat("dd/MM/yyyy");

    public ChartCameraFragment() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        final View view = inflater.inflate(R.layout.fragment_chart_camera, container, false);
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

        HIChart chart = new HIChart();
        chart.setType("area");
        options.setChart(chart);

        HITitle title = new HITitle();
        title.setText(getString(R.string.menu_chart_camera));
        options.setTitle(title);

        HISubtitle subtitle = new HISubtitle();
        subtitle.setText(getString(R.string.subtitle));
        options.setSubtitle(subtitle);

        final HIXAxis xAxis = new HIXAxis();
        xAxis.setAllowDecimals(false);
        xAxis.setLabels(new HILabels());
        xAxis.setCategories(new ArrayList<>(dlDate));
        xAxis.getLabels().setFormatter(new HIFunction(
                new HIFunctionInterface<HIChartContext, String>() {
                    @Override
                    public String apply(HIChartContext f) {
                        return String.valueOf(f.getProperty("value"));
                    }
                },
                new String[] {"value"} )); /*clean, unformatted number for year*/
        options.setXAxis(new ArrayList<HIXAxis>(){{add(xAxis);}});

        final HIYAxis yAxis = new HIYAxis();
        yAxis.setTitle(new HITitle());
        yAxis.getTitle().setText(getString(R.string.number_of_motion_camera));
        yAxis.setLabels(new HILabels());
        yAxis.getLabels().setFormatter(new HIFunction(
                new HIFunctionInterface<HIChartContext, String>() {
                    @Override
                    public String apply(HIChartContext f) {
                        return String.valueOf((Double) f.getProperty("value") / 1000);
                    }
                }, new String[] {"value"} ));
        options.setYAxis(new ArrayList<HIYAxis>(){{add(yAxis);}});

        HITooltip tooltip = new HITooltip();
        tooltip.setPointFormat("{series.name} <b>{point.y:,.0f}</b>");
        options.setTooltip(tooltip);

        HIPlotOptions plotOptions = new HIPlotOptions();
        plotOptions.setArea(new HIArea());
        //plotOptions.getArea().setPointStart(1940);
        plotOptions.getArea().setMarker(new HIMarker());
        plotOptions.getArea().getMarker().setEnabled(false);
        plotOptions.getArea().getMarker().setSymbol("circle");
        plotOptions.getArea().getMarker().setRadius(2);
        plotOptions.getArea().getMarker().setStates(new HIStates());
        plotOptions.getArea().getMarker().getStates().setHover(new HIHover());
        plotOptions.getArea().getMarker().getStates().getHover().setEnabled(true);
        options.setPlotOptions(plotOptions);

        HIArea series1 = new HIArea();
        series1.setName(getString(R.string.motion));
        //Number[] series1_data = new Number[] {6, 11, 32, 110, 235, 369, 640, 1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468, 20434, 24126, 27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342, 26662, 26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605, 24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586, 22380, 21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950, 10871, 10824, 10577, 10527, 10475, 10421, 10358, 10295, 10104};
        series1.setData(new ArrayList<>(dlPara));
        options.setSeries(new ArrayList<HISeries>(Arrays.asList(series1)));

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
                    Call<List<Camera>> call = dataClient.getSelectCameras(timeStart, timeEnd);
                    call.enqueue(new Callback<List<Camera>>() {
                        @Override
                        public void onResponse(Call<List<Camera>> call, Response<List<Camera>> response) {
                            List<Camera> ds = response.body();
                            BieuDo1(ds);
                        }

                        @Override
                        public void onFailure(Call<List<Camera>> call, Throwable t) {
                            Log.e("tab1", "onFailure: " + t.getLocalizedMessage());
                            Toast.makeText(getActivity(), "Error: " + t.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
                        }
                    });
                }
            }
        });
    }

    private void BieuDo1(List<Camera> ds) {
        Number[] dl = new Number[ds.size()];
        ArrayList<String> arrDate = new ArrayList<>();
        if(ds!=null) {
            for (int i=0; i<ds.size();i++){
                dl[i] = ds.get(i).getParameter();
                arrDate.add(ds.get(i).getTimeStart());
            }
        }

        final HIXAxis xAxis = new HIXAxis();
        xAxis.setAllowDecimals(false);
        xAxis.setLabels(new HILabels());
        xAxis.setCategories(new ArrayList<>(arrDate));
        xAxis.getLabels().setFormatter(new HIFunction(
                new HIFunctionInterface<HIChartContext, String>() {
                    @Override
                    public String apply(HIChartContext f) {
                        return String.valueOf(f.getProperty("value"));
                    }
                },
                new String[] {"value"} )); /*clean, unformatted number for year*/
        options.setXAxis(new ArrayList<HIXAxis>(){{add(xAxis);}});


        HIArea series1 = new HIArea();
        series1.setName(getString(R.string.motion));
        //Number[] series1_data = new Number[] {6, 11, 32, 110, 235, 369, 640, 1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468, 20434, 24126, 27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342, 26662, 26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605, 24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586, 22380, 21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950, 10871, 10824, 10577, 10527, 10475, 10421, 10358, 10295, 10104};
        series1.setData(new ArrayList<>(Arrays.asList(dl)));
        options.setSeries(new ArrayList<HISeries>(Arrays.asList(series1)));

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
