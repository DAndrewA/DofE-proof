package net.net63.andrewm_testwebsite.achatsender;

import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;

import com.firebase.client.Firebase;

import java.util.HashMap;
import java.util.Map;


public class MainActivity extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Firebase.setAndroidContext(this);
        setContentView(R.layout.activity_main);
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

    public void sendIt(View v){
        EditText usernameInput = (EditText)findViewById(R.id.messageInput);
        EditText messageInput = (EditText)findViewById(R.id.usernameInput);

        String username = String.valueOf(usernameInput.getText());
        String message = String.valueOf(messageInput.getText());

        Firebase messageFB = new Firebase("https://radiant-torch-1512.firebaseio.com/chatapp/msgs");
        Map<String, String> msgToSend = new HashMap<String, String>();
        msgToSend.put("author",message);
        msgToSend.put("message",username);

        messageFB.push().setValue(msgToSend);

        usernameInput.setText("");
        messageInput.setText("");
    }
}
