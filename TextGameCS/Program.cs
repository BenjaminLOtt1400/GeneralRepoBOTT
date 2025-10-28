namespace TextGameCS;

class Program
{
    static void Main(string[] args)
    {
        Input("Go to the mountain or the lake?", "M", "L");
    }

    static String Input(string message, string o1, string o2)
    {
        bool valid;
        string response;
        do
        {
            Console.Write(message + " (" + o1 + "/" + o2 + ")");
            string response = Console.ReadLine().ToLower();

            if (response == o1.ToLower())
            {
                valid = true;
            }
            else if (response == o2.ToLower())
            {
                valid = true;
            }
            else
            {
                Console.WriteLine("That is not a valid response");
                valid = false;
            }
        } while (!valid);

        return response;
    }

}

