using System.Text.Json;

Console.WriteLine("Olio-ohjelmoinnin demo alkaa.");

List<int> luvut = [1, 2, 3];
List<Henkilö> henkilöt = [
    new() { Nimi = "Matti Möttönen", Sähköposti = "matti@kotinetti.fi" },
    new() { Nimi = "Kaija Kokeilija", Sähköposti = "kaija@testi.com" },
    new() { Nimi = "Anna Saarinen", Sähköposti = "anna.saarinen@webmail.com" },
    new() { Nimi = "Juha Korhonen", Sähköposti = "juha.korhonen@netti.com" }
];

foreach (Henkilö h in henkilöt)
{
    Console.WriteLine(h.Nimi + ": " + h.Sähköposti);
}

string json = JsonSerializer.Serialize(henkilöt);
File.WriteAllText("Henkilöt.json", json);
Console.WriteLine("JSON-tiedosto kirjoitettu.");

/*
Henkilö h = new()
{
    Nimi = "Matti Möttönen",
    Sähköposti = "matti@kotinetti.fi"
};

Console.WriteLine(h.Nimi);
Console.WriteLine(h.Sähköposti);

Henkilö h2 = new()
{
    Nimi = "Kaija Kokeilija",
    Sähköposti = "kaija@testi.com"
};

Console.WriteLine(h2.Nimi);
Console.WriteLine(h2.Sähköposti);
*/