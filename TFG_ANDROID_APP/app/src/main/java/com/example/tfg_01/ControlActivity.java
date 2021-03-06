package com.example.tfg_01;

import androidx.appcompat.app.AppCompatActivity;


import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.webkit.WebView;


import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.jackandphantom.joystickview.JoyStickView;


import java.util.HashMap;
import java.util.Map;

import static android.os.SystemClock.sleep;


public class ControlActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_control);
        WebView myWebView = (WebView) findViewById(R.id.webView2);
        myWebView.getSettings().setLoadWithOverviewMode(true);
        myWebView.getSettings().setUseWideViewPort(true);
        myWebView.getSettings().setBuiltInZoomControls(true);
        myWebView.getSettings().setDisplayZoomControls(true);
        String newAgent = "Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0";
        myWebView.getSettings().setUserAgentString(newAgent);
        myWebView.loadUrl("http://192.168.1.184:81/stream");
        startSendingData();

    }


    public void startSendingData()
    {

        JoyStickView joyStick = (JoyStickView) findViewById(R.id.joystick);
        joyStick.setOnMoveListener(new JoyStickView.OnMoveListener() {

            @Override
            public void onMove(double angle, float strength) {

                connectionURL(angle,strength);
                sleep(100);

            }

        });


    }

    public void connectionURL(double angle,float strength)
    {

            String url = "http://192.168.1.110:70/data/";
            String strStrength = String.valueOf(Math.round(strength));
            String str = angle +"/"+strStrength;
            RequestQueue queue = Volley.newRequestQueue(this);
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>()
                    {
                        @Override
                        public void onResponse(String response) {
                            // response
                            Log.d("Response", response);
                        }
                    },
                    new Response.ErrorListener()
                    {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            // error
                            Log.d("Error.Response", error.toString());
                        }
                    }
            ) {
                @Override
                protected Map<String, String> getParams()
                {
                    Map<String, String>  params = new HashMap<String, String>();
                    params.put(String.valueOf(angle),strStrength);


                    return params;
                }
            };
            queue.add(postRequest);

    }

    public void connectStop(View view)
    {
        connectionURL(0,0);
    }





}