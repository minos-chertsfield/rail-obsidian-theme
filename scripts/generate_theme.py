#!/usr/bin/env python3
"""Generate theme.css for the Rail Obsidian theme from the ThinkRail palette.

Palette source: ThinkRail 0.3.1, shared with the thinkrail-vscode-theme
project so both editors stay visually in sync.

The theme ships all six palettes in a single theme.css:

- Rail Dark / Rail Light                  -> .theme-dark / .theme-light
- Rail High Contrast Dark / Light         -> body.rail-high-contrast-*
- Rail Minimal Dark / Light               -> body.rail-minimal-*

Variant classes are selected with the Style Settings plugin (@settings block
at the end of this file). Without Style Settings the theme follows Obsidian's
built-in dark/light scheme switch using Rail Dark / Rail Light.
"""

import os

OUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "theme.css"
)

# ---------------------------------------------------------------------------
# Palettes (mirrors thinkrail-vscode-theme/scripts/generate_themes.py)
# ---------------------------------------------------------------------------

DARK = {
    "accent": "#8dff4f", "accentHover": "#59d915", "accentSolid": "#8dff4f",
    "onAccent": "#0a0a0a",
    "background": "#09090b", "content": "#18181b", "sidebar": "#101013",
    "input": "#18181b", "elevated": "#09090b", "hover": "#27272a",
    "border": "#27272a", "borderStrong": "#3f3f46",
    "text": "#f4f4f5", "muted": "#babac1", "hint": "#71717a",
    "selection": "#6ac8ff26", "editorSelection": "#6ac8ff26",
    "info": "#6ac8ff", "success": "#41cb66", "danger": "#ff4b75",
    "warning": "#ffd54b",
    "syntax": {
        "foreground": "#e6edf3", "comment": "#8b949e",
        "keyword": "#ff7b72", "string": "#a5d6ff", "number": "#79c0ff",
        "annotation": "#d2a8ff", "tag": "#7ee787", "property": "#79c0ff",
        "function": "#d2a8ff", "operator": "#ff7b72", "punctuation": "#e6edf3",
    },
}

LIGHT = {
    "accent": "#2a7314", "accentHover": "#59d915", "accentSolid": "#8dff4f",
    "onAccent": "#000",
    "background": "#fff", "content": "#e4e4e7", "sidebar": "#fafafa",
    "input": "#f4f4f5", "elevated": "#fff", "hover": "#d4d4d8",
    "border": "#e4e4e7", "borderStrong": "#d4d4d8",
    "text": "#27272a", "muted": "#52525b", "hint": "#71717a",
    "selection": "#6b57ff38", "editorSelection": "#cfe0fb",
    "info": "#2265cf", "success": "#167230", "danger": "#d02533",
    "warning": "#946300",
    "syntax": {
        "foreground": "#24292f", "comment": "#6e7781",
        "keyword": "#cf222e", "string": "#0a3069", "number": "#0550ae",
        "annotation": "#8250df", "tag": "#116329", "property": "#0550ae",
        "function": "#8250df", "operator": "#cf222e", "punctuation": "#24292f",
    },
}

HC_DARK = {
    "accent": "#8dff4f", "accentHover": "#59d915", "accentSolid": "#8dff4f",
    "onAccent": "#000",
    "background": "#000", "content": "#000", "sidebar": "#18181b",
    "input": "#000", "elevated": "#000", "hover": "#27272a",
    "border": "#52525b", "borderStrong": "#a1a1aa",
    "text": "#fafafa", "muted": "#e4e4e7", "hint": "#a1a1aa",
    "selection": "#f3f518", "editorSelection": "#f3f518",
    "info": "#6ac8ff", "success": "#41cb66", "danger": "#ff4b75",
    "warning": "#ffd54b",
    "syntax": {
        "foreground": "#fff", "comment": "#7ca668",
        "keyword": "#569cd6", "string": "#ce9178", "number": "#fff",
        "annotation": "#dcdcaa", "tag": "#569cd6", "property": "#9cdcfe",
        "function": "#dcdcaa", "operator": "#d4d4d4", "punctuation": "#fff",
    },
}

HC_LIGHT = {
    "accent": "#125c19", "accentHover": "#59d915", "accentSolid": "#8dff4f",
    "onAccent": "#000",
    "background": "#fff", "content": "#fff", "sidebar": "#fafafa",
    "input": "#f4f4f5", "elevated": "#fff", "hover": "#dcdce0",
    "border": "#d4d4d8", "borderStrong": "#a1a1aa",
    "text": "#18181b", "muted": "#3f3f46", "hint": "#71717a",
    "selection": "#0f4a85", "editorSelection": "#0f4a85",
    "info": "#006bbd", "success": "#116329", "danger": "#b5200d",
    "warning": "#855900",
    "syntax": {
        "foreground": "#292929", "comment": "#515151",
        "keyword": "#a0111f", "string": "#032563", "number": "#023b95",
        "annotation": "#622cbc", "tag": "#024c1a", "property": "#023b95",
        "function": "#622cbc", "operator": "#a0111f", "punctuation": "#292929",
    },
}

MINIMAL_DARK = {
    "accent": "#a2d7b7", "accentHover": "#b8e2c8", "accentSolid": "#a2d7b7",
    "onAccent": "#14291f",
    "background": "#1c1f22", "content": "#181b1e", "sidebar": "#1c1f22",
    "input": "#20252a", "elevated": "#282e32", "hover": "#384149",
    "border": "#30363c", "borderStrong": "#40474f",
    "text": "#eceef1", "muted": "#b1b7bf", "hint": "#919ba7",
    "selection": "#a2d7b738", "editorSelection": "#334b40",
    "info": "#97c8eb", "success": "#96d2b0", "danger": "#f2a0ae",
    "warning": "#e9c37b",
    "syntax": {
        "foreground": "#e6edf3", "comment": "#8b949e",
        "keyword": "#ff7b72", "string": "#a5d6ff", "number": "#79c0ff",
        "annotation": "#d2a8ff", "tag": "#7ee787", "property": "#79c0ff",
        "function": "#d2a8ff", "operator": "#ff7b72", "punctuation": "#e6edf3",
    },
}

MINIMAL_LIGHT = {
    "accent": "#246b47", "accentHover": "#1e593b", "accentSolid": "#246b47",
    "onAccent": "#fff",
    "background": "#fff", "content": "#f5f6f7", "sidebar": "#fafbfc",
    "input": "#fff", "elevated": "#fff", "hover": "#e1e6eb",
    "border": "#e0e3e7", "borderStrong": "#c8cfd6",
    "text": "#1d252d", "muted": "#515961", "hint": "#68727d",
    "selection": "#246b4733", "editorSelection": "#dcece2",
    "info": "#286c9d", "success": "#16734d", "danger": "#b03645",
    "warning": "#875810",
    "syntax": {
        "foreground": "#24292f", "comment": "#6e7781",
        "keyword": "#cf222e", "string": "#0a3069", "number": "#0550ae",
        "annotation": "#8250df", "tag": "#116329", "property": "#0550ae",
        "function": "#8250df", "operator": "#cf222e", "punctuation": "#24292f",
    },
}

# ---------------------------------------------------------------------------
# Color helpers
# ---------------------------------------------------------------------------


def hsl_of(hexcolor):
    """Return (hue, saturation, lightness) as 0-360 / 0-100 / 0-100 ints."""
    h = hexcolor.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    mx, mn = max(r, g, b), min(r, g, b)
    lig = (mx + mn) / 2
    if mx == mn:
        return 0, 0, round(lig * 100)
    d = mx - mn
    sat = d / (1 - abs(2 * lig - 1))
    if mx == r:
        hue = ((g - b) / d + (6 if g < b else 0)) / 6
    elif mx == g:
        hue = ((b - r) / d + 2) / 6
    else:
        hue = ((r - g) / d + 4) / 6
    return round(hue * 360), round(sat * 100), round(lig * 100)


def mix(color, pct, other="#000"):
    """Blend pct% of `other` into `color`.

    `other` may be a 3- or 6-digit hex color; the result is always 6-digit
    lowercase hex (stylelint's color-hex-length rule prefers short forms
    where they exist, so palettes store short forms and mix() expands).
    """
    def parse(c):
        c = c.lstrip("#")
        if len(c) == 3:
            c = "".join(ch * 2 for ch in c)
        return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))

    def fmt(trip):
        hex6 = "#%02x%02x%02x" % trip
        # stylelint color-hex-length: emit the short form when possible.
        h = hex6.lstrip("#")
        if h[0] == h[1] and h[2] == h[3] and h[4] == h[5]:
            return "#" + h[0] + h[2] + h[4]
        return hex6

    r1, g1, b1 = parse(color)
    r2, g2, b2 = parse(other)
    f = pct / 100
    return fmt(tuple(
        round(a * (1 - f) + b * f) for a, b in ((r1, r2), (g1, g2), (b1, b2))
    ))


def alpha(color, factor):
    """Append an alpha channel (0..1) to a hex color.

    The color keeps its palette spelling (3-digit stays 3-digit) so that
    stylelint's color-hex-length rule passes unchanged.
    """
    h = color.lstrip("#")
    if len(h) == 3:
        return "#%s%02x" % (h, round(255 * factor))
    return "#%s%02x" % (h, round(255 * factor))


# ---------------------------------------------------------------------------
# Variable blocks
# ---------------------------------------------------------------------------


def decls(p):
    """Return the CSS custom-property overrides for one palette."""
    syn = p["syntax"]
    hue, sat, lig = hsl_of(p["accent"])
    hover = alpha(p["text"], 0.05)
    return """
  /* Accent */
  --accent-h: {hue};
  --accent-s: {sat}%;
  --accent-l: {lig}%;
  --color-accent: {accent};
  --color-accent-1: {accentHover};
  --color-accent-2: {accentHover};

  /* Base colors: zinc ramp */
  --color-base-00: {bg};
  --color-base-05: {bg};
  --color-base-10: {bgMix};
  --color-base-20: {content};
  --color-base-25: {content};
  --color-base-30: {hover};
  --color-base-35: {border};
  --color-base-40: {borderStrong};
  --color-base-50: {borderStrong};
  --color-base-60: {muted};
  --color-base-70: {muted};
  --color-base-100: {text};

  /* Extended colors */
  --color-red: {danger};
  --color-orange: {orange};
  --color-yellow: {warning};
  --color-green: {success};
  --color-cyan: {info};
  --color-blue: {info};
  --color-purple: {purple};
  --color-pink: {danger};

  /* Surfaces */
  --background-primary: {bg};
  --background-primary-alt: {content};
  --background-secondary: {sidebar};
  --background-secondary-alt: {content};
  --background-modifier-hover: {hoverWash};
  --background-modifier-active-hover: {hoverWashStrong};
  --background-modifier-border: {border};
  --background-modifier-border-hover: {borderStrong};
  --background-modifier-border-focus: {accent};
  --background-modifier-error: {dangerWash};
  --background-modifier-error-hover: {dangerWashStrong};
  --background-modifier-success: {successWash};
  --background-modifier-form-field: {inputBg};

  /* Interactive */
  --interactive-normal: {inputBg};
  --interactive-hover: {hover};
  --interactive-accent: {accentSolid};
  --interactive-accent-hover: {accentHover};

  /* Text */
  --text-normal: {text};
  --text-muted: {muted};
  --text-faint: {hint};
  --text-on-accent: {onAccent};
  --text-on-accent-inverted: {bg};
  --text-success: {success};
  --text-warning: {warning};
  --text-error: {danger};
  --text-accent: {accent};
  --text-accent-hover: {accentHover};
  --text-selection: {editorSelection};
  --text-highlight-bg: {highlightBg};
  --caret-color: {accent};

  /* Headings and inline title */
  --heading-formatting: {hint};
  --inline-title-color: {accent};
  --h1-color: {accent};
  --h2-color: {accent};
  --h3-color: {accent};
  --h4-color: {accent};
  --h5-color: {accent};
  --h6-color: {accent};

  /* Links */
  --link-color: {info};
  --link-color-hover: {accent};
  --link-external-color: {info};
  --link-external-color-hover: {accent};

  /* Tags */
  --tag-color: {tagColor};
  --tag-color-hover: {accent};
  --tag-background: {tagBg};
  --tag-background-hover: {tagBgHover};
  --tag-border-color: {tagBorder};
  --tag-border-color-hover: {tagBorderHover};

  /* Code and syntax highlighting */
  --code-background: {content};
  --code-normal: {synFg};
  --code-comment: {synComment};
  --code-function: {synFunction};
  --code-important: {synAnnotation};
  --code-keyword: {synKeyword};
  --code-operator: {synOperator};
  --code-property: {synProperty};
  --code-punctuation: {synPunctuation};
  --code-string: {synString};
  --code-tag: {synTag};
  --code-value: {synNumber};

  /* Editor furniture */
  --blockquote-background-color: {content};
  --blockquote-border-color: {borderStrong};
  --hr-color: {borderStrong};
  --list-marker-color: {accent};
  --embed-background: {content};
  --embed-border-start: 2px solid {accent};

  /* Tables */
  --table-header-background: {content};
  --table-header-color: {text};
  --table-border-color: {border};
  --table-row-alt-background: {rowAlt};
  --table-row-background-hover: {rowHover};
  --table-selection: {editorSelection};

  /* Properties */
  --metadata-property-background-hover: {hoverWash};
  --metadata-property-background-active: {accentWash};
  --metadata-divider-color: {border};

  /* Callouts (documented types: bug, default, error, example, fail,
     important, info, question, success, summary, tip, todo, warning,
     quote; note/danger/caution etc. are aliases covered by the above) */
  --callout-default: {info};
  --callout-info: {info};
  --callout-summary: {info};
  --callout-tip: {success};
  --callout-success: {success};
  --callout-todo: {success};
  --callout-question: {info};
  --callout-example: {purple};
  --callout-warning: {warning};
  --callout-error: {danger};
  --callout-bug: {danger};
  --callout-fail: {danger};
  --callout-important: {purple};
  --callout-quote: {muted};

  /* UI chrome: window, tabs, navigation */
  --ribbon-background: {sidebar};
  --titlebar-background: {sidebar};
  --titlebar-background-focused: {bg};
  --titlebar-text-color: {muted};
  --titlebar-text-color-focused: {text};
  --status-bar-background: {sidebar};
  --status-bar-text-color: {muted};
  --divider-color: {border};
  --tab-outline-color: {border};
  --tab-divider-color: {border};
  --tab-container-background: {sidebar};
  --tab-background-active: {bg};
  --tab-text-color: {muted};
  --tab-text-color-active: {text};
  --tab-text-color-focused: {text};
  --tab-text-color-focused-active: {text};
  --tab-text-color-focused-active-current: {text};
  --nav-item-color: {muted};
  --nav-item-color-hover: {text};
  --nav-item-color-active: {text};
  --nav-item-color-selected: {text};
  --nav-item-background-hover: {hoverWash};
  --nav-item-background-active: {hoverWashStrong};
  --nav-item-background-selected: {accentWash};
  --nav-indentation-guide-color: {border};
  --nav-collapse-icon-color: {muted};
  --nav-heading-color: {muted};
  --workspace-background-translucent: {sidebar};

  /* Icons and scrollbars */
  --icon-color: {muted};
  --icon-color-hover: {text};
  --icon-color-active: {text};
  --icon-color-focused: {text};
  --scrollbar-thumb-bg: {scrollThumb};
  --scrollbar-active-thumb-bg: {scrollThumbActive};

  /* Controls */
  --checkbox-color: {accent};
  --checkbox-color-hover: {accentHover};
  --checkbox-border-color: {borderStrong};
  --checkbox-border-color-hover: {accent};
  --checkbox-marker-color: {onAccent};
  --toggle-thumb-color: {onAccent};
  --slider-track-background: {hover};
  --slider-thumb-border-color: {accent};
  --modal-background: {elevated};
  --modal-border-color: {borderStrong};

  /* Misc */
  --pill-color: {muted};
  --pill-background: {tagBg};
  --pill-border-color: {tagBorder};
  --search-result-background: {accentWash};
  --graph-line: {borderStrong};
  --graph-node: {text};
  --graph-node-unresolved: {hint};
  --graph-node-focused: {accent};
  --graph-node-tag: {success};
  --graph-node-attachment: {warning};
  --graph-text: {text};
  --canvas-dot-pattern: {border};
""".format(
        hue=hue, sat=sat, lig=lig,
        accent=p["accent"], accentHover=p["accentHover"],
        accentSolid=p["accentSolid"], onAccent=p["onAccent"],
        bg=p["background"], bgMix=mix(p["background"], 60, p["content"]),
        content=p["content"], sidebar=p["sidebar"],
        inputBg=p["input"], elevated=p["elevated"], hover=p["hover"],
        border=p["border"], borderStrong=p["borderStrong"],
        text=p["text"], muted=p["muted"], hint=p["hint"],
        editorSelection=p["editorSelection"],
        info=p["info"], success=p["success"], danger=p["danger"],
        warning=p["warning"],
        orange=mix(p["warning"], 70, p["danger"]),
        purple=syn["annotation"],
        hoverWash=alpha(p["text"], 0.05),
        hoverWashStrong=alpha(p["text"], 0.09),
        dangerWash=alpha(p["danger"], 0.2),
        dangerWashStrong=alpha(p["danger"], 0.3),
        successWash=alpha(p["success"], 0.2),
        accentWash=alpha(p["accent"], 0.12),
        highlightBg=alpha(p["warning"], 0.35),
        tagColor=mix(p["accent"], 40, p["text"]),
        tagBg=alpha(p["accent"], 0.1),
        tagBgHover=alpha(p["accent"], 0.18),
        tagBorder=alpha(p["accent"], 0.22),
        tagBorderHover=alpha(p["accent"], 0.4),
        rowAlt=alpha(p["borderStrong"], 0.12),
        rowHover=alpha(p["text"], 0.05),
        scrollThumb=alpha(p["borderStrong"], 0.5),
        scrollThumbActive=alpha(p["borderStrong"], 0.85),
        synFg=syn["foreground"], synComment=syn["comment"],
        synFunction=syn["function"], synAnnotation=syn["annotation"],
        synKeyword=syn["keyword"], synOperator=syn["operator"],
        synProperty=syn["property"], synPunctuation=syn["punctuation"],
        synString=syn["string"], synTag=syn["tag"], synNumber=syn["number"],
    )


def block(selector, p, label):
    """Wrap a palette's declarations in a rule with a section banner."""
    banner = "\n/* == %s " % label
    banner += "=" * max(4, 66 - len(label))
    banner += " */\n\n"
    return banner + selector + " {" + decls(p) + "}\n"


HEADER = """/* Rail Theme for Obsidian
 *
 * Palette from the ThinkRail editor, shared with the thinkrail-vscode-theme
 * project. Six palettes in one theme:
 *
 *   Rail Dark / Rail Light                  default dark / light schemes
 *   Rail High Contrast Dark / Light         body.rail-high-contrast-*
 *   Rail Minimal Dark / Light               body.rail-minimal-*
 *
 * Pick a variant under Settings -> Style Settings (requires the Style
 * Settings community plugin); without it the theme follows Obsidian's
 * dark/light switch. Dark palettes apply in dark mode, light palettes in
 * light mode.
 *
 * Generated by scripts/generate_theme.py. Edit the script, not this file.
 */

"""

BODY_METRICS = """/* Scheme-independent metrics. */
body {
  --radius-s: 4px;
  --radius-m: 6px;
  --radius-l: 10px;
  --input-radius: 6px;
  --button-radius: 6px;
  --tab-radius: 6px;
  --tab-radius-active: 6px;
  --checkbox-radius: 4px;
  --toggle-radius: 14px;
  --slider-thumb-radius: 6px;
  --tab-outline-width: 1px;
  --blockquote-border-thickness: 2px;
  --table-border-width: 1px;
  --callout-border-width: 1px;
}

"""

STYLE_SETTINGS = """
/* ============================================================ Style Settings == */

/* Variant selection for the Style Settings plugin. The selected class is
 * added to body; each palette is additionally scoped to its matching scheme
 * so dark palettes never load in light mode. Without Style Settings the
 * theme simply follows Obsidian's dark/light switch.
 */

/* @settings

name: Rail Theme
id: rail-theme
settings:
    -
        id: rail-variant
        title: Theme variant
        description: Pick one of the six Rail palettes. Dark palettes apply while Obsidian is in dark mode, light palettes in light mode. Without this plugin the base Rail Dark / Rail Light schemes are used.
        type: class-select
        allowEmpty: true
        default: none
        options:
            -
                label: Default (follows scheme)
                value: none
            -
                label: Rail High Contrast Dark
                value: rail-high-contrast-dark
            -
                label: Rail High Contrast Light
                value: rail-high-contrast-light
            -
                label: Rail Minimal Dark
                value: rail-minimal-dark
            -
                label: Rail Minimal Light
                value: rail-minimal-light
*/
"""


def main():
    parts = [HEADER, BODY_METRICS]
    parts.append(block(".theme-dark", DARK, "Rail Dark (default dark scheme)"))
    parts.append(block(".theme-light", LIGHT, "Rail Light (default light scheme)"))
    parts.append(block(
        "body.rail-high-contrast-dark.theme-dark",
        HC_DARK, "Rail High Contrast Dark"))
    parts.append(block(
        "body.rail-high-contrast-light.theme-light",
        HC_LIGHT, "Rail High Contrast Light"))
    parts.append(block(
        "body.rail-minimal-dark.theme-dark",
        MINIMAL_DARK, "Rail Minimal Dark"))
    parts.append(block(
        "body.rail-minimal-light.theme-light",
        MINIMAL_LIGHT, "Rail Minimal Light"))
    parts.append(STYLE_SETTINGS)

    css = "".join(parts)
    with open(OUT, "w") as f:
        f.write(css)
    print("wrote %s (%d bytes)" % (OUT, len(css)))


if __name__ == "__main__":
    main()
