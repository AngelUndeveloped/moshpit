# MCP Server Tutorial

# Imports
from mcp.server.fastmcp import FastMCP

# Create a new MCP server
server = FastMCP()

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the weather for a given location"""
    return f"The weather in {location} is sunny, with a temperature of 25 degrees Celsius"

@mcp.tool()
def get_news(topic: str) -> str:
    """Get the news for a given topic"""
    return f"The news for {topic} is that the weather is sunny, with a temperature of 25 degrees Celsius"


@mcp.tool()
def get_stock_price(symbol: str) -> str:
    """Get the current stock price for a given symbol"""
    return f"The current stock price for {symbol} is $150.00"

@mcp.tool()
def get_currency_exchange(from_currency: str, to_currency: str) -> str:
    """Get the exchange rate between two currencies"""
    return f"1 {from_currency} = 1.2 {to_currency}"

@mcp.tool()
def get_recipe(ingredient: str) -> str:
    """Get a recipe that uses the given ingredient"""
    return f"Here's a recipe using {ingredient}: Mix with flour, eggs, and milk to make pancakes"

@mcp.tool()
def get_translation(text: str, target_language: str) -> str:
    """Translate text to the target language"""
    return f"Translation of '{text}' to {target_language}: Hola mundo"

@mcp.tool()
def get_definition(word: str) -> str:
    """Get the definition of a word"""
    return f"Definition of {word}: A word used to describe something"

@mcp.tool()
def get_math_solution(equation: str) -> str:
    """Solve a mathematical equation"""
    return f"Solution to {equation}: x = 5"

@mcp.tool()
def get_time(timezone: str) -> str:
    """Get the current time in a given timezone"""
    return f"Current time in {timezone}: 12:00 PM"

@mcp.tool()
def get_distance(from_location: str, to_location: str) -> str:
    """Get the distance between two locations"""
    return f"Distance from {from_location} to {to_location}: 100 kilometers"

@mcp.tool()
def get_population(city: str) -> str:
    """Get the population of a city"""
    return f"Population of {city}: 1,000,000"

@mcp.tool()
def get_holiday(date: str) -> str:
    """Get the holiday on a given date"""
    return f"Holiday on {date}: New Year's Day"

# Add the tool to the server
server.add_tool(get_weather)

# Run the server
server.run()