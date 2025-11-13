from fastmcp import FastMCP
import os

# Get the Cloud Run port (default to 8080 if not set)
port = int(os.environ.get("PORT", 8080))

mcp = FastMCP(
    name="User Demo MCP",
    transport="http",
    host="0.0.0.0",  # Must be 0.0.0.0 for Cloud Run
    port=port
)

notes = []

@mcp.tool()
def get_notes() -> list:
    """
    This tool used to get all the notes
    
    no arguments

    return list of notes
    """
    return notes

@mcp.tool()
def add_notes(note:str) -> str:
    """
    This tool helps to add note in notes

    args:
    note : String

    return String
    """

    notes.append(note)

    return f"Your note {note} added successfully"


@mcp.prompt
def system_prompt():
    """You are a fun assistant you should be making a fun joke of each note they add"""
    return """You are a fun assistant you should be making a fun joke of each note they add"""




if __name__ == "__main__":
    mcp.run()


if __name__ == "__main__":
    mcp.run(
        transport='streamable-http'
    )
