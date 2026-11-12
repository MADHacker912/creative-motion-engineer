# AGENT INSTALLATION GUIDE: CREATIVE MOTION ENGINEER

This guide explains how to install, register, and activate the **Creative Motion Engineer (CME)** skill across various AI coding agents and CLI environments.

---

## 1. Antigravity Agent Ecosystem

### Location
Copy or symlink the skill directory to the agent's skills repository:
```bash
# User-global installation (available across all projects)
mkdir -p ~/.gemini/config/skills/
cp -r creative-motion-engineer ~/.gemini/config/skills/

# Or project-specific installation
mkdir -p ./skills/
cp -r creative-motion-engineer ./skills/
```

### Verification
In your agent conversation or prompt:
```
Load skill creative-motion-engineer and verify available modules.
```

---

## 2. Claude Code / Anthropic Ecosystem

### Installation
Add the skill path to your project root or user configuration:
```bash
# Add to .claude/skills directory
mkdir -p .claude/skills
cp -r creative-motion-engineer .claude/skills/
```

### Configuration
In your `CLAUDE.md` or `.claude/config.json`:
```json
{
  "skills": [
    ".claude/skills/creative-motion-engineer/SKILL.md"
  ]
}
```

---

## 3. Cursor & Windsurf IDE Rules

### Cursor Rules (.cursorrules or .cursor/rules/)
Create a dedicated motion rule `.cursor/rules/creative-motion.mdc`:
```markdown
---
description: Creative Motion Engineer Guidelines for animations, 3D, and video production
globs: ["**/*.{tsx,jsx,ts,js,css,scss,vert,frag,glsl}"]
---

You are guided by the Creative Motion Engineer skill at `creative-motion-engineer/SKILL.md`.
Follow its core directives:
- Concept before code.
- Anti-slop design: No generic blur blobs or unmotivated wiggles.
- Performance: Strictly animate transform/opacity; clean up GSAP and Three.js memory.
- Accessibility: Provide prefers-reduced-motion fallbacks.
```

---

## 4. Roo Code / Cline

Install into the Cline custom instructions directory:
```bash
mkdir -p ~/.cline/skills/
cp -r creative-motion-engineer ~/.cline/skills/
```

Reference it in your Custom System Prompt:
```
When working on animations, videos, 3D graphics, or landing pages, adhere to the Creative Motion Engineer rules specified in ~/.cline/skills/creative-motion-engineer/SKILL.md.
```

---

## 5. Verification Checklist

- [ ] `SKILL.md` exists and contains valid YAML frontmatter.
- [ ] Sub-directories (`core/`, `domains/`, `technologies/`, `workflows/`, `examples/`, `checklists/`, `resources/`) are present.
- [ ] Agent recognizes commands and references the decision matrix in Section 3 of `SKILL.md`.
