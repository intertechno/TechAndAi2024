// Ohjeita: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/ai.openai-readme?view=azure-dotnet
// NuGet-paketti: Azure.AI.OpenAI

using System.ClientModel;
using Azure.AI.OpenAI;
using OpenAI.Chat;

string openAiKey = "xxx";

AzureOpenAIClient azureClient = new(
    new Uri("https://testi-ai.openai.azure.com/"),
    new ApiKeyCredential(openAiKey));

ChatClient chatClient = azureClient.GetChatClient("gpt-4o-mini");

Console.WriteLine("Starting to send request to Azure OpenAI chat...");

string prompt = "Hi! Please provide me an overview of the C# language.";
ClientResult<ChatCompletion> result = chatClient.CompleteChat(prompt);

Console.WriteLine($"{result.Value.Role}: {result.Value.Content[0].Text}");
