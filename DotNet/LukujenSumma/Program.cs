Console.WriteLine("Tervetuloa laskin-sovellukseen!");

Console.WriteLine("Syötä ensimmäinen luku:");
string syöte1 = Console.ReadLine() ?? "0";
Console.WriteLine("Syötä toinen luku:");
string syöte2 = Console.ReadLine() ?? "0";

int luku1 = int.Parse(syöte1);
int luku2 = int.Parse(syöte2);

int summa = luku1 + luku2;
Console.WriteLine("Lukujen summa on: " + summa);

int neliöidenSumma = (luku1 * luku1) + (luku2 * luku2);
Console.WriteLine("Lukujen neliöiden summa on: " + neliöidenSumma);
