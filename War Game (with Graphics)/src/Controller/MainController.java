package Controller;

import java.io.FileInputStream;

import DeckOfCards.Deck;
import application.Main;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;

import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.AnchorPane;

import javafx.scene.text.Text;

public class MainController implements EventHandler{
	;
	
	@FXML
	public static Text playerScore = new Text("0"), enemyScore = new Text("0");
	
	public MainController() {
		
	}
	
	@Override
	public void handle(Event e) {
		try {
			FXMLLoader loader = new FXMLLoader();
			loader.setLocation( Main.class.getResource("../PlayArea.fxml") );
			loader.setController(new PlayAreaController());
		
			// Load the layout from the FXML and add it to the scene
			AnchorPane layout = (AnchorPane) loader.load();				
			Scene scene = new Scene( layout );
			
			
			ImageView iv1 = new ImageView();
	         iv1.setImage(new Image(new FileInputStream(Deck.getCardColor()), 400, 650, false, false));
	         iv1.setFitWidth(200);
	         iv1.setPreserveRatio(true);
	         iv1.setSmooth(true);
	         iv1.setCache(true);
	         iv1.setTranslateX(100);
	         iv1.setTranslateY(300);
	         // resizes the image to have width of 100 while preserving the ratio and using
	         // higher quality filtering method; this ImageView is also cached to
	         // improve performance
	         ImageView iv2 = new ImageView();
	         iv2.setImage(new Image(new FileInputStream(Deck.getCardColor()), 400, 650, false, false));
	         iv2.setFitWidth(200);
	         iv2.setPreserveRatio(true);
	         iv2.setSmooth(true);
	         iv2.setCache(true);
	         iv2.setTranslateX(900);
	         iv2.setTranslateY(300);
			 
			
			((AnchorPane) scene.getRoot()).getChildren().addAll(iv1, iv2, playerScore, enemyScore);
			
			Main.stage.setResizable(false);
	        Main.stage.setScene(scene);
	        Main.stage.show();
	        
	        PlayAreaController.play.initiatePlayArea();
	        
	        
		} catch(Exception f) {
			f.printStackTrace();
		}		
	}
	
	public static void updateScene(){
		
	}
	
}
