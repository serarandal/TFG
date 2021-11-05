package com.example.tfg_01;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;



public class MainActivity extends AppCompatActivity {
    static String extramessage;
    static String extramessage2;
    static String Wifialreadyconnected;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        WifiManager w = (WifiManager) this.getApplicationContext().getSystemService(WIFI_SERVICE);
        WifiInfo wifiInfo = w.getConnectionInfo();
        if(wifiInfo.getMacAddress().equals("02:00:00:00:00:00") )
        {
            Intent intent = new Intent(this, DisplayMessageActivity.class);
            String message = "1";
            intent.putExtra(Wifialreadyconnected,message);
            startActivity(intent);
        }
    }


    public void sendMessage(View view)
    {


        Intent intent = new Intent(this, DisplayMessageActivity.class);
        EditText editText = (EditText) findViewById(R.id.wifiID);
        EditText editText2 = (EditText) findViewById(R.id.password);
        String message = editText.getText().toString();
        String message2 = editText2.getText().toString();
        intent.putExtra(extramessage, message);
        intent.putExtra(extramessage2, message2);
        startActivity(intent);

    }
}