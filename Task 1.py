import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {

    public static int playGame() {
        Random random = new Random();
        int numberToGuess = random.nextInt(100) + 1;
        int maxAttempts = 10;
        int attempts = 0;

        Scanner scanner = new Scanner(System.in);
        System.out.println("\nI have selected a number between 1 and 100.");
        System.out.println("You have " + maxAttempts + " attempts to guess the number.");

        while (attempts < maxAttempts) {
            System.out.print("\nAttempt " + (attempts + 1) + ": Enter your guess: ");
            
            if (!scanner.hasNextInt()) {
                System.out.println("Please enter a valid number!");
                scanner.next();
                continue;
            }
            
            int guess = scanner.nextInt();
            attempts++;

            if (guess < numberToGuess) {
                System.out.println("Too low! Try again.");
            } else if (guess > numberToGuess) {
                System.out.println("Too high! Try again.");
            } else {
                System.out.println("Congratulations! You guessed the correct number in " + attempts + " attempts.");
                return maxAttempts - attempts + 1;
            }
        }

        System.out.println("Sorry, you've used all your attempts! The number was " + numberToGuess + ".");
        return 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to the Number Guessing Game!");

        int totalScore = 0;
        int roundNumber = 1;

        while (true) {
            System.out.println("\n--- Round " + roundNumber + " ---");
            totalScore += playGame();
            System.out.println("Your current score: " + totalScore);

            System.out.print("\nDo you want to play again? (yes/no): ");
            String playAgain = scanner.next().trim().toLowerCase();
            if (!playAgain.equals("yes")) {
                break;
            }
            roundNumber++;
        }

        System.out.println("\nGame Over! Your final score is " + totalScore + ". Thanks for playing!");
        scanner.close();
    }
}
