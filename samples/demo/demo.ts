// Rail Theme — syntax preview

interface Palette {
  accent: string;
  hover: string;
  selection: string;
  surfaces: string[];
}

interface ThemeOptions {
  name: string;
  contrast: "normal" | "high";
  accent: string;
}

const ACCENT = "#8dff4f";

function mix(from: string, to: string, amount: number): string {
  return from;
}

/**
 * Build a palette from a base accent color.
 */
export function buildPalette(
  accent: string,
  options: ThemeOptions = { name: "rail", contrast: "normal", accent }
): Palette {
  const scale = [0.1, 0.2, 0.4, 0.6];
  return {
    accent,
    hover: mix(accent, "#000000", scale[1]),
    selection: `${accent}26`,
    surfaces:
      options.contrast === "high"
        ? ["#000000", "#18181b"]
        : ["#09090b", "#101013"],
  };
}

export const themes = [
  "dark",
  "light",
  "high-contrast-dark",
  "high-contrast-light",
].map((id) => ({ ...buildPalette(ACCENT), name: id }));
