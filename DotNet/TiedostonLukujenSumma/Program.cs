Console.WriteLine("Tiedoston lukujen summa alkaa.");

int summa = 0;
int lkm = 0;

string[] rivit = File.ReadAllLines("Luvut.txt");
foreach (string rivi in rivit)
{
    // Console.WriteLine(rivi);
    int luku = int.Parse(rivi);

    summa += luku;
    lkm++;
}

Console.WriteLine("Tiedoston lukujen summa: " + summa);

float keskiarvo = (float)summa / lkm;
Console.WriteLine("Tiedoston lukujen keskiarvo: " + keskiarvo);
