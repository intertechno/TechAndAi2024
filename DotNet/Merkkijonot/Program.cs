using System.Text;

Console.WriteLine("Merkkijonojen käsittely alkaa.");

DateTime alku = DateTime.Now;

StringBuilder rakentaja = new("");
for (int i = 0; i < 500_000; i++)
{
    rakentaja.Append('A');
}
string s = rakentaja.ToString();

// string s = "";
// for (int i = 0; i < 600_000; i++) {
//    s = s + "A";
// }

DateTime loppu = DateTime.Now;

TimeSpan kulunutAika = loppu - alku;
Console.WriteLine("Operaation kesto: " + kulunutAika.TotalSeconds);
Console.WriteLine("Merkkijonojen käsittely on päättynyt.");
