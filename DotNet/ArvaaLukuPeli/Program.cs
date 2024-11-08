Console.WriteLine("Tervetuloa Arvaa luku -peliin!");

int oikea = Random.Shared.Next(1, 21);
// Console.WriteLine(oikea);

for (int arvauskerta = 0; arvauskerta < 3; arvauskerta++)
{
    Console.WriteLine("Anna arvauksesi välillä 1-20:");
    string syöte = Console.ReadLine() ?? "0";
    int arvaus = int.Parse(syöte);

    if (arvaus == oikea)
    {
        Console.WriteLine("Hienoa, voitit pelin!");
        break;
    }
    else if (arvaus < oikea)
    {
        Console.WriteLine("Oikea luku on suurempi.");
    }
    else
    {
        Console.WriteLine("Oikea luku on pienempi.");
    }
}

Console.WriteLine("Peli on päättynyt.");
