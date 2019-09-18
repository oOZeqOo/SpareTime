package PlayArea;

import java.io.FileNotFoundException;
import java.util.ArrayList;

import DeckOfCards.Card;
import DeckOfCards.Deck;
import Player.Player;
import javafx.scene.image.Image;

public class PlayArea {

	public Player player1 = new Player("Player 1"); 
	public Player player2 = new Player("Player 2"); 
	protected static int score[] = {0 , 0};
	private static ArrayList<Card> stack = new ArrayList<Card>();
	
	public PlayArea() {
		
	}
	
	public void initiatePlayArea() {
		try {
			Deck.generateDeck();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		Deck.shuffleDeck(Deck.deck);
		initiatePlayers(); 
	}
	
	public void initiatePlayers() {
		int x = 0;
		clearWinPiles();
		while(x < Deck.getSize()) {
			player1.addCard(player1.hand, Deck.deck[x]);
			player2.addCard(player2.hand, Deck.deck[x+1]);
			x += 2;
		}
	}
	
	public void clearWinPiles() {
		while(player1.winPile.size() > 0)
			player1.winPile.remove(0);
		while(player2.winPile.size() > 0)
			player2.winPile.remove(0);
	}
	
	public void playGame() {
		
		if((player1.hand.size() > 0) && (player2.hand.size() > 0)) {
			
			Card p1 = player1.playCard();
			stack.add(p1);
			
			Card p2 = player2.playCard();
			stack.add(p2);
			
			if ((int)p1.getNumber() >  (int)p2.getNumber()) {
				
				System.out.println("Player 1 wins this round!");
				
				while(stack.size() > 0) {
					player1.addCard(player1.winPile, stack.get(0));
					player1.addCard(player1.winPile, stack.get(1));
					stack.remove(stack.get(0));
					stack.remove(stack.get(0));
				}
			
			}
			if ((int)p2.getNumber() > (int)p1.getNumber()) {
				
				System.out.println("Player 2 wins this round!");	
				
				while(stack.size() > 0) {
					player2.addCard(player2.winPile, stack.get(0));
					player2.addCard(player2.winPile, stack.get(1));
					stack.remove(0);
					stack.remove(0);
				}
			}
			 if ((int)p2.getNumber() == (int)p1.getNumber()){
				playGame();
			}//end of little if
		
			System.out.println("\nPlayer 1 score: " + player1.getScore());
			System.out.println("Player 2 score: " + player2.getScore());
			
		}//end of big if	
		else {
			
			declareWinner();
			System.exit(0);
			
		}
		
	}
	
	public int getP1Score() {
		 
		return player1.getScore();
	}
	public int getP2Score() {
		return player2.getScore();
	}
	
	public static boolean hasCards(Player player) {
		if (player.hand.isEmpty() )
			return false;
		return true;
	}
	
	public Image getPlayer1Card() {
		if(player1.hand.size() < 1)
			return null;
		return player1.hand.get(0).getImage();
	}
	public Image getPlayer2Card() {
		if(player1.hand.size() < 1)
			return null;
		return player2.hand.get(0).getImage();
	}
	
	public void declareWinner() {
		if(player1.winPile.size() > player2.winPile.size()) {
			System.out.println("Player 1 won the game with : " + player1.winPile.size() + " cards won!");
			System.out.println("\nPlayer 2 lost the game with : " + player2.winPile.size() + " cards!");
		}
		else if(player2.winPile.size() > player1.winPile.size()) {
			System.out.println("Player 2 won the game with : " + player2.winPile.size() + " cards!");
			System.out.println("\nPlayer 1 lost the game with : " + player1.winPile.size() + " cards!");
		}
		else
			System.out.println("Tie Game!\n");	
	}
	
}
