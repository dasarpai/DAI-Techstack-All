"use client";

import { useState } from "react";
import { Send } from "lucide-react";

// Add interface for message structure
interface Message {
  role: "user" | "assistant" | "error";
  content: string;
  isUpdate?: boolean;
}

const AgentChat = () => {
  const [prompt, setPrompt] = useState<string>("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleReset = () => {
    setMessages([]);
    setPrompt("");
    setIsLoading(false);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!prompt.trim() || isLoading) return;

    setIsLoading(true);
    setMessages((prev) => [...prev, { role: "user", content: prompt }]);

    try {
      const response = await fetch("/api/agent", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      });

      const data = await response.json();

      if (response.ok) {
        // Add intermediate updates
        data.updates.forEach((update: { type: string; content: string }) => {
          setMessages((prev) => [
            ...prev,
            {
              role: "assistant",
              content: `[${update.type}] ${update.content}`,
              isUpdate: true,
            },
          ]);
        });

        // Add final response
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            content: data.result,
          },
        ]);
      } else {
        throw new Error(data.error || "Failed to get response");
      }
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "error",
          content: error instanceof Error ? error.message : "An error occurred",
        },
      ]);
    } finally {
      setIsLoading(false);
      setPrompt("");
    }
  };

  return (
    <div className="w-full max-w-2xl mx-auto p-4 space-y-4">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold text-gray-800">
          Bee Agent Framework Chat
        </h1>
        <button
          onClick={handleReset}
          className="px-4 py-2 text-sm bg-gray-100 text-gray-600 rounded-lg hover:bg-gray-200 transition-colors"
        >
          Reset Chat
        </button>
      </div>
      <div className="bg-white rounded-lg shadow-md p-4 space-y-4 min-h-[400px] max-h-[600px] overflow-y-auto">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`p-3 rounded-lg ${
              message.role === "user"
                ? "bg-blue-100 ml-auto max-w-[80%]"
                : message.role === "error"
                  ? "bg-red-100 w-full"
                  : message.isUpdate
                    ? "bg-gray-50 text-sm border-l-4 border-blue-400 pl-4 my-1 w-full"
                    : "bg-gray-100 w-full"
            }`}
          >
            {message.isUpdate ? (
              <div className="space-y-1">
                <span className="font-medium text-blue-600 break-words">
                  {message.content.match(/\[(.*?)\]/)?.[1]}
                </span>
                <p className="text-gray-700 break-words whitespace-pre-wrap">
                  {message.content.replace(/\[(.*?)\]\s*/, "")}
                </p>
              </div>
            ) : (
              <p className="break-words whitespace-pre-wrap">
                {message.content}
              </p>
            )}
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt..."
          className="flex-1 p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          disabled={isLoading}
        />
        <button
          type="submit"
          disabled={isLoading}
          className="p-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed"
        >
          <Send className="w-5 h-5" />
        </button>
      </form>
    </div>
  );
};

export default AgentChat;
