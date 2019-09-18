package Controller;

import java.io.FileInputStream;
import DeckOfCards.Deck;
import PlayArea.PlayArea;
import application.Main;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.AnchorPane;
import javafx.scene.text.Text;

public class PlayAreaController implements EventHandler {
	public static PlayArea play = new PlayArea();
	
	@FXML
	public Text playerScore, enemyScore, player1Score = new Text("0"), player2Score = new Text("0");
	
	@FXML
	public ImageView you1, y2, e1, e2;
	

	@Override
	public void handle(Event e) {
		
		try {
			ImageView iv1 = new ImageView(), iv2 = new ImageView(), iv3 = new ImageView(), iv4 = new ImageView();
			FXMLLoader loader = new FXMLLoader();
			loader.setLocation( Main.class.getResource("../PlayArea.fxml") );
			loader.setController(new PlayAreaController());
			
			// Load the layout from the FXML and add it to the scene
			AnchorPane layout = (AnchorPane) loader.load();				
			Scene scene = new Scene( layout );
			
			if(PlayArea.hasCards(play.player1)) {//Player 1 Deck
	         	you1.setImage(new Image(new FileInputStream(Deck.getCardColor()), 400, 650, false, false));
	         	you1.setFitWidth(200);
	         	you1.setPreserveRatio(true);
	         	you1.setSmooth(true);
	         	you1.setCache(true);
 
			} else { 
				you1.setVisible(false);				
			}
	         
	         if(PlayArea.hasCards(play.player2)) { // Player 2 deck
	         	e1.setImage(new Image(new FileInputStream(Deck.getCardColor()), 400, 650, false, false));
	         	e1.setFitWidth(200);
	         	e1.setPreserveRatio(true);
	         	e1.setSmooth(true);
	         	e1.setCache(true);
	         } else {
	        	 e1.setVisible(false);	
	         }
	         
	         if(PlayArea.hasCards(play.player2)) { // Player 2 deck
	        	 	y2.setImage(play.getPlayer1Card());
		         	y2.setFitWidth(200);
		         	y2.setPreserveRatio(true);
		         	y2.setSmooth(true);
		         	y2.setCache(true);
		     } else {
		    	 y2.setVisible(false);	
		     }
	         
	         if(PlayArea.hasCards(play.player2)) { // Player 2 deck
	        	 e2.setImage(play.getPlayer2Card());
	        	 e2.setFitWidth(200);
	        	 e2.setPreserveRatio(true);
	        	 e2.setSmooth(true);
	        	 e2.setCache(true);
		     } else {
		        e2.setVisible(false);	
		     }
	                 
	         System.out.println(Integer.toString(play.getP1Score()));
	         System.out.println(Integer.toString(play.getP2Score()));
	         
	         player2Score.setText(Integer.toString(play.getP2Score()));
	         player1Score.setText(Integer.toString(play.getP1Score()));
	         
			((AnchorPane) scene.getRoot()).getChildren().addAll(you1, e1, y2, e2);
			
			Main.stage.setResizable(false);
	        Main.stage.setScene(scene);
	        Main.stage.show();
	        
	        play.playGame();
	        
	        ((AnchorPane) scene.getRoot()).getChildren().removeAll(player1Score, player2Score);
	        
	        player1Score.setText(Integer.toString(play.player1.getScore()));
	        player2Score.setText(Integer.toString(play.player2.getScore()));
	        System.out.println(player1Score);
	        System.out.println(player2Score);
	        
		} catch(Exception f) {
			f.printStackTrace();
		}
		
	}




}
