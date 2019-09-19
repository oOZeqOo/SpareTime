package application;
	
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import Controller.MainController;



public class Main extends Application {
	
	public static Stage stage;
	
	@Override
	public void start(Stage primaryStage) {
		
		stage = primaryStage;
		
		try {

			FXMLLoader loader = new FXMLLoader();
			loader.setLocation( Main.class.getResource("../Main.fxml") );
			loader.setController(new MainController());
			
			AnchorPane layout = (AnchorPane) loader.load();				
			Scene scene = new Scene( layout );
			
			primaryStage.setResizable(false);
			primaryStage.setScene(scene);
			primaryStage.show();
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
