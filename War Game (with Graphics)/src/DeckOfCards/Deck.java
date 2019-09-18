package DeckOfCards;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Random;
import javafx.scene.image.Image;

public class Deck {

	private static int size = 52;
	
	public static Card deck[] = new Card[size];
	private static String suit[] = { "Clubs", "Diamonds", "Hearts", "Spades" };
	
	private static String name[] = { "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace" };
	
	private static String cardColor = "src/images/blue_back.png";// default : Blue
	
	private static String cardColors[] = { "src/images/blue_back.png", "src/images/gray_back.png", "src/images/green_back.png", "src/images/purple_back.png",
										  "src/images/red_back.png", "src/images/yellow_back.png" };// Blue: 0, Gray : 1, Green 2, Purple: 3, Red : 4, Yellow 5
	
	private static String imgName[] = { "src/images/2C.png", "src/images/2D.png", "src/images/2H.png", "src/images/2S.png",
									    "src/images/3C.png", "src/images/3D.png", "src/images/3H.png", "src/images/3S.png",
									    "src/images/4C.png", "src/images/4D.png", "src/images/4H.png", "src/images/4S.png",
									    "src/images/5C.png", "src/images/5D.png", "src/images/5H.png", "src/images/5S.png",
									    "src/images/6C.png", "src/images/6D.png", "src/images/6H.png", "src/images/6S.png",
									    "src/images/7C.png", "src/images/7D.png", "src/images/7H.png", "src/images/7S.png",
										"src/images/8C.png", "src/images/8D.png", "src/images/8H.png", "src/images/8S.png",
										"src/images/9C.png", "src/images/9D.png", "src/images/9H.png", "src/images/9S.png",
										"src/images/10C.png", "src/images/10D.png", "src/images/10H.png", "src/images/10S.png",
										"src/images/JC.png", "src/images/JD.png", "src/images/JH.png", "src/images/JS.png",
										"src/images/QC.png", "src/images/QD.png", "src/images/QH.png", "src/images/QS.png",
										"src/images/KC.png", "src/images/KD.png", "src/images/KH.png", "src/images/KS.png",
										"src/images/AC.png", "src/images/AD.png", "src/images/AH.png", "src/images/AS.png" };
	
	public static void generateDeck() throws FileNotFoundException {

		for(int type = 0; type < 4; type++) {
			for(int x = 0; x < 13; x++) { 
					deck[(x + (type * 13))] = new Card(name[x], suit[type], x+2, new Image(new FileInputStream(imgName[(x + (type * 13))]), 300, 650, false, false));
			}
		}
		printDeck();
			
	}
	
	
	public static void shuffleDeck(Card deck[]) {
		for(int count = 0; count < 1000; count++) {
			int r1 = new Random().nextInt(size);
			int r2 = new Random().nextInt(size);
			while (r2 == r1) {
				r2 = new Random().nextInt(size);
			}
			Card a = deck[r1];
			Card b = deck[r2];
			deck[r1] = b;
			deck[r2] = a;
		}
		
	}
	
	public static void printDeck() {
		for(int x = 0; x < deck.length; x++) {
		}
	}


	public static int getSize() {
		return size;
	}


	public static String getCardColor() {
		return cardColor;
	}
	


	public void setCardColor(String cardColor) {
		this.cardColor = cardColor;
	}
}
