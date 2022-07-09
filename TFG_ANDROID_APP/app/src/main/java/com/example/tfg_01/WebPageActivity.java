package com.example.tfg_01;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.webkit.WebView;

public class WebPageActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_web_page);
        WebView myWebView = (WebView) findViewById(R.id.webview);
        String newAgent = "Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0";
        myWebView.getSettings().setUserAgentString(newAgent);
        myWebView.loadUrl("http://192.168.1.184:80");

    }
}