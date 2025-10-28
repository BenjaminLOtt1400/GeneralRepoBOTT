// Title: Forest Wander 
// Author: Ben Ott
// Description: A simple text based game about wanting through a forest

namespace SimpleTextAdventure;


class Program
{
    static void Main(string[] args)
    {
        string playername = "PlaceHolder";
        int apples = 0;
        int snakes = 0;
        string snakefriend = "PlaceHolder";
        int cows = 0;
        string cowfriend = "Placeholder";
        string signname = "PlaceHolder";

        Console.WriteLine("Welcome to your walk through the forest");
        Console.WriteLine("Please enter your name: ");
        playername = Console.ReadLine();
        Console.WriteLine("Well hello " + playername);
        Console.WriteLine("You see a dense forest in front of you that you enter");
        Console.WriteLine("You come across a small group of apple trees. How many do you pick?");
        apples = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Ah Yes " + apples + " apples, that should do.");
        Console.WriteLine("You proceed through the forest and find a den of snakes.");
        Console.WriteLine("You give your " + apples + " to the snakes and in return they let you count them.");
        Console.WriteLine("How many snakes do you count?");
        snakes = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("After counting " + snakes + " snakes, one of them asks to accompany you.");
        Console.WriteLine("What is the name you give your friend");
        snakefriend = Console.ReadLine();
        Console.WriteLine("You and your new friend " + snakefriend + " Continue through the forest");
        Console.WriteLine("You come across a pasture of cows");
        Console.WriteLine("How many cows do you see in the pasture?");
        cows = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Oh Wow! There are " + cows + " Cows in the pasture!");
        Console.WriteLine("You see one particular cow that has fluffy hair");
        Console.WriteLine("You approach the fluffy cow.");
        Console.WriteLine("You seem like an interesting group of people, never thought snakes and people could be friends.");
        Console.WriteLine("Might I accompany you and make you a trio?");
        Console.WriteLine("What do you call your new cow friend?");
        cowfriend = Console.ReadLine();
        Console.WriteLine("You and your friends all approach and old looking cabin.");
        Console.WriteLine("You brush off the dust from the sign and you read aloud what it says.");
        Console.WriteLine("What do you read?");
        signname = Console.ReadLine();
        Console.WriteLine(signname + ": What an interesting name for this cabin.");
        Console.WriteLine("Your trio enters the cabin and find a dinner table set for 3.");
        Console.WriteLine(playername + ", " + snakefriend + "and, " + cowfriend + " all sit at the table and eat dinner.");
        Console.WriteLine("You reflect on your wander through the forest.");
        Console.WriteLine("You collected " + apples + " apples");
        Console.WriteLine("You counted " + snakes + "snakes and met " + snakefriend);
        Console.WriteLine("You counted " + cows + " cows and met " + cowfriend);
        Console.WriteLine("This was a good day!");
    }
}