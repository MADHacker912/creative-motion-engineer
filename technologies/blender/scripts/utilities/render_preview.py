"""
Render Preview Utility (CME 2.0 Utilities)
Executes a fast preview or final render from the command line or within Blender.
"""

import sys
import argparse
from pathlib import Path

try:
    import bpy
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

if IN_BLENDER:
    CORE_DIR = Path(__file__).resolve().parent.parent / "core"
    sys.path.insert(0, str(CORE_DIR))
    import render_manager

def main():
    parser = argparse.ArgumentParser(description="Render Preview Utility")
    parser.add_argument("--output", "-o", default="/tmp/cme_preview.png", help="Output image file path")
    parser.add_argument("--mode", "-m", choices=["PREVIEW", "FINAL"], default="PREVIEW", help="Render mode")
    parser.add_argument("--frame", "-f", type=int, default=1, help="Frame to render")

    # In Blender, sys.argv contains arguments after '--'
    args_list = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    args = parser.parse_args(args_list)

    if not IN_BLENDER:
        print("[!] Must be executed inside Blender: blender -b scene.blend -P render_preview.py -- -o output.png")
        sys.exit(1)

    print(f"[*] Configuring render mode: {args.mode}...")
    render_manager.configure_render_mode(mode=args.mode)
    print(f"[*] Rendering frame {args.frame} to: {args.output}...")
    render_manager.render_to_file(args.output, frame=args.frame)
    print(f"[✓] Render completed successfully: {args.output}")

if __name__ == "__main__":
    main()
