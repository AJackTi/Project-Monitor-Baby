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
import com.nguyennhan.smartbaby.services.ApiUtils;
import com.nguyennhan.smartbaby.services.DataClient;
import com.nguyennhan.smartbaby.services.Motion;


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
public class ChartMotionFragment extends Fragment {

    EditText txtTimeStart, txtTimeEnd;
    Button btnXView;

    HIChartView chartView;
    HIOptions options;
    DataClient dataClient;

    Calendar calendar = Calendar.getInstance();
    SimpleDateFormat sdf1 = new SimpleDateFormat("dd/MM/yyyy");
    SimpleDateFormat sdf2 = new SimpleDateFormat("HH:mm");

    ArrayList<Integer>  dlQty = new ArrayList<>();
    ArrayList<String> dlDate = new ArrayList<>();
    public ChartMotionFragment() {
        // Required empty public constructor
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        final View view = inflater.inflate(R.layout.fragment_chart_motion, container, false);
        chartView = view.findViewById(R.id.hc);
        dataClient = ApiUtils.getData();
        txtTimeStart = view.findViewById(R.id.txtTimeStart);
        txtTimeEnd = view.findViewById(R.id.txtTimeEnd);
        btnXView = view.findViewById(R.id.btnXem);

        addEvents();

        String nhan = "";

        Bundle bundle = getArguments();
        if(bundle != null)
        {
            dlQty = bundle.getIntegerArrayList("dlQty");
            dlDate = bundle.getStringArrayList("dlDate");
        }

        BieuDo(dlQty,dlDate);
        return view;
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
                    return;
                }
                else if(txtTimeStart.getText().length()==10 && txtTimeEnd.getText().length() == 10) {
                    String timeStart = ChuyenDoiNgay(txtTimeStart.getText().toString());
                    String timeEnd = ChuyenDoiNgay(txtTimeEnd.getText().toString());
                    int so = timeStart.length();
                    Call<List<Motion>> call = dataClient.getSelectMotions(timeStart, timeEnd);
                    call.enqueue(new Callback<List<Motion>>() {
                        @Override
                        public void onResponse(Call<List<Motion>> call, Response<List<Motion>> response) {
                            List<Motion> ds = response.body();
                            BieuDo1(ds);
                        }

                        @Override
                        public void onFailure(Call<List<Motion>> call, Throwable t) {
                            Log.e("tab1", "onFailure: " + t.getLocalizedMessage());
                            Toast.makeText(getActivity(), "Error: " + t.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
                        }
                    });
                }
            }
        });
    }

    private String ChuyenDoiNgay(String time1) {
        String ngay = time1.substring(0,2);
        String thang = time1.substring(3,5);
        String nam = time1.substring(6,10);
        String tong = nam+"-"+thang+"-"+ngay;
        return tong;
    }

    private void BieuDo(ArrayList<Integer> iseries,ArrayList<String> stitle) {

        chartView.clearAnimation();
        options = new HIOptions();

        HIChart chart = new HIChart();
        chart.setType("column");
        options.setChart(chart);

        HITitle title = new HITitle();
        title.setText(getString(R.string.chart_motion));
        options.setTitle(title);

        HISubtitle subtitle = new HISubtitle();
        subtitle.setText(getString(R.string.subtitle));
        options.setSubtitle(subtitle);

        final HIXAxis xAxis = new HIXAxis();
        //String[] categoriesList = new String[] {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" };
        //xAxis.setCategories(new ArrayList<>(Arrays.asList(categoriesList)));
        xAxis.setCategories(new ArrayList<>(stitle));
        xAxis.setCrosshair(new HICrosshair());
        options.setXAxis(new ArrayList<HIXAxis>(){{add(xAxis);}});

        final HIYAxis yAxis = new HIYAxis();
        yAxis.setMin(0);
        yAxis.setTitle(new HITitle());
        yAxis.getTitle().setText(getString(R.string.number_of_motion));
        options.setYAxis(new ArrayList<HIYAxis>(){{add(yAxis);}});

        HITooltip tooltip = new HITooltip();
        tooltip.setHeaderFormat("<span style=\"font-size:10px\">{point.key}</span><table>");
        tooltip.setPointFormat("<tr><td style=\"color:{series.color};padding:0\">{series.name}: </td><td style=\"padding:0\"><b>{point.y:.1f} lan</b></td></tr>");
        tooltip.setFooterFormat("</table>");
        tooltip.setShared(true);
        tooltip.setUseHTML(true);
        options.setTooltip(tooltip);

        HIPlotOptions plotOptions = new HIPlotOptions();
        plotOptions.setColumn(new HIColumn());
        plotOptions.getColumn().setPointPadding(0.2);
        plotOptions.getColumn().setBorderWidth(0);
        options.setPlotOptions(plotOptions);

        HIColumn series1 = new HIColumn();
        series1.setName(getString(R.string.motion));

        series1.setData(new ArrayList<> (iseries));

        options.setSeries(new ArrayList<HISeries>(Arrays.asList(series1)));

        chartView.setOptions(options);

    }

    private void BieuDo1(List<Motion> a) {

        Number[] dl = new Number[a.size()];
        ArrayList<String> arrDate = new ArrayList<>();
        if(a!=null) {
            for (int i=0; i<a.size();i++){
                dl[i] = a.get(i).getQuantity();
                arrDate.add(a.get(i).getTimeStart());
            }
        }

        final HIXAxis xAxis = new HIXAxis();
        xAxis.setCategories(new ArrayList<>(arrDate));
        xAxis.setCrosshair(new HICrosshair());
        options.setXAxis(new ArrayList<HIXAxis>(){{add(xAxis);}});

        HIColumn series2 = new HIColumn();
        series2.setName(getString(R.string.motion));
        Number[] series2_data;

     //   series2_data = new Number[] {49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4};

        series2.setData(new ArrayList<> (Arrays.asList(dl)));
        options.setSeries(new ArrayList<HISeries>(Arrays.asList(series2)));
        chartView.update(options,true);

    }
}
