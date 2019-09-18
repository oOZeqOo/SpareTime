package Player;

import java.util.ArrayList;

import DeckOfCards.Card;

public class Player {

	public String name;
	public ArrayList<Card> hand = new ArrayList<Card>();
	public ArrayList<Card> winPile = new ArrayList<Card>();// = 0
	public int score = 0;
	
	public Player(String name) {
		this.name = name;
	}
	
	public void addCard(ArrayList<Card> c, Card card) {
		c.add(card);
	}
	
	public Card playCard() {
		if(hand.size() <= 0) {
			return null; 
		}
		Card c = hand.get(0);
		System.out.println(name + " playing " + c);
		removeCard(hand);
		return c;
	}
	
	public void removeCard(ArrayList<Card> c) {
		c.remove(0);
	}
	
	public int getScore() {
		return winPile.size();
	}
	
	public void showHand() {
		for(int x = 0; x < hand.size() - 1; x++ ) {
			System.out.println(hand.get(x));
		}
	}
	
}
