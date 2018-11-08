package application;

import java.util.*;
import java.io.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import javafx.scene.control.Button;


import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.TextArea;
import javafx.stage.Stage;

public class RawDataController {

	
	@FXML
	private TextArea rawtexthere;
	@FXML
	private Button backToMain;
	
	public void initialize() throws IOException {
		
		//read entire raw data file 
		 String text = new String(Files.readAllBytes(Paths.get("/home/mauricio/Desktop/Klog/raw.txt")), StandardCharsets.UTF_8);
		 //pass this string text to the label within java fx
		 
		rawtexthere.setText(text);	
		
	}
	
	
	public void backToMainR (ActionEvent event) throws IOException
	{
		System.out.println("going back to main page");
		//this will let us move to a different scene.
		Parent backtomainView = FXMLLoader.load(getClass().getResource("hackon.fxml"));
		Scene mainScene = new Scene(backtomainView);
		
		//this line gets the stage information
		//cast as stage, 
		Stage window = (Stage) ((Node)event.getSource()).getScene().getWindow();
		window.setScene(mainScene);
		window.show();


	}
}
	
	

