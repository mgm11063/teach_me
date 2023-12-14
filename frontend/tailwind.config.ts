import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        "C-dark-light": "#3D414C",
        "C-dark": "#050C16",
        "C-red": "#ED2B2A",
        "C-white": "#FAFAFA",
        "C-gray": "C9D6DF",
        "C-red-100": "#D21312",
        "C-red-300": "#F15A59",
      },
    },
  },
  plugins: [],
};
export default config;
