package net.net63.andrewm_testwebsite.testapplication;

import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.text.Editable;
import android.view.Menu;
import android.view.MenuItem;
// imports made by me
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.firebase.client.DataSnapshot;
import com.firebase.client.Firebase;
import com.firebase.client.FirebaseError;
import com.firebase.client.ValueEventListener;


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

    public void buttonClicked(View v){
        // creates the firebase reference to write data to
        Firebase FB = new Firebase("https://radiant-torch-1512.firebaseio.com/chatapp/");
        Firebase userFB = FB.child("users");

        // gets the widgets that have all the needed inputs
        EditText usernameInput = (EditText)findViewById(R.id.usernameInput);
        EditText passwordInput = (EditText)findViewById(R.id.passwordInput);
        Button button = (Button)findViewById(R.id.buttonToClick);
        TextView outputLabel = (TextView)findViewById(R.id.hiddenText);

        // gets the text from the input fields
        Editable username = usernameInput.getText();
        Editable password = passwordInput.getText();

        // sets the text of the button each time its pressed
        if(button.getText() == "State 1"){
            button.setText("State 2");
        }
        else{
            button.setText("State 1");
        }

        // empties the input fields
        usernameInput.setText("");
        passwordInput.setText("");

        // writes the username and password to the firebase - this can then be used on the website!
        userFB.child(String.valueOf(username)).child("userName").setValue(String.valueOf(username));
        userFB.child(String.valueOf(username)).child("password").setValue(String.valueOf(password));

        // changes the hidden label to show that the user's input was taken
        outputLabel.setText("Username : "+username+"\nPassword : "+password);
    }
}
