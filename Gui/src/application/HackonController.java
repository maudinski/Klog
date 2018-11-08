package application;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

import javafx.event.ActionEvent;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class HackonController {

	static int i = 0;
	
	public void initialize() {
	}
	
	
	public void ConfidentData(ActionEvent event) throws IOException
	{
		//
		System.out.println("Confident Data");//read from button to get screen
		
		//this will let us move to a different scene.
		Parent confidentDataView = FXMLLoader.load(getClass().getResource("ConfidentData.fxml"));
		Scene confidentDataScene = new Scene(confidentDataView, 600, 400);
		
		//this line gets the stage information
		//cast as stage, 
		Stage window = (Stage) ((Node)event.getSource()).getScene().getWindow();
		window.setScene(confidentDataScene);
		window.show();
		
		
	
	}
	
	public void RawData (ActionEvent event) throws IOException
	{
		System.out.println("raw data");
		
		
		//this will let us move to a different scene.
		Parent RawDataView = FXMLLoader.load(getClass().getResource("RawData.fxml"));
		Scene RawScene = new Scene(RawDataView, 600, 400);
		
		//this line gets the stage information
		//cast as stage, 
		Stage window = (Stage) ((Node)event.getSource()).getScene().getWindow();
		window.setScene(RawScene);
		window.show();
		
		
		//call python script
		String[] cmdScript = new String[] {"/usr/bin/python3.5", "~/Desktop/Klog/regex.py"};
		Process procScript = Runtime.getRuntime().exec(cmdScript);

		

		 
		
			
	}
	
	
}
