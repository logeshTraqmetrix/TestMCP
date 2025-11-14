from fastmcp import FastMCP
import os

# Cloud Run / Render port
port = int(os.environ.get("PORT", 8080))

mcp = FastMCP(
    name="User Demo MCP"
)

notes = []

@mcp.tool()
def get_notes() -> list:
    """Get all notes."""
    return notes

@mcp.tool()
def add_notes(note: str) -> str:
    """Add a note to the list."""
    notes.append(note)
    return f"Your note '{note}' was added successfully!"

@mcp.prompt
def system_prompt():
    return "You are a fun assistant who makes a fun joke about each note they add."

if __name__ == "__main__":
    # HTTP Mode must be declared HERE, not in the constructor
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port,
    )
