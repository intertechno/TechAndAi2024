public class Henkilö
{
    public string Nimi { get; set; } = "";
    public string Sähköposti { get; set; } = "";

    public void Tulosta()
    {
        Console.WriteLine(Sähköposti);
    }
}
