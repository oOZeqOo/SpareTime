package PlayArea;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class VisualField {
	
	public static Stage playArea;
	
	public static void playGame() {
		playArea.setTitle("War Game!");
        Button btn = new Button();
        btn.setPrefWidth(400);
        btn.setPrefHeight(200);
        btn.setFont(new Font(75));
        btn.setText("Stop");
        //btn.toFront();
        btn.setOnAction(new EventHandler<ActionEvent>() { //Figure out how to get rid of the button and play the game
 
            @Override
            public void handle(ActionEvent event) {
                System.out.println("Starting!");
               
            }
        });
        
        StackPane root = new StackPane();
        root.setStyle("-fx-background-color: #FF0000");
        root.getChildren().add(btn);
        playArea.setScene(new Scene(root, 800, 600));
        playArea.show();
	}
}
