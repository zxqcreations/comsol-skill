#!/bin/bash
# Install COMSOL Skill + MCP Server for Claude Code
# Usage: bash install.sh

SKILL_DIR="$HOME/.claude/skills/comsol-skill"
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== COMSOL Skill + MCP Server Installer ==="
echo ""

# 1. Install skill definition
echo "[1/3] Installing skill to $SKILL_DIR ..."
mkdir -p "$SKILL_DIR"
cp "$PROJECT_DIR/SKILL.md" "$SKILL_DIR/"
cp -r "$PROJECT_DIR/references" "$SKILL_DIR/"
cp -r "$PROJECT_DIR/scripts" "$SKILL_DIR/"
cp -r "$PROJECT_DIR/web" "$SKILL_DIR/"
echo "  Skill installed."

# 2. Install MCP server
echo "[2/3] Installing MCP server dependencies ..."
cd "$PROJECT_DIR/mcp_server"
pip install -e . 2>/dev/null || pip install -r requirements.txt
echo "  MCP server dependencies installed."

# 3. Configure Claude Code MCP
echo "[3/3] Configuring Claude Code MCP ..."
CLAUDE_JSON="$HOME/.claude.json"

python3 -c "
import json, sys, os

config_path = os.path.expanduser('$CLAUDE_JSON')
try:
    with open(config_path, 'r') as f:
        config = json.load(f)
except:
    config = {}

if 'mcpServers' not in config:
    config['mcpServers'] = {}

config['mcpServers']['comsol'] = {
    'command': 'python',
    'args': ['-m', 'src.server'],
    'cwd': '$PROJECT_DIR/mcp_server'
}

with open(config_path, 'w') as f:
    json.dump(config, f, indent=2)

print('  MCP server configured in ~/.claude.json')
" 2>/dev/null || echo "  WARNING: Could not auto-configure MCP. Add manually to ~/.claude.json"

echo ""
echo "=== Installation complete ==="
echo ""
echo "Skill:  $SKILL_DIR"
echo "MCP:    $PROJECT_DIR/mcp_server"
echo ""
echo "To use: restart Claude Code, then type: /comsol-skill"
