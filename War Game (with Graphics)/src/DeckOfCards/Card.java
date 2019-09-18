package DeckOfCards;

import javafx.scene.image.Image;

public class Card {

	private String name;
	private String suit;
	private int number;
	private Image image;
	
	public Card(String name, String suit, int number, Image img ) {
		this.name = name;
		this.suit = suit;
		this.number = number;
		image = img;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getsuit() {
		return suit;
	}

	public void setsuit(String suit) {
		this.suit = suit;
	}

	public int getNumber() {
		return number;
	}

	public void setNumber(int number) {
		this.number = number;
	}
	
	
	public String toString() {
		return name + " of " + suit + " : " + number;
	}

	public Image getImage() {
		return image;
	}
	
}