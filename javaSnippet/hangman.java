package proj;
/*description
    user story - 
    given list of 10 words, ask user for guess of letter
    if letter is in word, it reveals it

    every time game starts, program randomly selects 1 of 10
    case independent

    >>>c
    >>>c _ _ _

    >>>5 guesses in total
    >>>when over, it says you ran out

    
*/
import java.util.Scanner;
import java.util.Random;

public class hangman {
    private int life;
    private int charLeft;
    private char[] word;
    private char[] hiddenWord;
    private boolean alive;
    private String lettersUsed;

    public static String[] str = {"average", "candidate", "hesitate", "unlawful", "paradox", "offender", "popular", "genetic", "justify", "preference"};

    public hangman() {
        Random r = new Random();

        this.life = 5;
        this.word = str[r.nextInt(10)].toCharArray();
        this.hiddenWord = new char[this.word.length];
        this.alive = true;
        this.charLeft = this.word.length;
        this.lettersUsed = "";
        for (int i = 0; i < this.word.length; i++) {
            this.hiddenWord[i] = '_';
        }

        System.out.println("");
    }
    
    private char[] formatString(char[] str) {
        char[] hiddenWordString;
        hiddenWordString = new char[2*str.length];
        for (int i = 0; i<str.length; i++) {
            if (str[i] == '_') {
                hiddenWordString[2*i] = '_';
            } else {
                hiddenWordString[2*i] = str[i];
            }
            hiddenWordString[2*i + 1] = ' ';
        }
        return hiddenWordString;
    }

    private void guessCharacter(char c) {
        boolean isInWord = false;
        //is char in word
        this.lettersUsed += String.valueOf(c) + " ";

        for (int i = 0; i < this.word.length; i++) {
            if (this.word[i] == c) {
                isInWord = true;
                this.hiddenWord[i] = c;
                this.charLeft--;
            }
        }

        System.out.println("You used " + this.lettersUsed);
        if (!isInWord) {
            if (this.life <= 1) {
                this.alive = false;
                System.out.println("You lose");
            } else {
                this.life--;
                System.out.println(c + " is not in the word");
                System.out.println(this.life + " live(s) remaining");
                System.out.println(formatString(this.hiddenWord));
            }
        } else {
            System.out.println("Yes, the word contains " + c);
            System.out.println(formatString(this.hiddenWord));
            if (this.charLeft == 0) {
                System.out.println("You guessed the word. You win!");
                this.alive = false;
            }
        }
    }

    public static void main(String[] args) {
        hangman h;
        String s;
        char c;
        
        Scanner sc = new Scanner(System.in);
        //loop
        while (true) {
            h = new hangman();

            System.out.println("Let's play hangman");
            System.out.println("The word is " + new String(h.formatString(h.hiddenWord)));
            while (h.alive) {
                System.out.println("Guess a character");
                c = sc.next().charAt(0);
                h.guessCharacter(c);
            }
            System.out.println("The word was " + new String(h.word));
        }   
    }
}