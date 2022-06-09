package com.example.tfg_01;



import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.net.wifi.WifiManager;
import android.net.wifi.WifiNetworkSuggestion.Builder;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.net.wifi.WifiNetworkSuggestion;


import java.util.ArrayList;
import java.util.List;


public class DisplayMessageActivity extends AppCompatActivity {

    @RequiresApi(api = Build.VERSION_CODES.Q)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);



        Intent intent = getIntent();
        String message = intent.getStringExtra(MainActivity.extramessage);
        String message2 = intent.getStringExtra(MainActivity.extramessage2);
        String message3 = intent.getStringExtra(MainActivity.Wifialreadyconnected);
        TextView textView = findViewById(R.id.textView);

        if(message3.equals("1"))
        {
            Button viewWeb =  findViewById(R.id.viewWeb);
            viewWeb.setVisibility(View.VISIBLE);
            textView.setText("Connected");
        }else
            {
                connectWifi(message,message2);
                if (textView.getText() == "Connected")
                {
                    Button viewWeb =  findViewById(R.id.viewWeb);
                    viewWeb.setVisibility(View.VISIBLE);
                }
            }

    }

    public void connectWeb(View view)
    {
        Intent intent2 = new Intent(this, WebPageActivity.class);
        startActivity(intent2);
    }



    @RequiresApi(api = Build.VERSION_CODES.Q)
    void connectWifi(String message, String message2)
    {
        final WifiNetworkSuggestion suggestion = new Builder().setSsid(message).setWpa2Passphrase(message2).build();

        final List<WifiNetworkSuggestion> suggestionList = new ArrayList<WifiNetworkSuggestion>();
        suggestionList.add(suggestion);

        Context context = getApplicationContext();
        final WifiManager wifimanager = (WifiManager) context.getSystemService(Context.WIFI_SERVICE);
        final int status = wifimanager.addNetworkSuggestions(suggestionList);
        if(status != WifiManager.STATUS_NETWORK_SUGGESTIONS_SUCCESS)
        {
            TextView textView = findViewById(R.id.textView);
            textView.setText("Error Connecting to wifi");
        } else { TextView textView = findViewById(R.id.textView);
            textView.setText("Connected"); }

    }

    public void connectControl(View view)
    {
        Intent intent3 = new Intent(this,ControlActivity.class);
        startActivity(intent3);
    }


}