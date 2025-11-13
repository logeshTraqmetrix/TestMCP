from fastmcp import FastMCP
import os

# Get the Cloud Run port (default to 8080 if not set)
port = int(os.environ.get("PORT", 8080))

mcp = FastMCP(
    name="User Demo MCP",
    transport='streamable-http',          # ← This enables HTTP server mode
    host="0.0.0.0",            # ← Required for Cloud Run
    port=port                  # ← Must match PORT env var
)

notes = []

@mcp.tool()
def get_notes() -> list:
    """
    Get all the notes.
    No arguments.
    Returns a list of notes.
    """
    return notes

@mcp.tool()
def add_notes(note: str) -> str:
    """
    Add a note to the list.
    Args:
        note (str): The note to add.
    Returns:
        str: Confirmation message.
    """
    notes.append(note)
    return f"Your note '{note}' was added successfully!"

@mcp.prompt
def system_prompt():
    """You are a fun assistant who makes a fun joke about each note they add."""
    return "You are a fun assistant who makes a fun joke about each note they add."

# Only run once — with HTTP server
if __name__ == "__main__":
    mcp.run()  # ← Uses 'http' transport from constructor